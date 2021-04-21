<template>
    <v-app>
        <AreaChart/>
        <h1>{{dataFromServer}}</h1>
    </v-app>
</template>

<script>
import AreaChart from "@/components/Charts/StatisticsAreaChart.vue";

export default {
    name: "Statistics",
    data: function () {
        return {
            dataFromServer: null,
            datasetsAreaChart: [],
        }
    },
    components: {
        AreaChart,
  },
}
</script>