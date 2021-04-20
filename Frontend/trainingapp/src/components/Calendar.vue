<template>
  <v-row class="fill-height">
    <v-col>
      <v-sheet height="64">
        <v-toolbar
          flat
        >
          <v-btn
            outlined
            class="mr-4"
            color="grey darken-2"
            @click="setToday"
          >
            Today
          </v-btn>
          <v-btn
            fab
            text
            small
            color="grey darken-2"
            @click="prev"
          >
            <v-icon small>
              mdi-chevron-left
            </v-icon>
          </v-btn>
          <v-btn
            fab
            text
            small
            color="grey darken-2"
            @click="next"
          >
            <v-icon small>
              mdi-chevron-right
            </v-icon>
          </v-btn>
          <v-toolbar-title v-if="$refs.calendar">
            {{ $refs.calendar.title }}
          </v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn
            outlined
            class="mr-4"
            color="grey darken-2"
            @click="updateAddNewTrainingFormActive(true)"
          >
            Start New Training
          </v-btn>
          <v-menu
            bottom
            right
          >
          
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                outlined
                color="grey darken-2"
                v-bind="attrs"
                v-on="on"
              >
                <span>{{ typeToLabel[type] }}</span>
                <v-icon right>
                  mdi-menu-down
                </v-icon>
              </v-btn>
            </template>
            <v-list>
              <v-list-item @click="type = 'day'">
                <v-list-item-title>Day</v-list-item-title>
              </v-list-item>
              <v-list-item @click="type = 'week'">
                <v-list-item-title>Week</v-list-item-title>
              </v-list-item>
              <v-list-item @click="type = 'month'">
                <v-list-item-title>Month</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
        </v-toolbar>
      </v-sheet>
      <v-sheet height="800">
        <v-calendar
          ref="calendar"
          v-model="focus"
          color="primary"
          :events="events"
          :event-color="getEventColor"
          :type="type"
          @click:event="showEvent"
          @click:more="viewDay"
          @click:date="viewDay"
          @change="updateRange"
        ></v-calendar>
        <v-menu
          v-model="selectedOpen"
          :close-on-content-click="false"
          :activator="selectedElement"
          offset-x
        >
          <v-card
            color="grey lighten-4"
            min-width="350px"
            flat
          >
            <v-toolbar
              :color="selectedEvent.color"
              dark
            >
              <v-btn 
                icon
                @click="openUpdateTrainingForm"
              >
                <v-icon>mdi-pencil</v-icon>
              </v-btn>
              <v-toolbar-title v-html="selectedEvent.name"></v-toolbar-title>
              <v-spacer></v-spacer>
              <v-btn icon>
                <v-icon>mdi-heart</v-icon>
              </v-btn>
              <v-btn icon>
                <v-icon>mdi-dots-vertical</v-icon>
              </v-btn>
            </v-toolbar>
            <v-card-text>
              <span v-html="selectedEvent.details"></span>
            </v-card-text>
            <v-card-actions>
              <v-btn
                text
                color="secondary"
                @click="selectedOpen = false"
              >
                Cancel
              </v-btn>
              <v-spacer></v-spacer>
              <v-btn
                text
                color="secondary"
                @click="deleteSelectedEvent"
              >
                Delete
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-menu>
      </v-sheet>
      <AddNewTrainingForm 
        :activeForm="addNewTrainingFormActive" 
        @updateActiveForm="updateAddNewTrainingFormActive"
        @updateEvents="updateEvents"
      />
      <EditTrainingForm 
        ref="updateTrainingForm"
        :activeForm="updateTrainingFormActive" 
        :selectedEvent="selectedEvent"
        @updateActiveForm="updateUpdateTrainingFormActive"
        @updateEvents="updateEvents"
      />
    </v-col>
  </v-row>
</template>

<script>
import {getTrainingsByDate, deleteTrainingByPk} from "@/services/trainingServise.js"
import AddNewTrainingForm from "@/components/Forms/AddNewTrainingForm.vue"
import EditTrainingForm from "@/components/Forms/EditTrainingForm.vue"

  export default {
    data: () => ({
      focus: '',
      type: 'month',
      typeToLabel: {
        month: 'Month',
        week: 'Week',
        day: 'Day',
      },
      addNewTrainingFormActive: false,
      updateTrainingFormActive: false,
      selectedEvent: {},
      selectedElement: null,
      selectedOpen: false,
      events: [],
      calendarStart: null,
      calendarEnd: null,
    }),
    components: {
        AddNewTrainingForm,
        EditTrainingForm,
    },
    mounted () {
      this.$refs.calendar.checkChange()
    },
    methods: {
      async deleteSelectedEvent() {
        var data = {
          pk: this.selectedEvent.pk
        }
        await deleteTrainingByPk(data)
        this.updateEvents()
        this.selectedOpen = false
      },
      openUpdateTrainingForm() {
        this.$refs.updateTrainingForm.updateEvent()
        this.updateUpdateTrainingFormActive(true)
      },
      updateAddNewTrainingFormActive(newValue) {
        this.addNewTrainingFormActive = newValue
      },
      updateUpdateTrainingFormActive(newValue) {
        this.updateTrainingFormActive = newValue
      },
      viewDay ({ date }) {
        this.focus = date
        this.type = 'day'
      },
      getEventColor (event) {
        return event.color
      },
      setToday () {
        this.focus = ''
      },
      prev () {
        this.$refs.calendar.prev()
      },
      next () {
        this.$refs.calendar.next()
      },
      showEvent ({ nativeEvent, event }) {
        const open = () => {
          this.selectedEvent = event
          this.selectedElement = nativeEvent.target
          setTimeout(() => {
            this.selectedOpen = true
          }, 10)
        }

        if (this.selectedOpen) {
          this.selectedOpen = false
          setTimeout(open, 10)
        } else {
          open()
        }

        nativeEvent.stopPropagation()
      },
      updateEvents() {
        this.updateRange()
      },
      async updateRange (data) {
        if(typeof data !== 'undefined'){
          var start = data.start
          var end = data.end
          this.calendarStart = start.date
          this.calendarEnd = end.date
        }
        this.events = []
        var dataFromServer = await getTrainingsByDate(this.calendarStart, 
                                                        this.calendarEnd)
        const events = []
        dataFromServer.forEach(element => {
            events.push({
                name: element.fields.title,
                start: element.fields.start.slice(0, 10) + ' ' + element.fields.start.slice(11, 19),
                end: element.fields.end.slice(0, 10) + ' ' + element.fields.end.slice(11, 19),
                color: 'blue',
                details: 12321,
                pk: element.pk,
          })
        });
        this.events = events
      },
    },
  }
</script>