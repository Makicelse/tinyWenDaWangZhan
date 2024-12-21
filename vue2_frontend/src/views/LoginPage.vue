<template>
  <div class="login-container">
    <div class="login">
      <h1>登录</h1>
      <form @submit.prevent="postLogin()">
        <label>
          用户名：
          <input v-model="username" type="text" required />
        </label>
        <label>
          密码：
          <input v-model="password" type="password" required />
        </label>
        <button type="submit">登录</button>
      </form>
      <p>还没有账号？<router-link to="/register">注册</router-link></p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    postLogin () {
      // mock接口：http://127.0.0.1:4523/m2/4755954-4409227-default/243992732
      // 后端接口：http://127.0.0.1:5000/user_login
      this.$axios.post('http://127.0.0.1:5000/user_login', {
        'username': this.username, 
        'password': this.password
      }).then(response => {
        // console.log("登录接口返回数据为：", response.data);
        // console.log("access_token为：", response.data["access_token"]);
        
        if (response.data.status === true) {
          alert('登录成功！');
          // 保存用户登录状态
          this.$store.dispatch('login', response.data["access_token"])
          // 跳转至对话页面
          this.$router.push('/conversation');
        } else {
          alert('登录出错了……');
        }
      }).catch(error => {
        console.error("登录出错了！", error);
        
      })
    }, 
  }
};
</script>
  
<style scoped>
.login-container {
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

p {
  display: flex;
  justify-content: center;
  align-items: center;
}

</style>
