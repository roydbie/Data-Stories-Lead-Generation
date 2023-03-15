<template>
  <div id="WasteBinsChart"></div>
</template>

<script>

export default {
  name: "WasteBinsChart",
  props: {
    data: Array,
  },
  data() {
    return {
      chartData: [],
    }
  },
  mounted() {
    this.data.forEach(item => {
      if (item.amountOfBins !== null && item.amountOfResidents !== null) {
        this.chartData.push({amountOfBins: item.amountOfBins, amountOfResidents: item.amountOfResidents})
      }
    })
  },
};

</script>
