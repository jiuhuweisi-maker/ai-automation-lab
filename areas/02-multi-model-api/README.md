# 方向 2 · 多模型与 API

**状态**：🔄 进行中 ｜ 📋 本人实测数据待整理

## 涉及模型

主人确认接入和使用过：GPT、Gemini、DeepSeek、千问等。

## 可核对的证据

- 本地 **Qwen3-4B-Instruct-2507 Q4_K_M**：冷启动约 3.9 秒、推理约 0.42 秒、进程调用约 4.86 秒；服务器报 93 输入 / 27 输出 Token。见 [003 实验记录](../../experiments/003-multi-agent-collaboration.md) 与 `codex-task-router/VALIDATION.md`（本地文件，不上传）。
- **GPT 系列**：本地模型目录与验收记录中可见 luna / sol 等代号，按任务选择；跨模型交接用目标、证据和少量相关文件。
- **DeepSeek**：公开仓库 [qq-whale-girl-diary](https://github.com/jiuhuweisi-maker/qq-whale-girl-diary) 记录过配置层设计；事故复盘里出现过官方 API 中断。
- **Gemini**：本机存在对应工具目录，但未找到可引用的接入实验记录。

## 待整理

| 项 | 状态 |
| --- | --- |
| GPT / Gemini / DeepSeek / 千问的接入方式对比 | 📋 待整理 |
| 本人实测的成本与质量数据 | 📋 待整理 |
| 路由策略与失败切换的实测效果 | 📋 待整理 |

不填任何没有依据的数字。详见 [006 实验记录](../../experiments/006-multi-model-api.md)。

## 关联

[AI 工具与工作流](../09-tooling/README.md) · [多 Agent 协作](../01-agent-collaboration/README.md) · [证据分层](../../docs/status-and-evidence.md)
