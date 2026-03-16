#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
飞书发送图片脚本
功能：上传图片到飞书并发送到指定群组或用户
"""

import os
import sys
import json
import requests
import argparse

# 从环境变量读取飞书配置
APP_ID = os.environ.get("FEISHU_APP_ID", "cli_a813ea51f979901c")
APP_SECRET = os.environ.get("FEISHU_APP_SECRET", "DA4Uqn04nH8FAE8DL9mYrhBqPrkmgwSr")

# 飞书API地址
BASE_URL = "https://open.feishu.cn/open-apis"

def get_tenant_access_token():
    """获取tenant_access_token"""
    url = f"{BASE_URL}/auth/v3/tenant_access_token/internal"
    data = {
        "app_id": APP_ID,
        "app_secret": APP_SECRET
    }
    response = requests.post(url, json=data)
    result = response.json()
    if result.get("code") == 0:
        return result.get("tenant_access_token")
    else:
        raise Exception(f"获取token失败: {result}")
    
def upload_image(token, image_path):
    """上传图片到飞书"""
    url = f"{BASE_URL}/im/v1/images"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    files = {
        "image": open(image_path, "rb")
    }
    data = {
        "image_type": "message"
    }
    response = requests.post(url, headers=headers, files=files, data=data)
    result = response.json()
    if result.get("code") == 0:
        return result.get("data", {}).get("image_key")
    else:
        raise Exception(f"上传图片失败: {result}")

def send_image_message(token, image_key, receive_id, receive_id_type="chat_id"):
    """发送图片消息"""
    url = f"{BASE_URL}/im/v1/messages?receive_id_type={receive_id_type}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "receive_id": receive_id,
        "msg_type": "image",
        "content": json.dumps({"image_key": image_key})
    }
    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    if result.get("code") == 0:
        return result.get("data", {}).get("message_id")
    else:
        raise Exception(f"发送图片失败: {result}")

def send_feishu_image(image_path, receive_id, receive_id_type="chat_id"):
    """
    主函数：发送图片到飞书群组或用户
    
    Args:
        image_path: 图片本地路径或URL
        receive_id: 接收者ID (群组ID或用户ID)
        receive_id_type: 接收者类型 "chat_id" 或 "user_id"
    
    Returns:
        message_id: 发送成功的消息ID
    """
    # 如果是URL，先下载到临时文件
    if image_path.startswith("http"):
        response = requests.get(image_path)
        temp_file = "/tmp/feishu_temp_image.png"
        with open(temp_file, "wb") as f:
            f.write(response.content)
        image_path = temp_file
    
    # 获取token
    token = get_tenant_access_token()
    print(f"✓ 获取token成功")
    
    # 上传图片
    image_key = upload_image(token, image_path)
    print(f"✓ 图片上传成功, image_key: {image_key}")
    
    # 发送图片消息
    message_id = send_image_message(token, image_key, receive_id, receive_id_type)
    print(f"✓ 图片消息发送成功, message_id: {message_id}")
    
    return message_id

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="飞书发送图片")
    parser.add_argument("image", help="图片路径或URL")
    parser.add_argument("--receive-id", required=True, help="接收者ID (群组ID或用户ID)")
    parser.add_argument("--receive-id-type", default="chat_id", choices=["chat_id", "user_id"], help="接收者类型")
    
    args = parser.parse_args()
    
    try:
        message_id = send_feishu_image(args.image, args.receive_id, args.receive_id_type)
        print(f"\n=== 发送成功 ===")
        print(f"消息ID: {message_id}")
    except Exception as e:
        print(f"发送失败: {e}")
        sys.exit(1)
