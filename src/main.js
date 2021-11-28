import Vue from 'vue';
import App from '@/app';
import router from './router';

Vue.config.productionTip = false;

new Vue({
  router, 
  render: r => r(App)
}).$mount('#app');
