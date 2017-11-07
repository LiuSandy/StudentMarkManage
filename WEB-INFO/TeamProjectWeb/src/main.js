import Vue from 'vue'
import App from './App'
import router from './router'
import iView from 'iview'
import axios from 'axios'
import echarts from 'echarts'
import 'iview/dist/styles/iview.css'

Vue.use(iView)
Vue.config.productionTip = false
Vue.config.devtools = true
Vue.prototype.$http = axios.create({
  baseURL: 'http://localhost:5000/api/'
})
Vue.prototype.$echarts = echarts

/* eslint-disable no-new */

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
