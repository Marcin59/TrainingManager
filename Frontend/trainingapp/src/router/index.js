import Vue from 'vue';
import Router from 'vue-router';
import Calendar from '@/components/Calendar.vue';

Vue.use(Router);

const routes = [
  {
    path: '',
    name: 'Calendar',
    component: Calendar,
  },
];

export default new Router({
  routes,
  mode: 'history',
});