<template>
  <v-container>
    <apexchart type="area" height="350" ref="chart" :options="chartOptions" :series="chartData"></apexchart>
  </v-container>
</template>

<script>
import {getStatistics} from "@/services/statisticServise.js"

export default {
  data() {
    return {
        chartData: [],
        chartOptions: {
            chart: {
              id: 'area-datetime',
              type: 'area',
              height: 350,
              zoom: {
                autoScaleYaxis: true
              },
              events: {
                dataPointSelection: this.dataPointSelection
              }
            },
            dataLabels: {
              enabled: false
            },
            markers: {
              size: 10,
              style: 'hollow',
            },
            xaxis: {
              type: 'datetime',
              tickAmount: 6,
            },
            tooltip: {
              x: {
                format: 'dd MMM yyyy'
              },
              intersect: true,
              shared: false,
            },
            fill: {
              type: 'gradient',
              gradient: {
                shadeIntensity: 1,
                opacityFrom: 0.7,
                opacityTo: 0.9,
                stops: [0, 100]
              }
            },
        }
    };
  },
  async mounted() {
    await this.updateData()
  },
    methods: {
      async updateData() {
          var datasets = []
          this.dataFromServer = await getStatistics()
          for (var key in this.dataFromServer) {
            var newDataset = {}
            newDataset['name'] = key
            newDataset['data'] = []
            this.dataFromServer[key].forEach(element => {
                newDataset['data'].push({x:element.date, y:element.weight, additionalValues: 'Dupa'})
            });
            datasets.push(newDataset)
            }
          this.chartData = datasets
      },
      dataPointSelection(event, chartContext, config) {
        console.log(event)
        console.log(chartContext)
        console.log(config)
        console.log(this.$refs.chart.series[config.seriesIndex].data[config.dataPointIndex])
        this.$emit('openEditStatisticForm')
      },
  }
};
</script>