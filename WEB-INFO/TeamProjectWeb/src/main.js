import Vue from 'vue'
import App from './App'
import router from './router'
import iView from 'iview'
import axios from 'axios'
import echarts from 'echarts'
import lodash from 'lodash'
import Cookies from 'js-cookie'
import 'iview/dist/styles/iview.css'

Vue.use(iView)
Vue.config.productionTip = false
Vue.config.devtools = true
Vue.prototype.$_ = lodash

Vue.prototype.$http = axios.create({
  baseURL: 'http://localhost:5000/api/'
})
Vue.prototype.$echarts = echarts

router.beforeEach((to, from, next) => {
  iView.LoadingBar.start()
  console.log(to.name)
  if (!Cookies.get('user') && to.name !== 'login') {  // 判断是否登录
    console.log('没有登陆')
    next({
      path: '/login'
    })
  }
  next()
  iView.LoadingBar.finish()
})

/* eslint-disable no-new */

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
