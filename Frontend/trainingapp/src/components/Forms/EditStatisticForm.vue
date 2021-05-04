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
          <v-row>
            <v-col>
              <v-btn
                color="primary"
                text
                @click="closeForm"
              >
                Cancel
              </v-btn>
            </v-col>

            <v-col>
              <v-btn
                color="primary"
                text
                @click="deleteForm"
              >
                Delete
              </v-btn>
            </v-col>

            <v-col>
              <v-btn
                color="primary"
                text
                @click="updateForm"
              >
                Accept
              </v-btn>
            </v-col>
          </v-row>
        </v-card-actions>
      </v-card>
    </v-dialog>
    </v-container>
</template>

<script>
import {getStatisticTitles, postNewStatistic, deleteStatisticByPk} from "@/services/statisticServise.js"

export default {
    data: () => ({
        statisticWeight: null,
        statisticDate: null,
        statisticTitle: null,
        statisticPk: null,
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
        async updateForm() {
            var dataToDelete = {
              pk: this.statisticPk
            }
            await deleteStatisticByPk(dataToDelete)
            var dataToPost = {
                title: this.statisticTitle,
                date: this.statisticDate,
                weight: this.statisticWeight,
              }
            await postNewStatistic(dataToPost)
            this.closeForm()
            this.$emit('updateCharts')
        },
        async deleteForm() {
          var data = {
            pk: this.statisticPk,
          }
          await deleteStatisticByPk(data)
          this.closeForm()
          this.$emit('updateCharts')
        },
        updateFormValues(title, date, weight, pk) {
            this.statisticWeight = weight
            this.statisticDate = date.slice(0, 10)
            this.statisticTitle = title
            this.statisticPk = pk
        },
        closeForm() {
            this.$emit('updateActiveForm', false)
        },
    }
}
</script>