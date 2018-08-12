import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/view/Home'
import Main from '@/view/Main'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
      children: [{
        path: '/main',
        component: Main
      }]
    }
  ]
})
