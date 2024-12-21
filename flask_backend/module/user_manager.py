from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import os
import json
import hashlib

DATA_FILE = "./data/users.json"

def load_users():
    # 检查文件是否为空并初始化
    if not os.path.exists(DATA_FILE) or os.stat(DATA_FILE).st_size == 0:
        with open(DATA_FILE, 'w') as file:
            json.dump([], file)  # 将文件内容初始化为空的列表（JSON格式）

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_users(users):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, ensure_ascii=False, indent=4)

def save_singleUser(userId, user_info):
    # 构造文件路径
    data_dir = f'./data/{userId}'
    data_file = f'{data_dir}/user_info.json'
    
    # 如果目录不存在，递归创建用户数据{username}目录
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # 存储用户信息user_info.json
    with open(data_file, "w", encoding="utf-8") as file:
        json.dump(user_info, file, ensure_ascii=False, indent=4)

    # 递归创建子目录conversation_logs
    conversation_dir = os.path.join(data_dir, 'conversation_logs')
    os.makedirs(conversation_dir)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(username, password):
    users = load_users()

    if any(user["username"] == username for user in users):
        return False, "用户已存在"
    # print(username, password)
    cur_user = {"username": username, "password": hash_password(password)}
    users.append(cur_user)   
    # 分两处：初始化、存储用户信息
    save_users(users)
    save_singleUser(username, cur_user)
    return True, "用户注册成功！"


def authenticate_user(username, password):
    users = load_users()
    hashed_password = hash_password(password)
    for user in users:
        if user["username"] == username and user["password"] == hashed_password:
            return True
    return False

