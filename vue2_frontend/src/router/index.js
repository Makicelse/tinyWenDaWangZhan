import ShouYe from '@/views/conversationPage.vue'
import RegisterPage from '@/views/RegisterPage.vue'
import LoginPage from '@/views/LoginPage.vue'

import Vue from 'vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter)

const routes = [
  {
    path: '/', 
    redirect: '/login'
  }, 
  {
    path: '/login', 
    component: LoginPage, 
    
  }, 
  {
    path: '/register', 
    component: RegisterPage
  }, 
  {
    path: '/conversation', 
    component: ShouYe,
  }, 
  {
    path: '/conversation/:id', // 动态路由，详情页面
    component: ShouYe,
  }, 
]

const router = new VueRouter({
  routes,
  mode: 'history',
  base: '/'
})

export default router