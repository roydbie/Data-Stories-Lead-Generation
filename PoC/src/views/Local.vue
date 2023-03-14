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
            <th scope="col">Stadsdeel</th>
            <th scope="col">Buurt</th>
            <th scope="col">Aantal afvalbakken</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="row in afvalbakkenData">
            <template v-if="row[0] && row[1]">
              <th scope="row">{{ row[0] }}</th>
              <td>{{ row[1] }}</td>
              <td>{{ row[2] }}</td>
            </template>
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
        afvalbakkenData: null,
        loading: false
      }
    },
  mounted() {
    this.loading = true;
    axios
        .get('afvalbakken.json')
        .then(response => {

          let uniekeElementen = [...new Set(response.data)];

          const elementenTellen = uniekeElementen.map(value => [value.stadsdeel, value.buurt, response.data.filter(str => str.buurt === value.buurt && str.stadsdeel === value.stadsdeel).length]);

          this.afvalbakkenData = elementenTellen.filter((value, index) => {
            const _value = JSON.stringify(value);
            return index === elementenTellen.findIndex(obj => {
              return JSON.stringify(obj) === _value;
            });
          }).sort();
        })
        .then(() => {
          this.loading = false
        })
  }

}
</script>
