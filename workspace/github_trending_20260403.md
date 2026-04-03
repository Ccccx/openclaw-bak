# 📊 GitHub Trending 日榜深度调研报告

> **调研日期：** 2026年4月2日（UTC）/ 2026年4月3日（CST）
> 
> **调研范围：** GitHub Trending 日榜（综合榜 + 多语言分类榜）
> 
> **数据来源：** github.com/trending + GitHub API

---

## 📈 今日趋势总览

本日 GitHub Trending 呈现出以下显著特征：

- **🤖 AI/Agent 爆发式增长**：以 Claude Code、OpenAI Codex 为代表的 AI Coding Agent 持续霸榜，同时带动了一系列周边工具（Harness、SDK、集成工具）的热度
- **🔐 安全工具持续热门**：Aikido Safe Chain 等 npm/PyPI 安全防护工具进入视野，反映开发者对供应链安全的重视
- **🎬 内容创作工具崛起**：视频翻译（KrillinAI）、屏幕录制（OpenScreen）等内容生产工具获得大量关注
- **🗄️ 数据基础设施**：Lance（多模态 AI Lakehouse）、GLM-OCR 等数据层工具展现强劲势头
- **📚 学术/教育资源**：哈佛 CS249r 机器学习系统课程获得大量 Star

---

## 🔥 重点深度分析项目

---

### 1. 🦞 `siddharthvaddem/openscreen`

**基本信息**

| 指标 | 数值 |
|------|------|
| ⭐ Stars | 15,179 |
| 🍴 Forks | 1,045 |
| 🐙 语言 | TypeScript |
| 🔗 链接 | https://github.com/siddharthvaddem/openscreen |

**项目描述**

> Create stunning demos for free. Open-source, no subscriptions, no watermarks, and free for commercial use. An alternative to Screen Studio.

**深度分析**

OpenScreen 是 Screen Studio 的开源免费替代方案，专为创建精美的产品演示和引导视频而设计。它解决了内容创作者面临的核心痛点：Screen Studio 月费 $29，而 OpenScreen 完全免费、无水印、可商用。

**核心功能：**
- 全屏或指定窗口录制
- 自动/手动缩放（Zoom）效果
- 可自定义缩放深度级别
- 100% 免费（个人和商业用途）

**亮点分析：**
- **定位精准**：只做"基础但够用"的功能子集，降低开发复杂度同时满足大多数用户需求
- **商业模式对冲**：开发者明确表示"如果需要全部高级功能，推荐购买 Screen Studio"，体现了健康的开源生态观
- **市场需求真实**：屏幕录制+自动变焦是 YouTube/TikTok 创作者的刚需

**适用场景：**
- 产品演示视频制作
- 软件功能引导录制
- GitHub 项目介绍视频
- 技术博客/教程辅助素材

**趋势洞察：** 开源替代专有工具是持续的主题，尤其在 $29/月 vs 免费 的强烈对比下，OpenScreen 具有极强的用户吸引力。预计将持续增长。

---

### 2. 🤖 `sherlock-project/sherlock`

**基本信息**

| 指标 | 数值 |
|------|------|
| ⭐ Stars | 76,956 |
| 🍴 Forks | 9,045 |
| 🐙 语言 | Python |
| 🔗 链接 | https://github.com/sherlock-project/sherlock |

**项目描述**

> Hunt down social media accounts by username across social networks

**深度分析**

Sherlock 是一个通过用户名在多个社交网络平台上搜索对应账号的强大工具。它利用各平台公开信息和 API，通过穷举式查询快速判断用户名是否在特定平台注册。

**技术特点：**
- 支持 300+ 社交媒体平台
- 多线程并发查询，速度极快
- 简洁的命令行界面
- 可导出 JSON/CSV 格式结果

**核心使用场景：**
- OSINT（开源情报收集）
- 数字足迹追踪
- 账户安全审计
- 社交媒体品牌保护

