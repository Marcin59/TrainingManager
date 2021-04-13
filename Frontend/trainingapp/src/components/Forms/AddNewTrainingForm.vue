<template>
  <div class="text-center">
    <v-dialog
      v-model="active"
      width="80%"
    >
      <v-card>
        <v-card-title class="headline grey lighten-2">
          <center style="margin: auto">
            New training
          </center>
        </v-card-title>

      <v-container>
        <v-container
          v-for="(exercise, index) in newTraining"
          v-bind:key="exercise.id"
        >
        <v-row>
          <v-col
            md="3"
          >
            <h1 style="margin:0">{{exercise.name}}</h1>
          </v-col>
          <v-col>
            <v-btn
              outlined
              class="mr-4"
              color="grey darken-2"
              @click="addNewSet(exercise.sets)"
            >
              Add new set
            </v-btn>
            <v-btn
                  @click="deleteExerciseByIndex(newTraining ,index)"
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
          <v-row>
              <v-col
                md='5'
              >
                <th>
                  reps
                </th>
              </v-col>
              <v-col
                md='5'
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
              >
                <v-text-field
                  v-model="set.reps"
                ></v-text-field>
              </v-col>
              <v-col
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
            md="4"
          >
            <v-date-picker
              v-model="date"
            ></v-date-picker>
          </v-col>
          <v-col
            md="4"
          >
            <h1>Start</h1>
            <v-time-picker
              v-model="startTime"
            ></v-time-picker>
          </v-col>
          <v-col
            md="4"
          >
            <h1>End</h1>
            <v-time-picker
              v-model="endTime"
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
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
    export default {
        data: () => ({
          date: null,
          startTime: null,
          endTime: null,
          newTraining: [],
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
        methods: {
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
              if(this.newTraining.length != 0){
                newId  = this.newTraining[this.newTraining.length-1].id+1
              }
              else{
                newId = 0
              }
              this.newTraining.push({
                id: newId,
                name: 'Push',
                sets: [],
            })
            },
            deleteExerciseByIndex(sets, index) {
              sets.splice(index, 1)
            },
        }
    }
</script>

