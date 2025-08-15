from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage
import os

import module.conversation as conversation
import module.user_manager as user_manager
# 本地开发时用
from config import SPARKAI_APP_ID, SPARKAI_API_SECRET, SPARKAI_API_KEY, SPARKAI_DOMAIN, SECRET_KEY



app = Flask(__name__)

# 星火大模型的配置参数
SPARKAI_URL = 'wss://spark-api.xf-yun.com/v1.1/chat'
# 暂时没法从环境变量中读取，先直接从本地 config 文件中读取。
# SPARKAI_APP_ID = os.environ.get('SPARKAI_APP_ID')
# SPARKAI_API_SECRET = os.environ.get('SPARKAI_API_SECRET')
# SPARKAI_API_KEY = os.environ.get('SPARKAI_API_KEY')
# SPARKAI_DOMAIN = os.environ.get('SPARKAI_DOMAIN', 'lite')
# SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')

# 初始化星火大模型
spark = ChatSparkLLM(
    spark_api_url=SPARKAI_URL,
    spark_app_id=SPARKAI_APP_ID,
    spark_api_key=SPARKAI_API_KEY,
    spark_api_secret=SPARKAI_API_SECRET,
    spark_llm_domain=SPARKAI_DOMAIN,
    streaming=False,
)

# 允许来自前端的源的跨域请求
CORS(app, origins=[
    "http://localhost:8080",                          # 本地调试
    "https://tiny-wen-da-wang-zhan.vercel.app/"     # 上线前端
])

app.config['SECRET_KEY'] = SECRET_KEY
jwt = JWTManager(app)  # 初始化 JWT 扩展


# 定义一个处理聊天请求的API
@app.route('/chat', methods=['POST'])
@jwt_required()
def chat():
    chatId = request.json.get('chatId')
    user_message = request.json.get('message')

    username = get_jwt_identity()
    file_path = conversation.create_folderPath(username, chatId)

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    # 存储用户的问题
    conversation.save_conversation(file_path, chatId, 'user', user_message)

    # 将用户消息传递给星火大模型
    messages = [ChatMessage(role="user", content=user_message)]
    handler = ChunkPrintHandler()
    response = spark.generate([messages], callbacks=[handler])
    reply = response.generations[0][0].text

    # 存储大模型的回复
    conversation.save_conversation(file_path, chatId, 'assistant', reply)

    # 返回大模型的回复
    return jsonify({"reply": reply})


# 一个返回历史对话标题（给历史对话侧边栏组件）的接口
@app.route('/load_conversationTitle', methods=['GET'])
@jwt_required()
def load_conversationTitle():
    username = get_jwt_identity()
    # print(username)
    
    folder_path = conversation.create_folderPath(username)

    return conversation.load_conversation(folder_path, list_all=True)


# 一个接收特定对话id，返回该对话的历史对话内容的接口
@app.route('/load_conversationContent', methods=['GET'])
@jwt_required()
def load_conversationContent():
    username = get_jwt_identity()
    # print(username)
    chatId = request.args.get('chatId')

    folder_path = conversation.create_folderPath(username, chatId)

    return conversation.load_conversation(folder_path, chatId=chatId)


# 一个用户注册时，接收、存储用户的注册信息的接口
@app.route('/user_register', methods=['POST'])
def user_register():

    data = request.get_json()
    if not data:
        return jsonify({"error": "没有接收到json数据"}), 400 

    username = data.get('username')
    password = data.get('password')

    # print(username, password)
    status, message = user_manager.register_user(username, password)
    return jsonify({ "status": status, "message": message })


# 一个用户登录时，校验用户发送的登录信息是否正确的接口
@app.route('/user_login', methods=['POST'])
def user_login():
    
    data = request.get_json()
    if not data:
        return jsonify({"error": "没有接收到json数据"}), 400 

    username = data.get('username')
    password = data.get('password')
    status = user_manager.authenticate_user(username, password)
    print(status)
    # 若用户登录成功
    if (status == True): 
        # 生成 JWT
        access_token = create_access_token(identity=username)
        
        return jsonify({
            'status': status, 
            'access_token': access_token
        })
    # 用户登录失败
    else: 
        return jsonify({ 'status': status })


if __name__ == '__main__':
    # 在 Railway 部署中监听端口
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