**趋势洞察：** 长期稳居 Trending 榜单，说明 OSINT 和网络安全工具始终是开发者社区的刚性需求。

---

### 3. 🦙 `anthropics/claude-code`

**基本信息**

| 指标 | 数值 |
|------|------|
| ⭐ Stars | 106,315 |
| 🍴 Forks | 17,022 |
| 🐙 语言 | Shell |
| 🔗 链接 | https://github.com/anthropics/claude-code |

**项目描述**

> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.

**深度分析**

Claude Code 是 Anthropic 官方推出的终端编程 Agent，通过自然语言命令执行日常编码任务、解释复杂代码、处理 Git 工作流。

**核心能力：**
- **代码库理解**：深度理解整个代码库结构
- **任务执行**：自动执行重 routine 任务
- **Git 工作流**：处理 commit、branch、merge 等操作
- **代码解释**：深入分析复杂代码逻辑
- **多模型支持**：可在终端、IDE 或 GitHub 中使用

**安装方式：**
```bash
# MacOS/Linux
curl -fsSL https://claude.ai/install.sh | bash
# 或 Homebrew
brew install --cask claude-code
```

**趋势洞察：** Claude Code 代表了 AI 编程工具的主流方向——从辅助提示进化为能独立执行任务的 Agent。今日 Star 数突破 10 万，成为最受欢迎的 AI Coding 工具之一。

---

### 4. ⚡ `openai/codex`

**基本信息**

| 指标 | 数值 |
|------|------|
| ⭐ Stars | 72,565 |
| 🍴 Forks | 10,158 |
| 🐙 语言 | Rust |
| 🔗 链接 | https://github.com/openai/codex |

**项目描述**

> Lightweight coding agent that runs in your terminal

**深度分析**

Codex CLI 是 OpenAI 推出的轻量级终端编程 Agent，Rust 编写，主打快速、本地运行。

**安装方式：**
```bash
npm i -g @openai/codex
# 或
brew install --cask codex
```

**产品矩阵：**
- **Codex CLI**：本地终端 Agent（本次上榜）
- **Codex IDE**：VS Code、Cursor、Windsurf 插件
- **Codex App**：桌面应用体验
- **Codex Web**：云端 Agent（chatgpt.com/codex）

**趋势洞察：** OpenAI 与 Anthropic 在 AI Coding Agent 赛道形成双雄格局。Rust 实现确保了极致的性能表现，这是值得关注的架构选择。

---

### 5. 🔓 `asgeirtj/system_prompts_leaks`

**基本信息**

| 指标 | 数值 |
|------|------|
| ⭐ Stars | 36,041 |
| 🍴 Forks | 5,971 |
| 🐙 语言 | — |
| 🔗 链接 | https://github.com/asgeirtj/system_prompts_leaks |

**项目描述**

> Extracted system prompts from ChatGPT (GPT-5.4, GPT-5.3, Codex), Claude (Opus 4.6, Sonnet 4.6, Claude Code), Gemini (3.1 Pro, 3 Flash, CLI), Grok (4.2, 4), Perplexity, and more. Updated regularly.

**深度分析**

这是一个持续更新的 AI 系统提示词（System Prompt）泄露仓库，收集了主流 AI 产品的系统提示词。

**收录内容：**
- OpenAI：GPT-5.4、GPT-5.3、Codex
- Anthropic：Claude Opus 4.6、Sonnet 4.6、Claude Code
- Google：Gemini 3.1 Pro、Gemini 3 Flash、Gemini CLI
- xAI：Grok 4.2、Grok 4
- Perplexity 等

**价值分析：**
- **AI 对齐研究**：了解各 AI 系统的隐含行为规则
- **安全研究**：识别潜在的 prompt injection 风险
- **产品竞争分析**：了解竞品的能力边界和设计哲学
- **Prompt Engineering**：学习业界最佳实践

