# OpenClaw ACP 调研报告

> Agent Client Protocol (ACP) - 让外部 AI 编程助手通过标准协议接入 OpenClaw

---

## 一、什么是 ACP？

**ACP (Agent Client Protocol)** 是一个标准化的 AI Agent 通信协议。OpenClaw 通过 ACP 可以直接驱动外部编程助手，如：

- **Pi** - OpenClaw 内置 AI
- **Claude Code** - Anthropic 的 CLI 编程助手
- **Codex** - OpenAI 的 CLI 编程助手
- **OpenCode** - 开源的 CLI 编程助手
- **Gemini CLI** - Google 的 CLI 助手
- **Kimi** - 月之暗面助手

---

## 二、ACP vs Sub-agents 对比

| 特性 | ACP Session | Sub-agent Run |
|------|-------------|---------------|
| **运行时** | ACP 后端插件（如 acpx） | OpenClaw 原生子代理运行时 |
| **会话 key** | `agent:<agentId>:acp:<uuid>` | `agent:<agentId>:subagent:<uuid>` |
| **主命令** | `/acp ...` | `/subagents ...` |
| **Spawn 工具** | `sessions_spawn` with `runtime:"acp"` | `sessions_spawn`（默认） |
| **适用场景** | 外部 harness 运行时 | OpenClaw 原生任务 |

---

## 三、核心玩法

### 3.1 快速开始

```bash
# 1. 安装 acpx 插件
openclaw plugins install acpx
openclaw config set plugins.entries.acpx.enabled true

# 2. 启用 ACP
openclaw config set acp.enabled true
openclaw config set acp.defaultAgent "codex"

# 3. 重启 Gateway
openclaw gateway restart
```

### 3.2 配置 ACP

```json5
{
  acp: {
    enabled: true,
    dispatch: { enabled: true },
    backend: "acpx",
    defaultAgent: "codex",
    allowedAgents: ["pi", "claude", "codex", "opencode", "gemini", "kimi"],
    maxConcurrentSessions: 8,
    stream: {
      coalesceIdleMs: 300,
      maxChunkChars: 1200,
    },
    runtime: {
      ttlMinutes: 120,
    },
  }
}
```

### 3.3 线程绑定配置

**Discord 配置：**
```json5
{
  channels: {
    discord: {
      threadBindings: {
        enabled: true,
        spawnAcpSessions: true,
      },
    },
  }
}
```

**Telegram 配置：**
```json5
{
  channels: {
    telegram: {
      threadBindings: {
        enabled: true,
        spawnAcpSessions: true,
      },
    },
  }
}
```

---

## 四、命令手册

### 4.1 基础命令

| 命令 | 功能 | 示例 |
|------|------|------|
| `/acp spawn` | 创建 ACP 会话 | `/acp spawn codex --mode persistent --thread auto` |
| `/acp cancel` | 取消当前运行 | `/acp cancel agent:codex:acp:<uuid>` |
| `/acp steer` | 发送引导指令 | `/acp steer --session support 优先处理失败测试` |
| `/acp close` | 关闭会话 | `/acp close` |
| `/acp status` | 查看状态 | `/acp status` |
| `/acp sessions` | 列出会话 | `/acp sessions` |
| `/acp doctor` | 诊断健康 | `/acp doctor` |

### 4.2 运行时控制

| 命令 | 功能 | 示例 |
|------|------|------|
| `/acp model` | 设置模型 | `/acp model anthropic/claude-opus-4-5` |
| `/acp permissions` | 设置权限 | `/acp permissions strict` |
| `/acp timeout` | 设置超时 | `/acp timeout 120` |
| `/acp cwd` | 设置工作目录 | `/acp cwd /Users/user/repo` |
| `/acp set-mode` | 设置模式 | `/acp set-mode plan` |
| `/acp reset-options` | 重置选项 | `/acp reset-options` |

### 4.3 线程模式

```bash
# 自动模式：在活跃线程中绑定该线程
/acp spawn codex --mode persistent --thread auto

# 这里模式：要求在活跃线程中
/acp spawn codex --thread here

# 关闭模式：不绑定
/acp spawn codex --mode oneshot --thread off
```

---

## 五、API 调用

### 5.1 使用 sessions_spawn

```json
{
  "task": "打开仓库并总结失败的测试",
  "runtime": "acp",
  "agentId": "codex",
  "thread": true,
  "mode": "session"
}
```

**参数说明：**
- `task` (必需): 初始提示
- `runtime`: 设置为 `"acp"`
- `agentId`: ACP 目标 harness ID（如 `codex`, `claude`）
- `thread`: 是否绑定线程
- `mode`: `"run"`（一次性）或 `"session"`（持久）
- `cwd`: 工作目录
- `label`: 会话标签
- `resumeSessionId`: 恢复已有会话

