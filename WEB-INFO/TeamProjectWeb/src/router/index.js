import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const Login = resolve => require(['@/components/login/Login'], resolve)

const Main = resolve => require(['@/components/Main'], resolve)
const Dashboard = resolve => require(['@/components/dashboard/Dashboard'], resolve)

const AllRank = resolve => require(['@/components/rank/Allrank'], resolve)

// error-router
const NotFind = resolve => require(['@/components/error/404'], resolve)
const NotBad = resolve => require(['@/components/error/500'], resolve)

export default new Router({
  routes: [
    {
      path: '/',
      component: Main,
      children: [
        {
          path: '',
          name: 'main',
          component: Dashboard
        },
        {
          path: '/allRank',
          name: 'allRank',
          component: AllRank
        }
      ]
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '*',
      name: '404',
      component: NotFind
    },
    {
      path: '*',
      name: '500',
      component: NotBad
    }
  ]
})
