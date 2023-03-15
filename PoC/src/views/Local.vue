<script setup>

</script>

<template>
  <main>

    <div v-if="loading === true" class="m-auto" style="text-align: center;">
      <div class="spinner-border" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>

    <div v-if="loading === false" class="row" style="max-width: 100%;">
      <div class="col" style="max-height: 80vh!important;overflow: scroll;">
        <h1>{{ wasteBinsRowCount }}</h1>
        <table class="table">
          <thead>
          <tr>
            <th scope="col"><b>Neighbourhood</b></th>
            <th scope="col"><b>Neighbourhood code</b></th>
            <th scope="col"><b>Amount of waste bins</b></th>
            <th scope="col"><b>Amount of residents</b></th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="row in wasteBinsData">
              <th scope="row">{{ row.neighbourhoodName }}</th>
              <td>{{ row.neighbourhoodCode }}</td>
              <td>{{ row.amountOfBins }}</td>
              <td>{{ row.amountOfResidents }}</td>
          </tr>
          </tbody>
        </table>
      </div>
      <div class="col" style="max-height: 80vh!important;overflow: scroll;padding:2rem;">
        <template v-if="wasteBinsData != null">
          <WasteBinsChart :data="wasteBinsData"></WasteBinsChart>
        </template>
      </div>
    </div>

  </main>
</template>

<script>
import axios from 'axios';
import WasteBinsChart from "@/components/WasteBinsChart.vue";

export default {
    components: {
      WasteBinsChart
    },

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
                    this.wasteBinsData.find(item => item.neighbourhoodName === buurt.buurtnaam).neighbourhoodCode = buurt.buurtcode;
                  }
                })
              })
        })
        .then(() => {
          axios
              .get('bevolking.json')
              .then(response => {
                response.data.forEach(buurt => {
                  if (this.wasteBinsData.find(item => item.neighbourhoodCode === buurt.buurtcode)) {
                    this.wasteBinsData.find(item => item.neighbourhoodCode === buurt.buurtcode).amountOfResidents = buurt.totaal_aantal_inwoners;
                  }
                })
              })
              .then(() => this.loading = false)
        })
        .then(() => {
          this.wasteBinsRowCount = this.wasteBinsData.length;
        })


  }

}
</script>
