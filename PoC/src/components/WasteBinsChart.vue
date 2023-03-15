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
        datasets: []
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            display: false
          }
        },
        scales: {
          x: {
            title: {
              display: true,
              text: 'Amount of residents in the neighbourhood'
            }
          },
          y: {
            title: {
              display: true,
              text: 'Amount of waste bins in the neighbourhood'
            }
          }
        }
      },
      loaded: false
    }
  },
  mounted() {
    const datasets = [];
    this.data.forEach(item => {
      if (item.amountOfBins !== null && item.amountOfResidents !== null) {
        datasets.push({label: item.neighbourhoodName + " (Residents, Waste bins)", fill: false, borderColor: '#f87979', backgroundColor: '#f87979', data: [{x: item.amountOfResidents, y: item.amountOfBins}]});
      }
    })
    this.chartData.datasets = datasets;
    this.loaded = true;
  },
};

</script>
