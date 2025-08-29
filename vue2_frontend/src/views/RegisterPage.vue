<template>
  <div class="reg-container">
    <div class="reg-wrapper">
      <h1 class="title">注册</h1>
      <form @submit.prevent="postRegister()">
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
          <el-button @click="postRegister()" type="primary">注册</el-button>
        </div>
      </form>
      <p>
        已有账号？点此
        <el-link @click="$router.replace('/login')" type="primary"
          >登录</el-link
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
    postRegister() {
      // mock接口：http://127.0.0.1:4523/m2/4755954-4409227-default/243983104?apifoxApiId=243983104
      // 后端接口：http://127.0.0.1:5000/user_register
      this.$axios
        .post("http://127.0.0.1:5000/user_register", {
          username: this.username,
          password: this.password,
        })
        .then((response) => {
          alert(response.data.message);
          this.$router.push("/login");
        })
        .catch((error) => {
          console.error("接口请求失败", error);
        });
    },
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

.title {
  display: flex;
  justify-content: center;
}

.reg-wrapper {
  backdrop-filter: blur(4px);
  box-shadow: inset 1px 1px 6px rgba(255, 255, 255, 0.3),
    2px 2px 15px rgba(0, 0, 0, 0.3);
  padding: 20px 30px;
  border-radius: 1rem;
}

.reg-wrapper,
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

.reg-wrapper .button {
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
