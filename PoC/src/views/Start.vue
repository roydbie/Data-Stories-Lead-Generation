<script setup>

</script>

<template>
  <main>
    Start  hallooooo
    {{ data }}
  </main>
</template>

<script>
import axios from 'axios';

export default {
    data() {
      return {
        data: null
      }
    },
  mounted() {
    axios
        .get('https://api.coindesk.com/v1/bpi/currentprice.json')
        .then(response => (this.data = response))
  }

}
</script>
