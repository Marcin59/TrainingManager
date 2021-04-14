<template>
  <div class="text-center">
    <v-dialog
      v-model="active"
      width="80%"
    >
      <v-card
        min-height=850
      >
        <v-card-title class="headline grey lighten-2">
          <center style="margin: auto">
            New training
          </center>
        </v-card-title>

      <v-container>
        <v-text-field
          v-model="trainingTitle"
          label="Title"
        ></v-text-field>
        <v-container
          v-for="(exercise, index) in exercises"
          v-bind:key="exercise.id"
        >
        <v-row>
          <v-col
            md="3"
            style="padding:0; padding-right:10px"
          >
            <v-select
              :items="exercisesTypes"
              v-model="exercise.title"
              solo
            ></v-select>
          </v-col>
          <v-col
            style="padding:0"
          >
            <v-btn
              outlined
              class="mr-4"
              color="grey darken-2"
              @click="addNewSet(exercise.sets)"
            >
              Add new set
            </v-btn>
            <v-btn
                  @click="deleteExerciseByIndex(exercises ,index)"
                >
                  <v-icon 
                    color='red'
                    medium
                  >
                    mdi-delete
                  </v-icon>
                </v-btn>
          </v-col>
        </v-row>
        <v-row
          v-if="exercise.sets.length != 0"
        >
            <v-col
              md='5'
              style="padding:0"
            >
              <th>
                reps
              </th>
            </v-col>
            <v-col
              md='5'
              style="padding:0"
            >
              <th>
                weight
              </th>
            </v-col>
          </v-row>

          <v-container
            v-for="(set, index) in exercise.sets"
            v-bind:key="set.id"
          >
            <v-row>
              <v-col
                md='5'
                style="padding:0; padding-right:10px"
              >
                <v-text-field
                  v-model="set.reps"
                ></v-text-field>
              </v-col>
              <v-col
                style="padding:0"
                md='5'
              >
                <v-text-field
                  suffix="kg"
                  v-model="set.weight"
                ></v-text-field>
              </v-col>
              <v-col
                md='2'
              >
                <v-btn
                  @click="deleteSetByIndex(exercise.sets ,index)"
                >
                  <v-icon 
                    color='red'
                    medium
                  >
                    mdi-delete
                  </v-icon>
                </v-btn>
              </v-col>
            </v-row>
          </v-container>
        </v-container>
        <v-container style="height: 100px">
          <v-btn
            outlined
            class="mr-4"
            color="grey darken-2"
            @click="addNewExercise"
          >
            Add new exercise
          </v-btn>
        </v-container>
        <v-row>
          <v-col
            md="6"
            align='center'
          >
            <v-date-picker
              v-model="startDate"
            ></v-date-picker>
          </v-col>
          <v-col
            md="6"
            align='center'
          >
            <v-time-picker
              v-model="startTime"
            ></v-time-picker>
          </v-col>
        </v-row>
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
  </div>
</template>

<script>

import {getExerciseTitles, postNewTraining} from "@/services/defaultService.js"

    export default {
        data: () => ({
          startDate: null,
          startTime: null,
          exercises: [],
          exercisesTypes: [],
          trainingTitle: null,
        }),
        props: {
            activeForm: Boolean,
        },
        computed: {
            active: {
                get () { return this.activeForm },
                set (value) { this.$emit('updateActiveForm', value) },    
            }
        },
        mounted() {
          this.resetNewTrainingTime()
          this.updateExerciseTitles()
        },
        methods: {
            async updateExerciseTitles() {
              var dataFromServer = await getExerciseTitles()
              this.exercisesTypes = []
              dataFromServer.forEach(element => {
                this.exercisesTypes.push(element.fields.title)
              });
            },
            async acceptForm() {
              var data = {
                title : this.trainingTitle,
                exercises : this.exercises,
                start: this.startDate+' '+this.startTime
              }
              await postNewTraining(data)
              this.resetForm()
              this.closeForm()
              this.$emit('updateEvents')
            },
            resetForm() {
              this.trainingTitle = null
              this.resetNewTrainingTime()
              this.exercises = []
            },
            resetNewTrainingTime() {
              var actualDate = new Date().toJSON().slice(0,10)
              var actualTime = new Date().toJSON().slice(11,16)
              this.startDate = actualDate
              this.startTime = actualTime 
            },
            closeForm() {
                this.$emit('updateActiveForm', false)
            },
            addNewSet(sets) {
              var newId
              if(sets.length != 0){
                newId  = sets[sets.length-1].id+1
              }
              else{
                newId = 0
              }
              sets.push({
                id: newId,
                weight: 0,
                reps: 0,
              })
            },
            deleteSetByIndex(sets, index) {
              sets.splice(index, 1)
            },
            addNewExercise() {
              var newId
              if(this.exercises.length != 0){
                newId  = this.exercises[this.exercises.length-1].id+1
              }
              else{
                newId = 0
              }
              this.exercises.push({
                id: newId,
                title: null,
                sets: [],
            })
            },
            deleteExerciseByIndex(sets, index) {
              sets.splice(index, 1)
            },
        }
    }
</script>