**趋势洞察：** 反映了大模型时代"模型行为理解"这一新兴研究领域的热度，也是 AI 安全研究的重要资源。

---

### 6. 🧠 `MervinPraison/PraisonAI`

**基本信息**

| 指标 | 数值 |
|------|------|
| ⭐ Stars | 6,290 |
| 🍴 Forks | 917 |
| 🐙 语言 | Python |
| 🔗 链接 | https://github.com/MervinPraison/PraisonAI |

**项目描述**

> PraisonAI 🦞 — Your 24/7 AI employee team. Automate and solve complex challenges with low-code multi-agent AI that plans, researches, codes, and delivers results to Telegram, Discord, and WhatsApp — running 24/7.

**深度分析**

PraisonAI 是一个低代码多 Agent AI 框架，特点是将 AI Agent 团队部署到即时通讯平台（TG/Discord/WhatsApp），实现 7x24 小时自动化任务处理。

**核心特性：**
- 多 Agent 协作（Handoffs 机制）
- Guardrails（内容安全护栏）
- Memory（记忆管理）
- RAG（检索增强生成）
- 100+ LLM 提供商支持
- MCP（Model Context Protocol）支持
- 消息平台集成（Telegram、Discord、WhatsApp）

**适用场景：**
- 自动化客服
- 持续研究代理
- 社交媒体运营自动化
- 内部知识库问答

**趋势洞察：** 低代码 Agent 框架 + IM 平台集成的组合非常实用，将 AI Agent 从"开发工具"变成"可运营的产品"，这是一个有价值的差异化方向。

---

### 7. 🏗️ `google/adk-go`

**基本信息**

| 指标 | 数值 |
|------|------|
| ⭐ Stars | 7,376 |
| 🍴 Forks | 606 |
| 🐙 语言 | Go |
| 🔗 链接 | https://github.com/google/adk-go |

**项目描述**

> An open-source, code-first Go toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control.

**深度分析**

Google Agent Development Kit (ADK) 的 Go 语言版本，是 Google 官方 AI Agent 开发工具包的跨语言扩展。

**核心设计理念：**
- **Code-First**：用代码而非配置来构建 Agent
- **软件工程原则**：将软件开发最佳实践应用于 AI Agent 构建
- **模块化**：灵活的组件化设计
- **模型无关**：虽然针对 Gemini 优化，但支持其他模型
- **云原生友好**：利用 Go 的并发优势

**ADK 家族：**
- `google/adk-python` — Python 版（主版）
- `google/adk-java` — Java 版
- `google/adk-go` — Go 版（本次上榜）
- `google/adk-web` — Web 版

**趋势洞察：** Google ADK 正在构建完整的跨语言 Agent 开发工具链。Go 版本的推出瞄准了云原生和后端服务场景。

---

### 8. 📦 `BoundaryML/baml`

**基本信息**

| 指标 | 数值 |
|------|------|
| ⭐ Stars | 7,886 |
| 🍴 Forks | 403 |
| 🐙 语言 | Rust |
| 🔗 链接 | https://github.com/BoundaryML/baml |

**项目描述**

> BAML: The AI framework that adds the engineering to prompt engineering

**深度分析**

BAML（Basically A Made-up Language）是一种专注于 AI 工作流的提示语言，通过将提示工程转化为"模式工程"来实现更可靠的 AI 输出。

**核心理念：**
- 传统的 prompt engineering 是"试错式"的
- BAML 把它变成"类型安全式"的
- 开发者关注"Prompt 模型"而非"字符串"
- 支持多语言绑定：Python、TypeScript、Ruby、Java、C#、Rust、Go

**关键价值：**
- 类型安全的提示词
- 结构化输出保证
- 可测试的 Prompts
- 跨语言一致性

**趋势洞察：** Prompt Engineering 的工程化是 2026 年的重要趋势，从"调 prompt 字符串"到"构建类型安全的提示系统"，这是 AI 应用开发走向成熟的重要标志。

---

