import ShouYe from "@/views/conversationPage.vue";
import RegisterPage from "@/views/RegisterPage.vue";
import LoginPage from "@/views/LoginPage.vue";
import NotFound404 from "@/components/notFound404.vue";

import Vue from "vue";
import VueRouter from "vue-router";
// import { meta } from "@babel/eslint-parser";

const TOKEN_KEY = "access_token";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    redirect: "/login",
  },
  {
    path: "/login",
    component: LoginPage,
  },
  {
    path: "/register",
    component: RegisterPage,
  },
  {
    path: "/conversation",
    component: ShouYe,
    meta: { needAuth: true },
  },
  {
    path: "/conversation/:id", // 动态路由，详情页面
    component: ShouYe,
    meta: { needAuth: true },
  },
  // 404 页面
  {
    path: "/404",
    component: NotFound404,
  },
  {
    path: "*",
    redirect: "/404",
  },
];

const router = new VueRouter({
  routes,
  mode: "history",
  base: "/",
});

// 前置全局守卫
router.beforeEach((to, from, next) => {
  const isLogin = !!sessionStorage.getItem(TOKEN_KEY); // 双重取反：转换为 true 或 false

  if (!isLogin && to.meta.needAuth) {
    // 如果未登录 且目标页面不是登录页，重定向到登录页
    alert("您未登录，请先登录后再进行聊天！");
    next("/login");
  } else {
    // 放行
    next();
  }
});

export default router;
