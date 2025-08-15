<template>
  <!-- <div class="page-container">
    <div class="not-found-wrapper">
      <div class="not-found-img">
        <img src="../assets/svg/404.svg" alt="404图片" />
      </div>
      <el-button @click="toHome()">返回首页</el-button>
    </div>
  </div> -->
  <el-container>
    <el-main class="page-container">
      <div class="not-found-wrapper">
        <div class="not-found-img">
          <img src="../assets/svg/404.svg" alt="404图片" />
        </div>
        <p class="not-found-txt">啊哦，页面不见了！</p>
        <div class="btn">
          <el-button @click="toHome()">返回首页</el-button>
        </div>
      </div>
    </el-main>
  </el-container>
</template>

<script>
import router from "@/router";

export default {
  methods: {
    toHome() {
      router.replace("/");
    },
  },
};
</script>

<style scoped>
img {
  width: 100%;
  height: auto;
}

.page-container {
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
}

.not-found-wrapper {
  width: 400px;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.not-found-img {
  width: 100%;
  height: auto;
}

.not-found-txt {
  text-align: center;
  color: grey;
  font-size: large;
}

.btn {
  display: flex;
  justify-content: center;
  margin-top: 5%;
}
</style>
