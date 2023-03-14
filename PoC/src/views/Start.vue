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
      <h2 v-if="data !== null">Aantal rows in tabel: {{ data.length }}</h2>

      <table class="table">
        <thead>
          <tr>
            <th scope="col">Straatnaam</th>
            <th scope="col">Soort</th>
            <th scope="col">Aantal parkeerplaatsen</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="row in data">
            <th scope="row">{{ row.fields.straat }}</th>
            <td>{{ row.fields.type_en_merk }}</td>
            <td>{{ row.fields.aantal }}</td>
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
        data: null,
        loading: false
      }
    },
  mounted() {
    this.loading = true;
    axios
        .get('https://data.eindhoven.nl/api/records/1.0/search/?dataset=parkeerplaatsen&q=&rows=10000&facet=straat&facet=type_en_merk&facet=aantal')
        .then(response => (this.data = response.data.records))
        .then(() => {this.loading = false})
  }

}
</script>
