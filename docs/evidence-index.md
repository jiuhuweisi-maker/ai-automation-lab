# 证据索引

结论对应可核对来源。**公开链接已逐一验证**（2026-11-18）。本地证据只列文件名与结论，不上传私有日志原文。

先读 [状态与证据纪律](status-and-evidence.md)：没日志不等于没发生，但用过不等于验证过结果。

## 一、公开链接核验

| 链接 | 用途 | 结果 |
| --- | --- | --- |
| <https://jiuhuweisi.me/> | 方向 5 站点 | 网页抓取成功，标题 `jiuhuweisi-maker.github.io \| Bistro`；本机 curl 返回 000 是代理环境所致；`www` 子域不可用 |
| <https://github.com/jiuhuweisi-maker/jiuhuweisi-maker.github.io> | 方向 5 源码 | HTTP 200 |
| <https://github.com/jiuhuweisi-maker/qq-whale-girl-diary> | 方向 3 / 4 | HTTP 200 |
| <https://github.com/jiuhuweisi-maker/cs2-skin-price-trend> | 方向 6 / 实验 008 | HTTP 200 |
| <https://github.com/jiuhuweisi-maker/IFISH-v5> | 方向 6 / 7 / 实验 009 | HTTP 200 |
| <https://github.com/jiuhuweisi-maker/dsh-prompt-kit> | 方向 9 / 提示词 | HTTP 200 |
| <https://github.com/jiuhuweisi-maker/proxy-tun-loop-postmortem> | 方向 4 CRLF 坑 | HTTP 200 |

## 二、按方向列证据

| 方向 | 证据 | 状态 |
| --- | --- | --- |
| 1 Agent 协作 | 本地 `AI-Agent-Orchestrator/logs/` 5 份日志 + `reports/` diff + `codex-task-router/VALIDATION.md` | ✅ Copilot 案例；🔄 WorkBuddy；📋 Muse |
| 2 多模型 API | 本地验收记录（Qwen 时延 / Token）；公开仓库 DeepSeek 配置层设计；本机 `~/.gemini` 目录存在但无实验记录 | 🔄 进行中 |
| 3 QQ 机器人 | `qq-whale-girl-diary` 的 `README.md`、`FRESH-SERVER.md`、事故复盘、补丁文档 | ✅ 项目级；📋 本人运维细节 |
| 4 VPS | `FRESH-SERVER.md`、`INCIDENT-2026-11-07-MEMORY-EXHAUSTION.md`、`deploy/README.md` | 🔄 方法可查，参数待补 |
| 5 网站 | `jiuhuweisi-maker.github.io` 的 `README.md`、`deploy-workflow.yml`、提交历史 | ✅ 已验证 |
| 6 视频 | `cs2-skin-price-trend/README.md`、`IFISH-v5/README.md` 及 `work/qa/` | ✅ 已验证；📋 卡点细节 |
| 7 图像音乐 | IFISH 生图素材与 `native_prompts_v5.json`；网站像素素材；本地 WAV 合成器任务日志 | 🔄 进行中；📋 Suno |
| 8 社交自动化 | 无适合公开的记录 | 📋 待整理 |
| 9 工具工作流 | `codex-environment-audit-20261115/审计报告.md`；公开 `dsh-prompt-kit` | ✅ 已验证 |

## 三、本地证据明细（不上传原文）

| 来源 | 支撑结论 |
| --- | --- |
| `logs/e2e-20261114-130155.*` | Copilot 1.0.112、模型选择、退出码 0、Credits 0.14、白名单单文件改动 |
| `logs/vps-friend-links-review-20261115.*` | 只读审查，无正确性回归，diff 为空 |
| `logs/jp-friend-backend-20261115.*` | 后端路由增加 |
| `logs/mv-night-signal-score-20261116.*` | 194 行无依赖 WAV 合成器 |
| `reports/*` | diff、集成状态 `integrated_uncommitted` |
| `codex-task-router/VALIDATION.md` | 本地推理时延、Token 对照、额度控制流 |
| `codex-environment-audit-20261115/审计报告.md` | Skills 101 / MCP 7 / 工具效率 / Token 口径 |
| `~/AI-Agent-Orchestrator/AGENTS.md` | Codex 与 Copilot 分工规则 |

## 四、脱敏原则

- 公开仓库事实可引用，但 IP、QQ 号、群号、票、密钥、代理节点不复制进本仓库。
- 本地日志只提炼结论，不上传 stdout / stderr / diff 原文。
- 没有可核对记录的数字写「待补充」，不写近似值。
- 状态按证据给，不由叙述便利决定。

## 五、复核记录

- 2026-11-18：敏感扫描 0 命中；7 个公开链接逐一核验。
