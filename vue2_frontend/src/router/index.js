import ShouYe from "@/views/conversationPage.vue";
import RegisterPage from "@/views/RegisterPage.vue";
import LoginPage from "@/views/LoginPage.vue";
// import NotFound404 from "@/components/notFound404.vue";

import Vue from "vue";
import VueRouter from "vue-router";

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
  },
  {
    path: "/conversation/:id", // 动态路由，详情页面
    component: ShouYe,
  },
  // 404 页面
  // {
  //   path: "*",
  //   component: NotFound404,
  // },
];

const router = new VueRouter({
  routes,
  mode: "history",
  base: "/",
});

// 前置全局守卫
router.beforeEach((to, from, next) => {
  const isLogin = !!sessionStorage.getItem(TOKEN_KEY); // 双重取反：转换为 true 或 false
  // 注册放行
  if (!isLogin && to.path === "/register") {
    next();
  } else if (!isLogin && to.path !== "/login") {
    // 如果未登录 且目标页面不是登录页，重定向到登录页
    next("/login");
  } else {
    // 已登录，或正访问登录页，放行
    next();
  }
});

export default router;