### 9. 🎬 `krillinai/KrillinAI`

**基本信息**

| 指标 | 数值 |
|------|------|
| ⭐ Stars | 9,809 |
| 🍴 Forks | 861 |
| 🐙 语言 | Go |
| 🔗 链接 | https://github.com/krillinai/KrillinAI |

**项目描述**

> Minimalist AI Video Translation and Dubbing Tool — 100种语言双向翻译，一键部署全流程

**深度分析**

KrillinAI（克林AI）是一个端到端 AI 视频翻译和配音工具，支持 100 种语言的自动翻译和配音。

**核心功能：**
- **视频采集**：支持 yt-dlp 下载或本地上传
- **语音识别**：基于 Whisper 的高精度语音识别
- **智能分段**：LLM 驱动字幕对齐和分段
- **翻译引擎**：100 种语言双向翻译
- **配音生成**：语音克隆 + 翻译配音
- **一键部署**：无需复杂环境配置

**支持的平台：**
哔哩哔哩、小红书、抖音、微信视频号、快手、YouTube、TikTok 等

**趋势洞察：** 视频本地化是 AIGC 落地的重要场景。KrillinAI 的"一键全流程"设计降低了内容出海的技术门槛，预计在跨境内容创作者中有强烈需求。

---

### 10. 🛡️ `AikidoSec/safe-chain`

**基本信息**

| 指标 | 数值 |
|------|------|
| ⭐ Stars | 1,007 |
| 🍴 Forks | 47 |
| 🐙 语言 | JavaScript |
| 🔗 链接 | https://github.com/AikidoSec/safe-chain |

**项目描述**

> Protect against malicious code installed via npm, yarn, pnpm, npx, and pnpx with Aikido Safe Chain. Free to use, no tokens required.

**深度分析**

Aikido Safe Chain 是一个免费的 npm/PyPI 供应链安全工具，在包管理器层面阻止恶意代码执行。

**支持的工具链：**
- 📦 npm, npx, yarn, pnpm, pnpx, bun, bunx
- 🐍 pip, pip3, uv, poetry, pipx

**核心防护能力：**
- **阻止 48 小时内的恶意包**：新发布的恶意包往往在 48 小时内被大量植入，Aikido 阻断这个窗口期
- **无需 Token/API Key**：免费使用，降低采纳门槛
- **本地/CI 双覆盖**：保护开发者笔记本和 CI/CD 环境

**趋势洞察：** npm 供应链安全是 2024-2026 年的持续热点。xz-utils 后门等事件让整个行业对供应链攻击高度警惕。Aikido Safe Chain 的"零配置+免费"策略有望获得快速普及。

---

### 11. 🦀 `lance-format/lance`

**基本信息**

| 指标 | 数值 |
|------|------|
| ⭐ Stars | 6,262 |
| 🍴 Forks | 610 |
| 🐙 语言 | Rust |
| 🔗 链接 | https://github.com/lance-format/lance |

**项目描述**

> Open Lakehouse Format for Multimodal AI. Convert from Parquet in 2 lines of code for 100x faster random access, vector index, and data versioning.

**深度分析**

Lance 是一个面向多模态 AI 的开源 Lakehouse 格式，旨在为机器学习数据管理提供现代解决方案。

**核心特性：**
- **多模态支持**：图像、视频、点云、文本等
- **高性能随机访问**：比 Parquet 快 100 倍
- **向量索引**：内置 ANN 向量搜索
- **数据版本控制**：类似 Git 的数据版本管理
- **丰富生态**：Pandas、DuckDB、Polars、PyArrow、PyTorch、Rays、Spark

**技术亮点：**
- Rust 实现确保高性能和内存安全
- 与 Parquet 兼容，迁移成本低
- 向量检索 + 全文搜索一体化

**趋势洞察：** 多模态 AI 时代需要新的数据格式。Lance 定位于"AI Native"的数据湖格式，在 RAG、向量数据库等场景有广泛应用价值。

