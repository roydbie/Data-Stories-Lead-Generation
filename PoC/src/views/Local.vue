<script setup>

</script>

<template>
  <main>

    <div v-if="loading === true" class="m-auto" style="text-align: center;">
      <div class="spinner-border" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>

    <div v-if="loading === false" class="row">
      <div class="col">
        <h1>{{ wasteBinsRowCount }}</h1>
        <table class="table">
          <thead>
          <tr>
            <th scope="col"><b>Neighbourhood</b></th>
            <th scope="col"><b>Neighbourhood code</b></th>
            <th scope="col"><b>Amount of waste bins</b></th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="row in wasteBinsData">
              <th scope="row">{{ row.neighbourhoodName }}</th>
              <td>{{ row.neighbourhoodCode }}</td>
              <td>{{ row.amountOfBins }}</td>
          </tr>
          </tbody>
        </table>
      </div>
      <div class="col">

      </div>
    </div>

  </main>
</template>

<script>
import axios from 'axios';

export default {
    data() {
      return {
        wasteBinsData: null,
        loading: false,
        wasteBinsRowCount: 0,
      }
    },
  mounted() {
    this.loading = true;
    axios
        .get('afvalbakken.json')
        .then(response => {

          let allRowsFromResponse = [...new Set(response.data)];

          const countBinsPerNeighbourhood = allRowsFromResponse.map(value => [value.buurt, response.data.filter(str => str.buurt === value.buurt).length]);

          const convertedArrayOfObjects = [];
          countBinsPerNeighbourhood.forEach(item => {
            convertedArrayOfObjects.push({neighbourhoodName: item[0], amountOfBins: item[1]})
          })

          this.wasteBinsData = convertedArrayOfObjects.filter((value, index) => {
            const _value = JSON.stringify(value);
            return index === convertedArrayOfObjects.findIndex(obj => {
              return JSON.stringify(obj) === _value;
            });
          });

          this.wasteBinsData.find(item => item.neighbourhoodName === null).neighbourhoodName = "Parkforum";
          this.wasteBinsData.sort();

        })
        .then(() => {
          axios
              .get('buurten.json')
              .then(response => {
                response.data.forEach(buurt => {
                  if (this.wasteBinsData.find(item => item.neighbourhoodName === buurt.buurtnaam)) {
                    this.wasteBinsData.find(item => item.neighbourhoodName === buurt.buurtnaam).neighbourhoodCode = buurt.buurtnaam;
                  }
                })
              })
        })
        .then(() => {
          this.loading = false;
          this.wasteBinsRowCount = this.wasteBinsData.length;
        })


  }

}
</script>
