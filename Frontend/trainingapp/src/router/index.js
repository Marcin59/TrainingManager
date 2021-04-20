import Vue from 'vue';
import Router from 'vue-router';
import Calendar from '@/components/Calendar.vue';
import Statistics from '@/components/Statistics.vue';

Vue.use(Router);

const routes = [
  {
    path: '',
    name: 'Calendar',
    component: Calendar,
  },
  {
    path: '/Statistics',
    name: 'Statistics',
    component: Statistics,
  },
];

export default new Router({
  routes,
  mode: 'history',
});