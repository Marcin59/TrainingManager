<template>
  <v-container>
    <v-dialog
      v-model="active"
      width="40%"
    >
      <v-card>
        <v-card-title class="headline grey lighten-2">
          <center style="margin: auto">
            New Statistic
          </center>
        </v-card-title>

      <v-container>
        <v-select
          :items="statisticTypes"
          v-model="statisticTitle"
          solo
        ></v-select>
        <v-text-field
            v-model="statisticWeight"
        ></v-text-field>
        <div
          class="justify-center"
          style="text-align: center;"
        >
          <v-date-picker
            v-model="statisticDate"
          ></v-date-picker>
        </div>
      </v-container>

        <v-card-actions>
          <v-btn
            color="primary"
            text
            @click="closeForm"
          >
            Cancel
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="acceptForm"
          >
            Accept
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    </v-container>
</template>

<script>
import {getStatisticTitles, postNewStatistic} from "@/services/statisticServise.js"

export default {
    data: () => ({
        statisticWeight: null,
        statisticDate: null,
        statisticTitle: null,
        statisticTypes: [],
    }),
    props: {
            activeForm: Boolean,
    },
    mounted() {
          this.updateStatisticTitles()
        },
    computed: {
        active: {
            get () { return this.activeForm },
            set (value) { this.$emit('updateActiveForm', value) },    
        }
    },
    methods: {
        async updateStatisticTitles() {
              var dataFromServer = await getStatisticTitles()
              this.statisticTypes = []
              dataFromServer.forEach(element => {
                this.statisticTypes.push(element.fields.title)
              });
        },
        async acceptForm() {
            var data = {
                title: this.statisticTitle,
                date: this.statisticDate,
                weight: this.statisticWeight,
            }
            await postNewStatistic(data)
            this.closeForm()
            this.resetForm()
            this.$emit('updateCharts')
        },
        resetForm() {
            this.statisticWeight= []
            this.statisticDate = null
            this.statisticTitle = null
        },
        closeForm() {
            this.$emit('updateActiveForm', false)
        }
    }
}
</script>