<template>
  <v-app>
    
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center" style="width:100%">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          :src="require('./assets/logo.png')"
          transition="scale-transition"
          width="40"
        />

        <h1
          style='font-family: "Ubuntu"'
        >
          Training manager
        </h1>
        <v-spacer></v-spacer>
        <router-link
          to="Statistics"
          custom
          v-slot="{ navigate, isActive}"
        >
          <v-btn
            right
            elevation="2"
            :active="isActive"
            @click="navigate"
          >
            Statistics
          </v-btn>
        </router-link>
        <div style="width:3%"></div>
        <router-link
          to="/"
          custom
          v-slot="{ navigate, isActive}"
        >
          <v-btn
            right
            elevation="2"
            :active="isActive"
            @click="navigate"
          >
            Calendar
          </v-btn>
        </router-link>
      </div>

    </v-app-bar>

    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',

  components: {
  },

  data: () => ({
    href: null,
    isActive: null,
    navigate: null,
  }),
};
</script>
