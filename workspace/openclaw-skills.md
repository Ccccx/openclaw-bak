# OpenClaw Skills 文档

> 更新时间: 2026-03-01

---

## 一、系统 Skills (51个)

| Skill名称 | 描述 |
|-----------|------|
| 1password | 1Password CLI 集成 (op)，管理密码库 |
| apple-notes | Apple Notes 管理 (memo CLI) |
| apple-reminders | Apple Reminders 管理 (remindctl CLI) |
| bear-notes | Bear Notes 管理 (grizzly CLI) |
| blogwatcher | 博客/RSS 监控 |
| blucli | BluOS 音频控制 |
| bluebubbles | iMessage 发送管理 |
| camsnap | RTSP/ONVIF 摄像头捕获 |
| canvas | Canvas 画布控制 |
| clawhub | ClawHub 技能市场搜索/安装/发布 |
| coding-agent | 编码代理 (Codex/Claude Code/Pi) |
| discord | Discord 操作 |
| eightctl | Eight Sleep 智能床垫控制 |
| gemini | Gemini CLI 集成 |
| gh-issues | GitHub Issues 批量处理 |
| gifgrep | GIF 搜索下载 |
| github | GitHub 操作 (gh CLI) |
| gog | Google Workspace (Gmail/Calendar/Drive) |
| goplaces | Google Places API |
| healthcheck | 主机安全加固检查 |
| himalaya | 邮件管理 (IMAP/SMTP) |
| imsg | iMessage/SMS CLI |
| mcporter | MCP 服务器工具调用 |
| model-usage | 模型使用统计 |
| nano-banana-pro | Gemini 3 Pro 图像生成 |
| nano-pdf | PDF 编辑 |
| notion | Notion API |
| obsidian | Obsidian 笔记库管理 |
| openai-image-gen | OpenAI 图像生成 |
| openai-whisper | 本地语音转文字 (Whisper) |
| openai-whisper-api | OpenAI 语音转文字 API |
| openhue | Philips Hue 灯光控制 |
| oracle | Oracle CLI 最佳实践 |
| ordercli | 外卖订单查询 (Foodora) |
| peekaboo | macOS UI 自动化 |
| sag | ElevenLabs TTS 语音合成 |
| session-logs | 会话日志搜索分析 |
| sherpa-onnx-tts | 本地离线 TTS |
| skill-creator | 技能创建器 |
| slack | Slack 操作 |
| songsee | 音频频谱可视化 |
| sonoscli | Sonos 音箱控制 |
| spotify-player | Spotify 播放控制 |
| summarize | URL/文件摘要/转录 |
| things-mac | Things 3 任务管理 |
| tmux | tmux 会话控制 |
| trello | Trello 看板管理 |
| video-frames | 视频帧提取 |
| voice-call | 语音通话 |
| wacli | WhatsApp 消息发送 |
| weather | 天气查询 |
| xurl | X (Twitter) API 操作 |

---

## 二、用户自定义 Skills (5个)

| Skill名称 | 描述 |
|-----------|------|
| find-skills | 技能发现与安装 |
| ontology | 知识图谱/记忆管理 |
| proactive-agent | 主动式代理 (WAL Protocol) |
| self-improving | 自反思代理 |
| skill-vetter | 技能安全审查 |

---

## 三、Workspace Skills (3个)

| Skill名称 | 描述 |
|-----------|------|
| humanizer | AI 内容去 AI 化 |
| mcporter | MCP 服务器工具调用 (本地副本) |
| modelscope-image-generation | ModelScope 文生图 |

---

## 四、已启用的 Skills 配置

根据 `openclaw.json` 配置，已启用的技能如下：

```json
{
  "skills": {
    "entries": {
      "notion": {
        "apiKey": "ntn_***"  // 已配置
      },
      "modelscope-image-generation": {
        "enabled": true
      }
    }
  }
}
```

---

## 五、Skills 目录位置

- 系统 Skills: `~/.npm-global/lib/node_modules/openclaw/skills/`
- 用户自定义: `~/.openclaw/shared-skills/`
- Workspace: `~/.openclaw/workspace/skills/`
