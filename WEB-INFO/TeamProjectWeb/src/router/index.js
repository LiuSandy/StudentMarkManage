import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const Main = resolve => require(['@/components/Main'], resolve)
const Login = resolve => require(['@/components/login/Login'], resolve)
const Hello = resolve => require(['@/components/Hello'], resolve)

// error-router
const NotFind = resolve => require(['@/components/error/404'], resolve)
const NotBad = resolve => require(['@/components/error/500'], resolve)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'main',
      component: Main,
      children: [
        {
          path: 'hello',
          component: Hello
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
