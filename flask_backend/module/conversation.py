from flask import jsonify
import json
import os
from datetime import datetime


# 判断用户，并加载对话
def load_user(userId, chatId=None, list_all=False): 
    folder_path = create_folderPath(userId, chatId)

    return load_conversation(folder_path, chatId, list_all)


def save_user(userId, chatId, role, content):
    file_path = create_folderPath(userId, chatId)

    return save_conversation(file_path, chatId, role, content)


# 加载对话函数
# 分为两种情况：1. 加载所有文件标题//2. 加载特定文件的对话内容 
# 追加更改：根据传入的文件路径，打开对话文件
def load_conversation(folder_path, chatId=None, list_all=False):
    if list_all:
        # 如果需要列出所有对话文件信息
        conversation_list = []
        try:
            # 遍历目录中的所有 JSON 文件
            for file_name in os.listdir(folder_path):
                if file_name.endswith('.json'):
                    file_path = os.path.join(folder_path, file_name)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        # 从文件名提取 chatId，并尝试从文件内容中提取标题
                        chat_id = file_name[len('conversation_log_'):-len('.json')]
                        title = data[0].get('title', '无标题') if data and isinstance(data, list) and 'title' in data[0] else '无标题'
                        conversation_list.append({'chatId': chat_id, 'title': title})
            return conversation_list
        except Exception as e:
            print(f"遍历文件时发生错误: {e}")
            return []


    # 如果提供了 chatId，则返回特定对话内容
    if chatId is not None: 
        # 尝试加载 JSON 文件内容
        try:
            with open(folder_path, 'r', encoding='utf-8') as f:
                conversations = json.load(f)
                
                return conversations
        except json.JSONDecodeError:
            # 如果 JSON 文件格式错误，打印错误信息并返回空列表
            print(f"JSON 文件 {folder_path} 格式无效，已重置为空文件。")
            with open(folder_path, 'w', encoding='utf-8') as f:
                json.dump([], f, ensure_ascii=False, indent=4)
            return []
        except Exception as e:
            # 捕获其他异常
            print(f"读取对话记录时发生错误: {e}")
            return []


def save_conversation(file_path, chatId, role, content):
    # 标准化要存储的历史对话数据
    new_data = {
        'role': role, 
        'content': content, 
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    # 打开文件进行读取和写入
    try:
        # 读取现有的对话记录，如果文件为空，则初始化一个空的对象（格式化）
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                conversation = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            conversation = create_conversationLog(chatId)
        
        # 将当前消息添加到对话记录中
        conversation = add_message(conversation, new_data)
        
        # 将对话记录写回文件
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(conversation, file, indent=4, ensure_ascii=False)

        print('对话历史文件存储OK！')
        
    except Exception as e:
        print(f"保存为文件时出错: {e}")


# 生成对应文件路径
def create_folderPath(userId, chatId=None):
    folder_path = os.path.join('.', 'data', userId, 'conversation_logs')
    if chatId: 
        folder_path = os.path.join(folder_path, f'conversation_log_{chatId}.json')

    elif not os.path.isfile(folder_path):
        os.makedirs(folder_path, exist_ok=True)  # 如果目录不存在，创建它

    return folder_path


# 对话文件需要一些基本格式（加入用户功能后，大概也会在这里修改）
def create_conversationLog(chatId):
    conversation = {
        'chatId': chatId, 
        'messages': []
    }
    
    return conversation

# 无需循环一次性写入。app接口中是每有一条新纪录就存储下来（可能是为了防止浏览器突然关闭，导致存储失败）
def add_message(conversation, cur_message): 
    new_conversation = conversation

    # 将传来的单条信息追加到对话记录中
    new_conversation['messages'].append(cur_message)

    return new_conversation