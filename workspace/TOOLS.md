# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

### 生图（ModelScope）

- API Key: ms-e9df1fa1-c961-4132-89d9-5d515d660b6f
- 默认模型: Tongyi-MAI/Z-Image-Turbo
- 生图完成后，必须用**在线URL**发送图片，不要用本地路径！

### 飞书发图片

- 使用 feishu-send-image skill 发送图片到飞书群组或用户
- 脚本路径: `/home/admin/.openclaw/shared-skills/feishu-send-image/scripts/send_image.py`
- 用法: `python3 send_image.py <图片路径或URL> --receive-id <接收者ID> --receive-id-type chat_id|user_id`
- 群组ID示例: `oc_3f109728466e9a968ad73c0957638eb4`
- 用户ID示例: `ou_xxxxx` (需使用 open_id 或 user_id)

### 生图输出格式（必须严格遵守）

生图完成后，**必须返回2条内容**：

**内容1（代码块格式）：**
```
📝 原始提示词
用户输入的提示词内容
🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧
🔧 优化后提示词
优化后的提示词内容
🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧
📊 模型调用统计
模型名称: xxx
模型当日调用: x/x
总当日调用: x/x
生成耗时: x秒
🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧
🖼️ 生成的图片
在线地址: [图片URL]
本地保存: [本地路径]
```

**内容2：**
- 如果是飞书消息 → 使用 feishu-send-image skill 发送图片
- 否则 → 直接发送本地保存的文件

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
