import axios from 'axios'

const instance = axios.create({
  baseURL: '/api',
  timeout: 5000
})

// 请求拦截器：自动加上 token
instance.interceptors.request.use(config => {
  const token = sessionStorage.getItem('TOKEN_KEY')
  if (token && token !== 'null') {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export default instance
