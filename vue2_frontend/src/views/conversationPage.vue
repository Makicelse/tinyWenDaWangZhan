<template>
  <div class="shouYe">
    <div class="sidebar-history">
      <historyChatsList @handleChatId="getChatContent"></historyChatsList>
    </div>

    <div class="chat-area">
      <h2>聊天</h2>
      <div class="ans-area">
        <div v-for="(item) in messages" :key="item.timestamp">
            <message :message="item"></message>
        </div>
      </div>

      <div class="ques-area">
        <input v-model="input" type="text" placeholder="请输入想问的问题">
        <button @click="postInput()">发送</button>
      </div>
    </div>
  </div>
</template>

<script>
import message from '@/components/message.vue';
import historyChatsList from '@/components/historyChatsList.vue';

export default {
    data () {
        return {
            cur_chatId: this.generateUUid(),
            input: "",
            messages: []
        }
    }, 
    components: {
        message, 
        historyChatsList
    },
    created () {
        
    }, 
    methods: {
        generateTimeId () {
            return `id_${Date.now()}`;
        }, 
        generateUUid () {
          return crypto.randomUUID();
        }, 
        postInput () {
            let ques = this.input;
            // 前端本地对话缓存
            this.messages.push({
                role: 'user', 
                content: ques, 
                timestamp: this.generateTimeId()
            });

            // 向后端发送请求，后端返回AI回答
            // mock接口：http://127.0.0.1:4523/m2/4755954-4409227-default/239445275
            // flask后端接口：http://127.0.0.1:5000/chat 
            this.$axios.post('http://127.0.0.1:5000/chat', {
                'chatId': this.cur_chatId,
                'message': ques
            }, {
                headers: {
                  Authorization: `Bearer ${this.$store.state.accessToken}`,
                }
            })
            .then((response) => {
                console.log(response);
                let answer = response.data.reply;
                this.messages.push({
                    role: 'assistant', 
                    content: answer, 
                    timestamp: this.generateTimeId()
                });
            })
            .catch((error) => {
                console.log('请求出错了！');
                console.log(error);
            })

            this.input = ""
        },  
        getChatContent (chatId) {
          // 对话ID复用性高，因此在前端缓存
          this.cur_chatId = chatId

          // 获取历史对话内容。
          // mock接口：http://127.0.0.1:4523/m2/4755954-4409227-default/242100735?apifoxApiId=242100735
          // 后端接口：http://127.0.0.1:5000/load_conversationContent
          this.$axios.get('http://127.0.0.1:5000/load_conversationContent', {
            params: {
              chatId: this.cur_chatId
            }, 
            headers: {
              Authorization: `Bearer ${this.$store.state.accessToken}` // 添加特定的 Header
            }
          })
            .then(response => {
              console.log('接口返回数据：', response.data);
              
              // 将后端返回的历史对话内容保存到本地
              this.messages = response.data.messages;
              // 预估：显示页面对话内容的messages从空值变有值，页面实时渲染变化。
            })
            .catch(error => {
              // 请求失败，处理错误。
              console.error('请求接口失败：', error);
              
            })
        }
    }
}
</script>

<style scoped>
.shouYe {
  position: relative;
  display: flex;
  justify-content: space-between;
}

.sidebar-history {
  border: 1px solid #ccc;
  width: 200px;
  padding: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.chat-area {
  flex: 1;
  padding: 30px;
}

.ans-area {
    border: 2px solid transparent;
    border-radius: 10px;
    max-width: 1000px;
    min-height: 500px;
    max-height: 80vh;
    overflow-y: auto;
    background-color: aliceblue;
    margin: auto;
    margin-bottom: 25px;
}

.ques-area {
  display: flex;                  /* 使用 flexbox 排列 */
  align-items: center;            /* 垂直居中 */
  gap: 10px;                      /* 输入框和按钮之间的间距 */
  max-width: 500px;               /* 最大宽度 */
  margin: 20px auto;              /* 居中显示，上下有间距 */
  padding: 10px;
}

input[type="text"] {
  flex-grow: 1;                   /* 输入框占满剩余空间 */
  padding: 10px 15px;             /* 内边距，增加可点击区域 */
  font-size: 14px;                /* 字体大小 */
  border: 1px solid #555;         /* 边框颜色 */
  outline: none;                  /* 去掉聚焦时的默认轮廓 */
  transition: border-color 0.3s;  /* 平滑过渡效果 */
  
  position: relative;
  top: 3px;
}

</style>