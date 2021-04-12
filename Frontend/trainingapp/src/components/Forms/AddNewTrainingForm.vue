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
          exercises: Array,
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
