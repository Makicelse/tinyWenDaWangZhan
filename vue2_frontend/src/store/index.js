import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

// export default new Vuex.Store({
//   state: {
//     accessToken: null, // 存储用户的 access_token
//   },
//   mutations: {
//     setAccessToken(state, token) {
//       state.accessToken = token;
//       localStorage.setItem('access_token', token); // 同步到 LocalStorage
//     },
//     clearAccessToken(state) {
//       state.accessToken = null;
//       localStorage.removeItem('access_token'); // 从 LocalStorage 移除
//     },
//   },
//   actions: {
//     login({ commit }, token) {
//       commit('setAccessToken', token); // 调用 mutation 保存 Token
//     },
//     logout({ commit }) {
//       commit('clearAccessToken'); // 调用 mutation 清除 Token
//     },
//     initializeToken({ commit }) {
//       const token = localStorage.getItem('access_token'); // 检查 LocalStorage 是否有 Token
//       if (token) {
//         commit('setAccessToken', token); // 初始化到 Vuex
//       }
//     },
//   },
//   getters: {
//     isAuthenticated: state => !!state.accessToken, // 检查是否有 Token
//     getAccessToken: state => state.accessToken, // 获取 Token
//   },
// });

// 键名统一放这里，防止写错
const TOKEN_KEY = 'access_token'
const CHAT_ID_KEY = 'cur_chat_id'
const MESSAGES_KEY = 'chat_messages'

export default new Vuex.Store({
  state: {
    accessToken: sessionStorage.getItem(TOKEN_KEY) || null,
    cur_chatId: sessionStorage.getItem(CHAT_ID_KEY) || null,
    messages: JSON.parse(sessionStorage.getItem(MESSAGES_KEY)) || []
  },

  mutations: {
    // === accessToken ===
    setAccessToken(state, token) {
      state.accessToken = token
      sessionStorage.setItem(TOKEN_KEY, token)
    },
    clearAccessToken(state) {
      state.accessToken = null
      sessionStorage.removeItem(TOKEN_KEY)
    },

    // === cur_chat_id ===
    setChatId(state, chatId) {
      state.cur_chatId = chatId
      sessionStorage.setItem(CHAT_ID_KEY, chatId)
    },
    clearChatId(state) {
      state.cur_chatId = null
      sessionStorage.removeItem(CHAT_ID_KEY)
    },

    // === messages ===
    setMessages(state, messages) {
      state.messages = messages
      sessionStorage.setItem(MESSAGES_KEY, JSON.stringify(messages))
    },
    clearMessages(state) {
      state.messages = []
      sessionStorage.removeItem(MESSAGES_KEY)
    }
  },

  actions: {
    // 登录 / 退出
    login({ commit }, token) {
      commit('setAccessToken', token)
    },
    logout({ commit }) {
      commit('clearAccessToken')
      commit('clearChatId')
      commit('clearMessages')
    },

    // 页面刷新时初始化
    initializeState({ commit }) {
      const token = sessionStorage.getItem(TOKEN_KEY)
      const chatId = sessionStorage.getItem(CHAT_ID_KEY)
      const messages = sessionStorage.getItem(MESSAGES_KEY)

      if (token) commit('setAccessToken', token)
      if (chatId) commit('setChatId', chatId)
      if (messages) commit('setMessages', JSON.parse(messages))
    }
  },

  getters: {
    isAuthenticated: state => !!state.accessToken,
    getAccessToken: state => state.accessToken,
    getChatId: state => state.cur_chatId,
    getMessages: state => state.messages
  }
})
