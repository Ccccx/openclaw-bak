# OpenClaw 架构模式与记忆系统深度解读

## 一、核心定位

OpenClaw 是一个**自托管的多通道网关**，它连接了各种聊天应用（WhatsApp、Telegram、Discord、iMessage 等）与 AI 编程助手。它的核心价值在于：

- **数据自主**：运行在用户自己的硬件上
- **多通道统一**：一个 Gateway 服务所有聊天渠道
- **Agent 原生**：专为编程 Agent 设计，支持工具调用、会话管理、记忆系统和多 Agent 路由

---

## 二、整体架构模式

### 2.1 架构分层

```
┌─────────────────────────────────────────────────────────────────┐
│                        Chat Apps + Plugins                      │
│   (WhatsApp, Telegram, Discord, iMessage, Signal, Slack...)    │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                        🦞 Gateway (核心)                        │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐ │
│  │  消息路由   │  │  会话管理   │  │      插件系统           │ │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘ │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐ │
│  │  认证授权   │  │  记忆系统   │  │      Provider 连接      │ │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘ │
└──────────────────────────┬──────────────────────────────────────┘
                           │
         ┌─────────────────┼─────────────────┐
         ▼                 ▼                 ▼
   ┌──────────┐     ┌──────────┐     ┌──────────┐
   │  CLI     │     │ Web UI   │     │  Nodes   │
   └──────────┘     └──────────┘     └──────────┘
```

### 2.2 Gateway 核心职责

Gateway 是整个系统的**唯一真相来源**：

1. **连接管理**：唯一打开 WhatsApp（Telegram 等）会话的地方
2. **协议转换**：所有客户端通过 WebSocket 连接，Gateway 验证 JSON Schema
3. **事件分发**：发送 `agent`、`chat`、`presence`、`heartbeat`、`cron` 等事件
4. **会话拥有权**：所有会话状态存储在 Gateway 端

### 2.3 客户端类型

| 类型 | 连接方式 | 职责 |
|------|----------|------|
| **Control Clients** | WebSocket | macOS App、CLI、Web UI、自动化脚本 |
| **Nodes** | WebSocket (role: node) | macOS/iOS/Android 设备，提供 canvas/camera/screen 命令 |
| **WebChat** | WebSocket | 静态 UI，聊天历史和发送 |

---

## 三、连接生命周期

```
Client                      Gateway
   │                          │
   │──── req:connect ────────>│
   │<─── res (ok/snapshot) ───│
   │                          │
   │<─── event:presence ──────│
   │<─── event:tick ─────────│
   │                          │
   │──── req:agent ──────────>│
   │<─── res:agent (accepted)│
   │<─── event:agent (stream) │
   │<─── res:agent (final) ──│
```

**关键点**：
- 首帧必须是 `connect`
- 幂等键（Idempotency keys）用于 `send`、`agent` 等副作用方法
- 设备身份 + 签名验证确保安全配对

---

## 四、记忆系统详解

### 4.1 记忆文件架构

```
~/.openclaw/workspace/
├── MEMORY.md              # 长期记忆（只读/主会话）
├── AGENTS.md              # Agent 配置
├── USER.md                # 用户信息
├── SOUL.md                # Agent 人格
├── TOOLS.md               # 工具配置
├── HEARTBEAT.md           # 心跳任务
├── BOOTSTRAP.md           # 初始化引导
├── memory/
│   ├── 2026-01-01.md     # 每日日志（每日创建）
│   ├── 2026-01-02.md
│   ├── ...
│   └── 2026-03-17.md
```

### 4.2 记忆分层策略

| 记忆类型 | 文件位置 | 加载规则 |
|----------|----------|----------|
| **长期记忆** | `MEMORY.md` | 仅主会话（私人 DM）加载 |
| **每日日志** | `memory/YYYY-MM-DD.md` | 读取今天 + 昨天 |
| **即时上下文** | 会话 transcript | 会话级别，会话结束时可选择导出 |

### 4.3 记忆工具

```python
# 语义搜索
memory_search(query: string) → [snippet]

# 精准读取
memory_get(path: string, from?: int, lines?: int) → text
```

### 4.4 向量记忆搜索

