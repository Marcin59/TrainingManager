<template>
    <v-app>
        <AreaChart/>
        <h1>{{dataFromServer}}</h1>
    </v-app>
</template>

<script>
import AreaChart from "@/components/Charts/StatisticsAreaChart.vue";
import {getStatistics} from "@/services/statisticServise.js"

export default {
    name: "Statistics",
    data: function () {
        return {
            dataFromServer: null,
        }
    },
    components: {
        AreaChart,
  },
  mounted() {
    this.updateData()
  },
  methods: {
      async updateData() {
          this.dataFromServer = await getStatistics()
      },
  }
}
</script>