### 5.2 恢复会话

```json
{
  "task": "继续之前的任务 - 修复剩余的测试失败",
  "runtime": "acp",
  "agentId": "codex",
  "resumeSessionId": "<之前的会话ID>"
}
```

---

## 六、权限配置

### 6.1 权限模式

| 值 | 行为 |
|---|------|
| `approve-all` | 自动批准所有文件写入和 shell 命令 |
| `approve-reads` | 自动批准读取；写入和执行需要提示 |
| `deny-all` | 拒绝所有权限提示 |

### 6.2 非交互权限

| 值 | 行为 |
|---|------|
| `fail` | 中止会话并报错（默认） |
| `deny` | 静默拒绝权限并继续 |

### 6.3 配置命令

```bash
openclaw config set plugins.entries.acpx.config.permissionMode approve-all
openclaw config set plugins.entries.acpx.config.nonInteractivePermissions fail
```

> ⚠️ **重要**：默认配置下，任何触发权限提示的写操作或执行都可能导致会话失败。

---

## 七、IDE 集成

### 7.1 Zed 编辑器

```json
{
  "agent_servers": {
    "OpenClaw ACP": {
      "type": "custom",
      "command": "openclaw",
      "args": ["acp", "--url", "wss://gateway-host:18789", "--token", "<token>", "--session", "agent:design:main"],
      "env": {}
    }
  }
}
```

### 7.2 acpx 直连

```bash
# 一次性请求
acpx openclaw exec "总结当前 OpenClaw 会话状态"

# 持久会话
acpx openclaw sessions ensure --name codex-bridge
acpx openclaw -s codex-bridge --cwd /path/to/repo "询问我的 OpenClaw 工作代理关于这个仓库的最近上下文"
```

---

## 八、持久绑定配置

### 8.1 绑定模型

```json5
{
  agents: {
    list: [
      {
        id: "codex",
        runtime: {
          type: "acp",
          acp: {
            agent: "codex",
            backend: "acpx",
            mode: "persistent",
            cwd: "/workspace/openclaw",
          },
        },
      },
    ],
  },
  bindings: [
    {
      type: "acp",
      agentId: "codex",
      match: {
        channel: "discord",
        accountId: "default",
        peer: { kind: "channel", id: "222222222222222222" },
      },
      acp: { label: "codex-main" },
    },
    {
      type: "acp",
      agentId: "claude",
      match: {
        channel: "telegram",
        accountId: "default",
        peer: { kind: "group", id: "-1001234567890:topic:42" },
      },
      acp: { cwd: "/workspace/repo-b" },
    },
  ],
}
```

---

## 九、常见问题排查

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| `ACP runtime backend is not configured` | 后端插件缺失 | 安装并启用 acpx 插件 |
| `ACP is disabled by policy` | ACP 全局禁用 | 设置 `acp.enabled=true` |
| `ACP agent "<id>" is not allowed` | Agent 不在白名单 | 更新 `acp.allowedAgents` |
| `Unable to resolve session target` | 错误的 key/id/label | 运行 `/acp sessions` 查看正确标识 |
| `Thread bindings are unavailable` | 适配器不支持线程绑定 | 使用 `--thread off` |
| `Permission prompt unavailable in non-interactive mode` | 权限被阻止 | 设置 `permissionMode=approve-all` |

---

## 十、使用场景示例

### 场景 1：Discord 线程中运行 Codex

```
用户: 在这个线程里启动一个持久的 Codex 会话
→ /acp spawn codex --mode persistent --thread auto

后续: 所有线程消息自动路由到同一 ACP 会话
```

### 场景 2：一次性任务

```
用户: 用 Claude Code 运行这个任务
→ /acp spawn claude --mode oneshot --thread off

结果: 任务完成后会话自动关闭
```

### 场景 3：会话恢复

```
用户: 继续之前的会话
→ 使用 resumeSessionId 参数恢复

场景: 从笔记本切换到手机，继续之前的编码会话
```

### 场景 4：多 Agent 协作

```
- Agent A (main): 处理用户请求
- Agent B (codex): 专门写代码
- Agent C (claude): 专门 Code Review
```

---

## 十一、总结

| 特性 | 说明 |
|------|------|
| **协议** | ACP (Agent Client Protocol) |
| **后端** | acpx 插件 |
| **支持 Agent** | Pi, Claude Code, Codex, OpenCode, Gemini CLI, Kimi |
| **线程绑定** | Discord / Telegram |
| **优势** | 外部 harness 运行时，完整 IDE 集成能力 |
| **对比** | Sub-agents 是 OpenClaw 原生，ACP 是外部运行时 |

---

*文档生成时间: 2026-03-17*
