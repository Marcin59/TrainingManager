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
        @openEditStatisticForm="updateEditStatisticFormActive(true)"
        @updateEditFormValues="updateEditFormValues"
      />
      <AddNewStatisticForm
        :activeForm="addNewStatisticFormActive"
        @updateActiveForm="updateAddNewStatisticFormActive"
        @updateCharts="updateCharts"
      />
      <EditStatisticForm
        ref="editForm"
        :activeForm="editStatisticFormActive"
        :selectedStatisticPk="selectedStatisticPk"
        @updateActiveForm="updateEditStatisticFormActive"
        @updateCharts="updateCharts"
      />
    </v-app>
</template>

<script>
import AreaChart from "@/components/Charts/StatisticsAreaChart.vue"
import AddNewStatisticForm from "@/components/Forms/AddNewStatisticForm.vue"
import EditStatisticForm from "@/components/Forms/EditStatisticForm.vue"

export default {
    name: "Statistics",
    data: function () {
        return {
            addNewStatisticFormActive: false,
            editStatisticFormActive: false,
            selectedStatisticPk: 'null',
        }
    },
    components: {
        AreaChart,
        AddNewStatisticForm,
        EditStatisticForm,
    },
    methods: {
        updateCharts() {
            window.location.reload()
        },
        updateAddNewStatisticFormActive(newValue) {
            this.addNewStatisticFormActive = newValue
        },
        updateEditStatisticFormActive(newValue) {
            this.editStatisticFormActive = newValue
        },
        updateEditFormValues(title, date, weight, pk) {
          this.$refs.editForm.updateFormValues(title, date, weight, pk)
        }
    },
}
</script>