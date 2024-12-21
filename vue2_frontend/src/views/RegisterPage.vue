<template>
  <div class="reg-container">
    <div class="register">
      <h1>注册</h1>
      <form @submit.prevent="postRegister()">
        <label>
          用户名：
          <input v-model="username" type="text" required />
        </label>
        <label>
          密码：
          <input v-model="password" type="password" required />
        </label>
        <button type="submit">注册</button>
      </form>
      <p>已有账号？<router-link to="/login">登录</router-link></p>
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
      postRegister () {
        // mock接口：http://127.0.0.1:4523/m2/4755954-4409227-default/243983104?apifoxApiId=243983104
        // 后端接口：http://127.0.0.1:5000/user_register
        this.$axios.post('http://127.0.0.1:5000/user_register', {
            'username': this.username, 
            'password': this.password
        }).then(response => {
            alert(response.data.message);
            this.$router.push('/login');
        }).catch(error => {
            console.error('接口请求失败', error);
            
        })
      }
    },
  };
</script>

<style scoped>
.reg-container {
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