---

### 12. 🧬 `zai-org/GLM-OCR`

**基本信息**

| 指标 | 数值 |
|------|------|
| ⭐ Stars | 5,203 |
| 🍴 Forks | 452 |
| 🐙 语言 | Python |
| 🔗 链接 | https://github.com/zai-org/GLM-OCR |

**项目描述**

> GLM-OCR: Accurate × Fast × Comprehensive — 新一代多模态 OCR 模型

**深度分析**

GLM-OCR 是智谱 AI 团队开源的多模态 OCR 模型，在 OmniDocBench V1.5 上达到 SOTA（94.62 分）。

**技术架构：**
- **GLM-V 编码器**：基于大规模图文数据预训练的视觉编码器
- **GLM-0.5B 解码器**：轻量级语言解码器
- **MTP Loss**：Multi-Token Prediction 损失函数
- **PP-DocLayout-V3**：两阶段流水线（布局分析 + 并行识别）

**核心优势：**
- 仅 0.9B 参数，却达到 SOTA 水平
- 支持 vLLM、SGLang、Ollama 部署
- 兼容复杂表格、公式、印章等困难场景
- 全量开源，提供完整 SDK

**趋势洞察：** OCR 是企业文档数字化的基础能力。GLM-OCR 的"小模型高精度"策略非常适合生产环境部署，是国产开源 OCR 的重要里程碑。

---

### 13. 🎮 `geode-sdk/geode`

**基本信息**

| 指标 | 数值 |
|------|------|
| ⭐ Stars | 2,146 |
| 🍴 Forks | 403 |
| 🐙 语言 | C++ |
| 🔗 链接 | https://github.com/geode-sdk/geode |

**项目描述**

> The ultimate Geometry Dash modding framework

**深度分析**

Geode 是知名游戏 Geometry Dash 的模块化 Mod 加载器和 SDK，旨在解决 Mod 不兼容问题。

**技术亮点：**
- 完整的 Mod 开发 SDK
- 统一的 Mod 生命周期管理
- 兼容层设计，解决 Mod 间冲突
- 现代化的 Mod 开发体验

**趋势洞察：** 虽然是游戏 Mod 工具，但 Geode 的"兼容层"设计思路对其他生态的 Plugin 系统有参考价值。

---

### 14. 🌐 `axios/axios`

**基本信息**

| 指标 | 数值 |
|------|------|
| ⭐ Stars | 108,993 |
| 🍴 Forks | 11,591 |
| 🐙 语言 | JavaScript |
| 🔗 链接 | https://github.com/axios/axios |

**项目描述**

> Promise based HTTP client for the browser and node.js

**趋势洞察：**

Axios 今日重回 Trending，反映了前端生态的持续活跃。作为最流行的 HTTP 客户端库之一，Axios 依然是 Web 开发的基础设施。

---

### 15. ⚙️ `biomejs/biome`

**基本信息**

| 指标 | 数值 |
|------|------|
| ⭐ Stars | 24,188 |
| 🍴 Forks | 929 |
| 🐙 语言 | Rust |
| 🔗 链接 | https://github.com/biomejs/biome |

**项目描述**

> A toolchain for web projects, aimed to provide functionalities to maintain them. Biome offers formatter and linter, usable via CLI and LSP.

**深度分析**

Biome 是用 Rust 重写的 Web 项目工具链，提供格式化（Formatter）和代码检查（Linter）功能。

**定位对标：**
- ESLint（代码检查）
- Prettier（代码格式化）
- 两者合一的 Rust 实现

**核心优势：**
- 🚀 Rust 实现，速度极快（比 ESLint 快 35 倍）
- 📦 单二进制文件，无需 Node.js 依赖
- 🔌 IDE LSP 集成
- 🎯 兼容 ESLint 配置

