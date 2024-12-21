import Vue from 'vue'
import App from './App.vue'

import axios from 'axios'
import router from './router/index'
import store from './store'

import '@/assets/css/normalize.css'
import '@/assets/css/skeleton.css'

// 将 axios 挂载到 Vue 原型上，这样在任何组件中都可以通过 this.$axios 访问
Vue.prototype.$axios = axios;

new Vue({
  render: h => h(App),
  router, 
  store, // 注册 Vuex Store
}).$mount('#app')
