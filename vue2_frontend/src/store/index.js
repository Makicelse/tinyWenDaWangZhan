import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    accessToken: null, // 存储用户的 access_token
  },
  mutations: {
    setAccessToken(state, token) {
      state.accessToken = token;
      localStorage.setItem('access_token', token); // 同步到 LocalStorage
    },
    clearAccessToken(state) {
      state.accessToken = null;
      localStorage.removeItem('access_token'); // 从 LocalStorage 移除
    },
  },
  actions: {
    login({ commit }, token) {
      commit('setAccessToken', token); // 调用 mutation 保存 Token
    },
    logout({ commit }) {
      commit('clearAccessToken'); // 调用 mutation 清除 Token
    },
    initializeToken({ commit }) {
      const token = localStorage.getItem('access_token'); // 检查 LocalStorage 是否有 Token
      if (token) {
        commit('setAccessToken', token); // 初始化到 Vuex
      }
    },
  },
  getters: {
    isAuthenticated: state => !!state.accessToken, // 检查是否有 Token
    getAccessToken: state => state.accessToken, // 获取 Token
  },
});
