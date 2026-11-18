# AI 自动化实验室

这是我个人的 **AI 自动化与多模型实践中心**——记录真实使用和研究过的工具与方向，不局限于当前机器上有日志的项目。

覆盖：AI Agent 协作、多模型 API、QQ 智能机器人、VPS 自动化、AI 网站开发、视频自动剪辑、图像与音乐创作、社交平台自动化、AI 工具与工作流。

> 三条纪律：**没找到日志不等于没发生**；**用过不等于验证过结果**；**A 工具的记录不写成 B 工具的成果**。

## English

A personal center for AI automation and multi-model practice: agent collaboration, model APIs, a QQ bot, VPS operations, AI-assisted web design, video editing, image/music creation, social automation, and tooling. Each area is labeled verified / in progress / to be organized. Evidence and personal experience are recorded separately, without inventing results.

## 状态定义

| 状态 | 含义 |
| --- | --- |
| ✅ **已验证** | 有公开仓库提交 / 文档 / 本地日志可核对，可写具体步骤与数值 |
| 🔄 **进行中** | 确认在持续使用，有部分证据，细节待补 |
| 📋 **待整理** | 确认使用过，但没有可公开引用的记录，只写入口不编结果 |

完整规则见 [状态与证据纪律](docs/status-and-evidence.md)。

## 九大方向

| # | 方向 | 状态 | 入口 |
| --- | --- | --- | --- |
| 1 | AI Agent 协作 | ✅ / 🔄 | [Codex · WorkBuddy · Muse · Copilot CLI](areas/01-agent-collaboration/README.md) |
| 2 | 多模型与 API | 🔄 | [GPT · Gemini · DeepSeek · 千问](areas/02-multi-model-api/README.md) |
| 3 | QQ 智能机器人 | ✅ / 🔄 | [鲸戒 · NapCat · SnowLuma · 语言风格](areas/03-qq-bot/README.md) |
| 4 | VPS 自动化 | 🔄 | [部署 · 运维 · 监控 · 故障排查](areas/04-vps/README.md) |
| 5 | AI 网站开发 | ✅ | [Bistro's Tavern](areas/05-website/README.md) |
| 6 | AI 视频自动剪辑 | ✅ / 📋 | [CS2 Montage · 卡点 · 渲染](areas/06-video/README.md) |
| 7 | AI 图像与音乐 | 🔄 | [像素角色 · 动画素材 · Suno BGM](areas/07-image-music/README.md) |
| 8 | 社交平台自动化 | 📋 | [Muse · X 内容发现与运营](areas/08-social/README.md) |
| 9 | AI 工具与工作流 | ✅ | [Skills · MCP · 提示词 · 成本](areas/09-tooling/README.md) |

## 实验记录（编号）

原有分类全部保留，按主题也可从上面九大方向进入。

| # | 实验 | 状态 |
| --- | --- | --- |
| [001](experiments/001-bistros-tavern-site.md) | Bistro's Tavern 网站开发 | ✅ 已上线，Actions 未启用 |
| [002](experiments/002-vps-automation.md) | VPS 有状态服务部署 | 🔄 方法可查，精确参数待补 |
| [003](experiments/003-multi-agent-collaboration.md) | 多 Agent 工具矩阵 + Codex/Copilot 案例 | ✅ 五 case 已验证 |
| [004](experiments/004-codex-workbuddy.md) | Codex + WorkBuddy | 🔄 已使用，记录待补 |
| [005](experiments/005-muse.md) | Muse | 📋 待整理 |
| [006](experiments/006-multi-model-api.md) | 多模型 API | 🔄 实测数据待补 |
| [007](experiments/007-whale-qq-bot.md) | 鲸戒 QQ 机器人 | ✅ 公开证据充分 |
| [008](experiments/008-cs2-trend-video.md) | CS2 价格走势视频 | ✅ 已验证 |
| [009](experiments/009-ifish-concept-film.md) | IFISH 概念片 | ✅ 已验证 |
| [010](experiments/010-codex-environment-audit.md) | Codex 环境与工具链审计 | ✅ 已验证 |

**关于 003**：Codex + Copilot CLI 的五次派发是**一个已验证案例**，属于方向 1 的一部分，不是整个实验室或整个多 Agent 方向的唯一内容，也不代表 Codex + WorkBuddy 的方式。

## 目录

| 目录 | 内容 |
| --- | --- |
| `areas/` | 九大方向的主题入口 |
| `experiments/` | 编号实验记录 |
| `workflows/` | 可复用流程 |
| `prompts/` | 脱敏提示词模板 |
| `scripts/` | 无密钥小工具 |
| `docs/` | 状态纪律、证据索引、公开边界、许可证、变更预览 |

## 公开边界

公开方法论、结构、脱敏示例和已验证结论；不公开凭据、代理节点、服务器地址、账号、私人记忆或个人数据。详见 [公开边界](docs/publication-boundary.md) 与 [证据索引](docs/evidence-index.md)。

## 许可证

MIT，见 [LICENSE](LICENSE)。

## 关联

- 网站：[Bistro's Tavern](https://jiuhuweisi.me)
- 网站源码：[jiuhuweisi-maker.github.io](https://github.com/jiuhuweisi-maker/jiuhuweisi-maker.github.io)
