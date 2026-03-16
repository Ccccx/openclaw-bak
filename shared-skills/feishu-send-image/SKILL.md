---
name: feishu-send-image
description: |
  发送图片到飞书群组或用户。先上传图片到飞书，然后构建图片消息发送到指定群组或用户。
  当用户要求在飞书发送图片时使用此技能。
version: 1.1.0
---

# 飞书发送图片技能

此技能用于将图片发送到飞书群组或用户。

## 功能特性

1. **上传图片**: 将本地图片或URL图片上传到飞书
2. **发送图片消息**: 将图片发送到指定群组或用户

## 支持场景

- **群组消息**: 发送图片到飞书群组
- **私聊消息**: 发送图片给飞书用户

## 使用方法

### 基本调用

```bash
python3 scripts/send_image.py <图片路径或URL> --receive-id <接收者ID> --receive-id-type <类型>
```

### 参数说明

| 参数 | 说明 | 示例 |
|------|------|------|
| image | 图片路径或URL | `/tmp/image.png` 或 `https://xxx.com/img.png` |
| receive-id | 接收者ID | 群组ID或用户ID |
| receive-id-type | 接收者类型 | `chat_id` (群组) 或 `user_id` (用户) |

### 场景示例

**发送到群组：**
```bash
python3 scripts/send_image.py https://example.com/image.png --receive-id oc_3f109728466e9a968ad73c0957638eb4 --receive-id-type chat_id
```

**发送给用户：**
```bash
python3 scripts/send_image.py /tmp/image.png --receive-id ou_edad1a9e5a6b404482a53140669d52b1 --receive-id-type user_id
```

### ID 类型判断

- **群组ID**: 以 `oc_` 开头
- **用户ID**: 以 `ou_` 开头

## 实施步骤

### Step 1: 获取参数

1. 提取图片路径或URL
2. 提取接收者ID（群组ID或用户ID）
3. 根据ID前缀判断类型：
   - `oc_` → chat_id (群组)
   - `ou_` → user_id (用户)

### Step 2: 调用脚本

### Step 3: 返回结果

```
=== 飞书图片发送成功 ===

🖼️ 图片已发送
类型: 群组/私聊
接收者: oc_xxx / ou_xxx
消息ID: om_xxx

✅ 发送成功！
```

## 注意事项

1. 图片大小不能超过 10MB
2. GIF 图片分辨率不能超过 2000x2000，其他图片不超过 12000x12000
3. 群组ID以 "oc_" 开头，用户ID以 "ou_" 开头
4. 需要在飞书开放平台配置应用并开通 im:image 权限

## 配置文件

脚本会自动从环境变量读取飞书配置：
- FEISHU_APP_ID: 飞书应用ID (默认: cli_a813ea51f979901c)
- FEISHU_APP_SECRET: 飞书应用密钥

默认使用 OpenClaw 配置中的飞书应用。
