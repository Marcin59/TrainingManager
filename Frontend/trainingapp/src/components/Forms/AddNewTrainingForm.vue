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

        <v-card-text>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-btn
            color="primary"
            text
            @click="closeForm"
          >
            Cancel
          </v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
    export default {
        data: () => ({

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
