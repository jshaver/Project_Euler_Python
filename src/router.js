import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

const parseId = p => ({ id: parseInt(p.params.id) });

export default new Router({
  mode: 'history', 
  base: process.env.BASE_URL, 
  routes: [
    {
      path: '/', 
      redirect: '/problems'
    }, 
    {
      name: 'problems',
      path: '/problems', 
      component: () => 
        import('./views/problems.vue')
    }, 
    {
      name: 'problem-detail', 
      path: '/problem/:id',
      props: parseId, 
      component: () => 
        import('./views/problem-detail.vue')
    }, 
    {
      name: 'about', 
      path: '/about', 
      component: () => 
        import('./views/about.vue')
    }
  ]
});

