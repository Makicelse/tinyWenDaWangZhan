<template>
  <div>
    <h4>对话历史列表</h4>
    <ul>
      <li v-for="item in historyChats" :key="item.chatId" @click="sendId(item.chatId)">
        <router-link :to="`/conversation/${item.chatId}`">
          {{ item.title }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
    data () {
      return {
        historyChats: []
      }
    }, 
    created () {
      console.log("creating histoy list data...");
      this.getHistoryChats();
    }, 
    methods: {
        getHistoryChats () {
          // mock接口：http://127.0.0.1:4523/m2/4755954-4409227-default/241860071?apifoxApiId=241860071
          // flask后端接口：http://127.0.0.1:5000/load_conversationTitle
          const getURL = "http://127.0.0.1:5000/load_conversationTitle"
          // console.log(this.$store.state.accessToken);
          
          this.$axios.get(getURL, {
            headers: {
              Authorization: `Bearer ${ this.$store.state.accessToken }` // 添加特定的 Header
            }
          })
            .then(response => {
                // 请求成功，处理返回的数据
                console.log('接口返回数据:', response.data);

                // 如果需要渲染数据，可以将其存入组件的 data 中
                this.historyChats = response.data;
            })
            .catch(error => {
                // 请求失败，处理错误
                console.error('请求历史对话记录数据失败:', error);
            });
        }, 
        sendId (chatId) {
          console.log(chatId);
          this.$emit('handleChatId', chatId);
        }
    }
}
</script>

<style scoped>
ul {
  list-style: none;
}
</style>