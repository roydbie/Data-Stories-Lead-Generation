<script setup>

</script>

<template>
  <main>

    <div v-if="loading === true" class="m-auto" style="text-align: center;">
      <div class="spinner-border" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>

    <div v-if="loading === false">

      <table class="table">
        <thead>
          <tr>
            <th scope="col">Straatnaam</th>
            <th scope="col">Type</th>
            <th scope="col">Aantal parkeerplaatsen</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="row in parkeerplaatsData">
            <th scope="row">{{ row[0] }}</th>
            <td>{{ row[1] }}</td>
            <td>{{ row[2] }}</td>
          </tr>
        </tbody>
      </table>
    </div>

  </main>
</template>

<script>
import axios from 'axios';

export default {
    data() {
      return {
        parkeerplaatsData: null,
        loading: false
      }
    },
  mounted() {
    this.loading = true;
    axios
        .get('https://data.eindhoven.nl/api/records/1.0/search/?dataset=parkeerplaatsen&q=&rows=10000&start=0&sort=straat&facet=straat&facet=type_en_merk&facet=aantal')
        .then(response => {

          let uniekeElementen = [...new Set(response.data.records)];

          const elementenTellen = uniekeElementen.map(value => [value.fields.straat, value.fields.type_en_merk, response.data.records.filter(str => str.fields.straat === value.fields.straat && str.fields.type_en_merk === value.fields.type_en_merk).length]);

          this.parkeerplaatsData = elementenTellen.filter((value, index) => {
            const _value = JSON.stringify(value);
            return index === elementenTellen.findIndex(obj => {
              return JSON.stringify(obj) === _value;
            });
          });
        })
        .then(() => {
          this.loading = false
        })
  }

}
</script>