**混合检索架构**：
```
┌─────────────┐     ┌─────────────┐
│ Vector相似度 │     │  BM25关键词  │
│ (语义匹配)    │     │ (精确匹配)   │
└──────┬──────┘     └──────┬──────┘
       │                   │
       └─────────┬─────────┘
                 ▼
        ┌─────────────────┐
        │   分数加权合并   │
        └────────┬────────┘
                 ▼
        ┌─────────────────┐
        │ MMR多样性重排    │  ← 减少重复结果
        └────────┬────────┘
                 ▼
        ┌─────────────────┐
        │ 时间衰减(可配置) │  ← 新笔记权重更高
        └────────┬────────┘
                 ▼
             Top-K 结果
```

**配置参数**：
```json5
{
  memorySearch: {
    provider: "openai",  // 或 gemini/voyage/mistral/ollama/local
    query: {
      hybrid: {
        enabled: true,
        vectorWeight: 0.7,
        textWeight: 0.3,
        mmr: { enabled: true, lambda: 0.7 },
        temporalDecay: { enabled: true, halfLifeDays: 30 }
      }
    }
  }
}
```

### 4.5 自动记忆刷新（Compaction 前置）

当会话接近**自动压缩**时，OpenClaw 会触发一个静默的 Agent 轮次，提醒模型在上下文压缩前写入持久记忆：

```json5
{
  compaction: {
    reserveTokensFloor: 20000,
    memoryFlush: {
      enabled: true,
      softThresholdTokens: 4000,
      systemPrompt: "Session nearing compaction. Store durable memories now.",
      prompt: "Write any lasting notes to memory/YYYY-MM-DD.md; reply with NO_REPLY if nothing to store."
    }
  }
}
```

**关键点**：
- 默认发送 `NO_REPLY`，用户看不到这个静默轮次
- 每个压缩周期只触发一次
- 工作区只读时跳过

---

## 五、QMD 后端（实验性）

使用 [QMD](https://github.com/tobi/qmd) 替代内置 SQLite：

- **BM25 + 向量 + 重排序**组合
- 本地运行 via Bun + node-llama-cpp
- 自动下载 GGUF 模型
- 支持会话 JSONL 索引

```json5
memory: {
  backend: "qmd",
  qmd: {
    update: { interval: "5m" },
    limits: { maxResults: 6, timeoutMs: 4000 },
    sessions: { enabled: true }
  }
}
```

---

## 六、会话管理

### 6.1 会话隔离策略

| 模式 | 描述 | 适用场景 |
|------|------|----------|
| `main` | 所有 DM 共享主会话 | 单用户 |
| `per-peer` | 按发送者隔离 | 多用户 DM |
| `per-channel-peer` | 按渠道 + 发送者隔离 | 推荐多用户 |
| `per-account-channel-peer` | 完全隔离 | 多账户 |

### 6.2 会话状态存储

- **Store 文件**：`~/.openclaw/agents/<agentId>/sessions/sessions.json`
- **Transcript**：`~/.openclaw/agents/<agentId>/sessions/<SessionId>.jsonl`
- Gateway 是唯一真相来源，客户端必须查询 Gateway

---

## 七、安全模型

### 7.1 设备配对流程

```
新设备 ──connect──> Gateway
    │
    ▼
生成 challenge nonce
    │
    ▼
设备签名 (payload v3: platform + deviceFamily)
    │
    ▼
Gateway 验证 + 颁发设备令牌
    │
    ▼
后续连接使用设备令牌
```

### 7.2 本地信任

- **本地连接**（loopback 或同主机 Tailscale）：可自动批准
- **远程连接**：需要手动批准

---

## 八、关键设计原则

1. **单一 Gateway**：每个主机一个 Gateway，控制所有消息渠道
2. **工作区即记忆**：Markdown 文件是唯一真相来源
3. **静默记忆刷新**：Compaction 前自动触发，不干扰用户
4. **混合检索**：语义 + 关键词 + 时间衰减 + 多样性
5. **设备级配对**：安全、可追溯的设备身份
6. **会话隔离**：保护多用户隐私

---

*文档生成时间: 2026-03-17*
