# 003 · 多 Agent 协作：工具矩阵与已验证案例

**状态**：✅ Codex + Copilot CLI 五次派发为已验证案例 ｜ ✅ 主人确认使用过 Codex + WorkBuddy ｜ ⚠️ Codex + WorkBuddy 的具体协作记录待补充验证

> 阅读前提见 [证据分层](../docs/status-and-evidence.md)。「没找到日志」不等于「没发生过」，本文不把任何待补充的方向写成已验证结果。

## 目标

研究多个 AI Agent 与模型之间的分工、交接和成本控制。这不是单一工具的实验，而是一个工具矩阵：

| 工具 / 组合 | 状态 | 本文位置 |
| --- | --- | --- |
| Codex | 已使用，路由与额度守护有本地验收记录 | 本文 + [额度工作流](../workflows/quota-handoff.md) |
| Copilot CLI | 已使用，5 次真实派发可查 | 下方「已验证案例」 |
| Codex + WorkBuddy | **已使用，具体协作记录待补充验证** | 下方「待补充方向」，另有 [004](../experiments/004-codex-workbuddy.md) |
| Muse | 主人确认使用 / 研究过，细节待补充 | [005](../experiments/005-muse.md) |
| 多模型 API | 已使用，本人实测数据待补充 | [006](../experiments/006-multi-model-api.md) |

## 已验证案例：Codex + Copilot CLI 五次派发

### 环境

- Codex CLI；Copilot CLI 1.0.112（日志实测版本）；PowerShell 7（`pwsh -NoProfile -File`）
- Git detached sparse worktree，白名单文件；Python 3.12 标准库 + SQLite
- 证据：本机 `AI-Agent-Orchestrator/logs/` 5 份 stdout/stderr、`reports/` 下 diff 与 integration 记录、`codex-task-router/VALIDATION.md`。**这些原文不进本仓库。**

### 实际分工

- Codex：架构、高风险变更、最终审查、测试、集成。依据是全局 `AGENTS.md` 规则。
- Copilot CLI：单个有界子任务，一次一条提示词，只开 `view` / `edit` / `apply_patch`，禁 shell、URL、MCP、二次委派。

### 交接方式

1. 准备：`Invoke-CopilotTask.ps1` 从干净 Git 源建 detached sparse worktree，只放白名单文件。
2. 提示注入：`HANDOFF NOTICE` 作为首段落盘，UTF-8 无损，实测 991 字节。
3. 派发：`Run-CopilotTask.ps1` 一次一个任务，缺 `-DirectoryTrustApproved` 时正确拒绝。
4. 集成：Codex 审 diff、跑测试、确认源未变，才集成；不自动提交、不自动部署。

### 实际结果（可核对）

| 项目 | 实测值 |
| --- | --- |
| 真实派发 | 5 次，日志与 diff 在 `AI-Agent-Orchestrator/logs/` 与 `reports/` |
| 端到端 | `e2e-20261114-130155`：Copilot 1.0.112，模型 GPT-5.6 Luna，退出码 0，AI Credits 0.14，只改白名单里一个文件，新增一条 Node 测试，集成状态 `integrated_uncommitted` |
| 只读审查 | `vps-friend-links-review-20261115`：只读渲染代码，未发现正确性回归，diff 为空 |
| 有界实现 | `jp-friend-backend-20261115` 改 `serve.py` 增加路由；`mv-night-signal-score-20261116` 重写 `tools/score.py`（194 行无依赖 WAV 合成器） |
| 本地推理 | Qwen 冷启动约 3.9 秒，推理约 0.42 秒，进程调用约 4.86 秒；93 输入 / 27 输出 Token |
| 云端对照 | Codex Luna 同任务返回一致；CLI 报 16,156 输入（10,752 缓存）/ 8 输出 Token，含运行上下文，不能直接与本地相减 |
| 额度触发 | 主窗口剩余 1%、周窗口 84%；C 类改派 `route_C_redirected_to_copilot_low_codex_quota`，D 类 `quota_guard_block=true`，云端调用 `not_started` |
| 控制流 | 替身后端三次：低额度 C、低额度 D 各拦截 0 次调用；额度充足 C 恰好 1 次 |
| 预算 | 单次 Copilot 响应软上限 30 AI Credits，端到端实跑用 0.14 |

**成本控制结论**：低额度时 Codex 云端调用被拦截，任务转向本地路线或独立的 GitHub AI Credits 通道。省下的订阅额度**无法精确计量**，拦截次数不能换算成额度。

### 失败经验

- 把验收工具的 PowerShell 5.1 缺 API 误写成生产限制；生产默认 PowerShell 7，改回 `pwsh -NoProfile -File` 后不做替换即通过。
- 验证脚本自身断言写错导致三次假 FAIL：调用次数时序错、`auto_handoff` 是原因字符串不是布尔、`quota_guard_block` 不是通用拦截标记。修断言而不是放宽产品逻辑。
- 关键词路由漏判高风险任务，高风险强制走 D 类。
- 额度快照是历史值，不是实时余额或账单；逐任务精确消耗写「未知」。
- 提示词优化器曾返回无关结果，现在同一任务跨层合计只优化一次，偏题沿用原文。

## 待补充方向：Codex + WorkBuddy

**状态：已使用，具体协作记录待补充验证。**

- 主人确认实际使用过 Codex 与 WorkBuddy 的协作，但本地未找到可直接引用、且适合公开的交接日志或完整任务记录。
- 本仓库从查重、内容编写、脱敏审核到链接核验，由 WorkBuddy 完成——这是当前可核对的一次实际工作，但不代表完整的协作方式。
- 不把这条方向改写成 Copilot CLI，也不把 Copilot CLI 的案例冒充成 WorkBuddy 的案例。
- 待补充：任务如何发起、上下文如何交接、谁负责审查、实际跑过哪些任务、效果如何。详见 [004](004-codex-workbuddy.md)。

## 改进方向

- 📋 收集 Codex + WorkBuddy 的真实交接记录，经确认后再补结果。
- 📋 补充 Muse 与多模型 API 的实验入口内容（[005](005-muse.md)、[006](006-multi-model-api.md)）。
- 📋 扩大有界任务样本量，比较缓存命中前后的质量与成本。
- 📋 把 C / D 路线的用量记账区分为订阅额度与独立 API 账单。

## 关联

- [证据分层](../docs/status-and-evidence.md) · [证据索引](../docs/evidence-index.md)
- 工作流：[额度守护与接手](../workflows/quota-handoff.md) · [隔离派发](../workflows/isolated-dispatch.md)
- 提示词：[真实交接提示](../prompts/bounded-subtask.md)
