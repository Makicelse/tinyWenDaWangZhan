<template>
  <div class="login-container">
    <div class="login-wrapper">
      <h1 class="title">登录</h1>
      <form @submit.prevent="postLogin()">
        <div class="input">
          <div class="name">
            <i class="el-icon-user"></i>
            <span>用户名：</span>
          </div>
          <el-input v-model="username" placeholder="请输入用户名"> </el-input>
        </div>

        <div class="input">
          <div class="name">
            <i class="el-icon-lock"></i>
            <span>密码：</span>
          </div>
          <el-input
            v-model="password"
            placeholder="请输入密码"
            show-password
          ></el-input>
        </div>

        <div class="button">
          <el-button @click="postLogin()" type="primary">登录</el-button>
        </div>
      </form>
      <p>
        还没有账号？点此
        <el-link @click="$router.replace('/register')" type="primary"
          >注册</el-link
        >
      </p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    postLogin() {
      // mock接口：http://127.0.0.1:4523/m2/4755954-4409227-default/243992732
      // 后端接口：http://127.0.0.1:5000/user_login
      this.$axios
        .post("http://127.0.0.1:5000/user_login", {
          username: this.username,
          password: this.password,
        })
        .then((response) => {
          // console.log("登录接口返回数据为：", response.data);
          // console.log("access_token为：", response.data["access_token"]);

          if (response.data.status === true) {
            alert("登录成功！");
            // 保存用户登录状态
            this.$store.dispatch("login", response.data["access_token"]);
            // 跳转至对话页面
            this.$router.push("/conversation");
          } else {
            alert("似乎出错了……");
          }
        })
        .catch((error) => {
          console.error("登录出错了！", error);
          alert("似乎出错了……");
        });
    },
    
  },
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

.title {
  display: flex;
  justify-content: center;
}

.login-wrapper {
  backdrop-filter: blur(4px);
  box-shadow: inset 1px 1px 6px rgba(255, 255, 255, 0.3),
    2px 2px 15px rgba(0, 0, 0, 0.3);
  padding: 20px 30px;
  border-radius: 1rem;
}

.login-wrapper,
.input {
  display: flex;
  flex-direction: column;
}

.input {
  gap: 7px;
  margin-bottom: 12px;
}

.input .name {
  display: flex;
  gap: 3px;
  align-items: baseline;
}

.login-wrapper .button {
  display: flex;
  justify-content: center;
  margin-top: 25px;
}

p {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 2px;

  color: #696969;
  font-size: 14px;
}
</style>