**趋势洞察：** Rust 在前端工具链中的渗透持续加速。Biome 代表了"用 Rust 重新发明现代 JS 工具链"的趋势，预计将对 ESLint/Prettier 的市场主导地位形成挑战。

---

### 16. 🤝 `affaan-m/everything-claude-code`

**基本信息**

| 指标 | 数值 |
|------|------|
| ⭐ Stars | 133,262 |
| 🍴 Forks | 19,327 |
| 🐙 语言 | Shell |
| 🔗 链接 | https://github.com/affaan-m/everything-claude-code |

**项目描述**

> The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**深度分析**

Everything Claude Code 是一个 Agent Harness 系统，为多个主流 Coding Agent 提供性能优化、安全增强和研究支持。

**收录成就：**
- 🏆 Anthropic Hackathon 冠军
- 50K+ Stars
- 6K+ Forks
- 7 种语言文档

**趋势洞察：** Coding Agent 的"Harness/Ecosystem"工具正在快速成熟，Everything Claude Code 聚合了多种 Agent 的最佳实践，是 AI Coding 领域的重要知识库。

---

### 17. 🔧 `ComposioHQ/open-claude-cowork`

**基本信息**

| 指标 | 数值 |
|------|------|
| ⭐ Stars | 3,341 |
| 🍴 Forks | 446 |
| 🐙 语言 | JavaScript |
| 🔗 链接 | https://github.com/ComposioHQ/open-claude-cowork |

**项目描述**

> Open Source version of Claude Cowork with 500+ SaaS app integrations

**深度分析**

Open Claude Cowork 是 Composio 推出的开源版 Claude Cowork，支持 500+ SaaS 应用集成。

**核心价值：**
- Claude Code 与 500+ SaaS 工具的桥接
- 开源版本降低了使用门槛
- 支持 GitHub、Slack、Notion 等主流工具

**趋势洞察：** Agent + SaaS 集成是 Agent 落地的重要路径。Composio 通过开源 Cowork 扩大生态影响力。

---

### 18. ⚒️ `antinomyhq/forgecode`

**基本信息**

| 指标 | 数值 |
|------|------|
| ⭐ Stars | 5,676 |
| 🍴 Forks | 1,254 |
| 🐙 语言 | Rust |
| 🔗 链接 | https://github.com/antinomyhq/forgecode |

**项目描述**

> AI enabled pair programmer for Claude, GPT, O Series, Grok, Deepseek, Gemini and 300+ models

**深度分析**

Forge 是一个支持 300+ AI 模型的终端编程 Agent，用 Rust 编写，主打多模型兼容。

**安装方式：**
```bash
curl -fsSL https://forgecode.dev/cli | sh
```

**趋势洞察：** "300+ 模型支持"体现了去中心化 AI 的趋势——不绑定单一提供商，让用户自由选择性价比最高的模型。

---

### 19. 📚 `harvard-edge/cs249r_book`

**基本信息**

| 指标 | 数值 |
|------|------|
| ⭐ Stars | 23,280 |
| 🍴 Forks | 2,776 |
| 🐙 语言 | JavaScript |
| 🔗 链接 | https://github.com/harvard-edge/cs249r_book |

**项目描述**

> Machine Learning Systems — Principles and Practices of Engineering Artificially Intelligent Systems

**深度分析**

哈佛 CS249r 课程配套开源书籍，系统讲解机器学习系统工程（从模型训练到生产部署的完整生命周期）。

**课程模块：**
- TinyTorch（TinyML 框架）
- Labs（实践实验）
- Kits（嵌入式 ML）
- MLSys·im（推理优化）
- Slides（课件资源）
- Instructors（教学材料）

**多语言支持：** 英文、中文、日文、韩文

**趋势洞察：** ML Systems 领域的开源教育资源持续受到重视，反映了 AI 工程化人才需求的增长。

---

## 📊 趋势总结与洞察

### 核心趋势（按热度排序）

