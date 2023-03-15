<template>
  <Scatter
      :options="chartOptions"
      :data="chartData"
      v-if="loaded"
  />
</template>

<script>
import {
  Chart as ChartJS,
  LinearScale,
  PointElement,
  LineElement,
  Tooltip,
  Legend
} from 'chart.js'
import { Scatter } from 'vue-chartjs'

ChartJS.register(LinearScale, PointElement, LineElement, Tooltip, Legend)

export default {
  name: "WasteBinsChart",
  components: { Scatter },
  props: {
    data: Array,
  },
  data() {
    return {
      chartData: {
        datasets: [
          {
            label: 'Test voor nu',
            fill: false,
            borderColor: '#f87979',
            backgroundColor: '#f87979',
            data: []
          }
        ]
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false
      },
      loaded: false
    }
  },
  mounted() {
    const datasets = [];
    this.data.forEach(item => {
      if (item.amountOfBins !== null && item.amountOfResidents !== null) {
        datasets.push({x: item.amountOfResidents, y: item.amountOfBins});
      }
    })
    this.chartData.datasets[0].data = datasets;
    this.loaded = true;
  },
};

</script>
