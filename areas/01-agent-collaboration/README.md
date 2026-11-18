# 方向 1 · AI Agent 协作

**状态**：✅ Codex + Copilot CLI 五次派发已验证 ｜ 🔄 其他组合进行中 ｜ 📋 细节待整理

## 涉及工具

Codex、WorkBuddy、Muse、Copilot CLI。

## 已验证：Codex + Copilot CLI

五次真实派发，有 stdout / stderr / diff / 集成记录可查。端到端一次用了 0.14 AI Credits（单次软上限 30），只改白名单里一个文件，新增一条 Node 测试，集成状态 `integrated_uncommitted`。其余四次分别是只读代码审查、后端路由增加、一个 194 行无依赖 WAV 合成器实现。

细节见 [003 实验记录](../../experiments/003-multi-agent-collaboration.md)。案例定位：**这是一个已验证案例，不是本方向的全部内容**。

## 进行中：Codex + WorkBuddy

主人确认实际使用过。本仓库从查重、内容编写、脱敏审核到链接核验由 WorkBuddy 完成。具体任务交接方式与效果待补充，见 [004](../../experiments/004-codex-workbuddy.md)。**不要改写成 Copilot CLI。**

## 待整理：Muse 相关协作

主人确认使用 / 研究过 Muse。本地未找到 AI 实验日志（只有一个同名游戏快捷方式，无关）。见 [005](../../experiments/005-muse.md) 和社交平台方向的 [08](../08-social/README.md)。

## 共用工作流

- [隔离派发](../../workflows/isolated-dispatch.md)
- [额度守护与接手](../../workflows/quota-handoff.md)
- [真实交接提示模板](../../prompts/bounded-subtask.md)