| 排名 | 趋势主题 | 代表项目 | 热度评级 |
|------|---------|---------|---------|
| 🥇 | AI Coding Agent | Claude Code, Codex, Forge | ⭐⭐⭐⭐⭐ |
| 🥈 | 多模态 AI 数据基础设施 | Lance, GLM-OCR | ⭐⭐⭐⭐⭐ |
| 🥉 | 供应链安全 | Aikido Safe Chain | ⭐⭐⭐⭐ |
| 4 | AI Agent 框架 | BAML, ADK-Go, PraisonAI | ⭐⭐⭐⭐ |
| 5 | 内容创作工具 | OpenScreen, KrillinAI | ⭐⭐⭐⭐ |
| 6 | AI 研究/教育 | system_prompts_leaks, CS249r | ⭐⭐⭐ |
| 7 | 基础设施工具链 | Biome, Axios | ⭐⭐⭐ |

### 关键洞察

1. **AI Coding Agent 进入生态竞争阶段**：Claude Code 和 OpenAI Codex 的竞争带动了整个 Agent 工具链的发展（SDK、Harness、集成工具）

2. **多模态 AI 数据层崛起**：Lance（存储格式）、GLM-OCR（识别能力）等数据基础设施项目快速增长，反映多模态 AI 应用落地的基础设施需求

3. **开源替代持续热门**：OpenScreen（Screen Studio 替代）、Forge（Claude Code 多模型替代）等开源替代方案有稳定的市场需求

4. **供应链安全意识增强**：Aikido Safe Chain 的出现说明 npm/PyPI 安全已经成为社区共识

5. **Rust 在工具链领域加速渗透**：Biome、Lance、BAML 等 Rust 实现项目体现了 Rust 在性能和可靠性方面的优势

---

## 📋 附录：完整上榜项目清单

| # | 项目 | 语言 | Stars | Forks | 分类 |
|---|------|------|-------|-------|------|
| 1 | anthropics/claude-code | Shell | 106,315 | 17,022 | AI Coding |
| 2 | affaan-m/everything-claude-code | Shell | 133,262 | 19,327 | AI Coding |
| 3 | axios/axios | JavaScript | 108,993 | 11,591 | HTTP Client |
| 4 | sherlock-project/sherlock | Python | 76,956 | 9,045 | Security/OSINT |
| 5 | openai/codex | Rust | 72,565 | 10,158 | AI Coding |
| 6 | asgeirtj/system_prompts_leaks | — | 36,041 | 5,971 | AI Research |
| 7 | biomejs/biome | Rust | 24,188 | 929 | Toolchain |
| 8 | harvard-edge/cs249r_book | JavaScript | 23,280 | 2,776 | Education |
| 9 | siddharthvaddem/openscreen | TypeScript | 15,179 | 1,045 | Media Tools |
| 10 | krillinai/KrillinAI | Go | 9,809 | 861 | Video AI |
| 11 | BoundaryML/baml | Rust | 7,886 | 403 | AI Framework |
| 12 | google/adk-go | Go | 7,376 | 606 | AI Framework |
| 13 | CeuiLiSA/Pixiv-Shaft | Java | 6,824 | 227 | Mobile App |
| 14 | MervinPraison/PraisonAI | Python | 6,290 | 917 | AI Framework |
| 15 | lance-format/lance | Rust | 6,262 | 610 | Data Infra |
| 16 | openMVG/openMVG | C++ | 6,365 | 1,710 | CV/3D |
| 17 | antinomyhq/forgecode | Rust | 5,676 | 1,254 | AI Coding |
| 18 | zai-org/GLM-OCR | Python | 5,203 | 452 | OCR |
| 19 | geode-sdk/geode | C++ | 2,146 | 403 | Game Mod |
| 20 | xororz/local-dream | Kotlin | 1,976 | 126 | Mobile AI |

---

*报告生成时间：2026-04-03 02:00 (Asia/Shanghai)*
*数据来源：GitHub Trending (github.com/trending) + GitHub REST API*
