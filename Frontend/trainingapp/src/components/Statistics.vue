<template>
    <v-app>
      <v-sheet height="64">
        <v-toolbar
          flat
        >
          <v-spacer></v-spacer>
          <v-btn
            outlined
            class="mr-4"
            color="grey darken-2"
            @click="updateAddNewStatisticFormActive(true)"
          >
            Add New Statistic
          </v-btn>
        </v-toolbar>
      </v-sheet>
      <AreaChart
        ref="areaChart"
      />
      <AddNewStatisticForm
        :activeForm="addNewStatisticFormActive"
        @updateActiveForm="updateAddNewStatisticFormActive"
        @updateCharts="updateCharts"
      />
    </v-app>
</template>

<script>
import AreaChart from "@/components/Charts/StatisticsAreaChart.vue"
import AddNewStatisticForm from "@/components/Forms/AddNewStatisticForm.vue"

export default {
    name: "Statistics",
    data: function () {
        return {
            addNewStatisticFormActive: false,
        }
    },
    components: {
        AreaChart,
        AddNewStatisticForm,
    },
    methods: {
        updateCharts() {
            window.location.reload()
        },
        updateAddNewStatisticFormActive(newValue) {
            this.addNewStatisticFormActive = newValue
        }
    },
}
</script>