<template>
  <div class="text-center">
    <v-dialog
      v-model="active"
      width="80%"
    >
      <v-card
      >
        <v-card-title class="headline grey lighten-2">
          <center style="margin: auto">
            New training
          </center>
        </v-card-title>

      <v-container>
        <v-row>
          <v-col
            md="12"
          >
            <v-text-field
              v-model="title"
              label="Title"
              required
            ></v-text-field>
          </v-col>
        </v-row>
        <v-container
          v-for="exercise in exercises"
          v-bind:key="exercise.name"
          style="margin: auto"
        >
          <h1 >{{exercise.name}}</h1>
          <v-row>
              <v-col>
                <th>
                  reps
                </th>
              </v-col>
              <v-col>
                <th>
                  weight(kg)
                </th>
              </v-col>
            </v-row>

          <v-container
            v-for="set in exercise.sets"
            v-bind:key="set.reps"
          >
            <v-row>
              <v-col>
                <v-text-field
                  v-model="set.reps"
                ></v-text-field>
              </v-col>
              <v-col>
                <v-text-field
                  v-model="set.weight"
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
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

        <v-divider></v-divider>

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
          title: '',
          date: null,
          startTime: null,
          endTime: null,
          exercises: [{
            name: 'Deadlift',
            sets: [
              {
                weight: 21,
                reps: 100,
              },
              {
                weight: 100,
                reps: 12,
              }
            ]
            },
            {
            name: 'Bench press',
            sets: [
              {
                weight: 21,
                reps: 100,
              },
              {
                weight: 100,
                reps: 12,
              }
            ]
            },],
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
            }
        }
    }
</script>
