# 方向 3 · QQ 智能机器人

**状态**：✅ 公开仓库证据充分 ｜ 🔄 本人参与细节待整理

## 涉及组件

鲸戒、NapCat、SnowLuma、语言风格优化。

## 已验证（公开仓库）

来源：<https://github.com/jiuhuweisi-maker/qq-whale-girl-diary>（2026-11-18 验证 HTTP 200）。

- 架构：DSH + SurfCore 固定版本 + 容器化 QQ 客户端 / OneBot；配置里 `NapCat` 是历史字段名，实际连的是 SnowLuma 的 OneBot 接口。
- 换机流程：`bootstrap.sh` 一条命令构建 + `state-transfer.sh` 迁移私密状态；代码 / 配置 / 状态三层分离。
- 逐文件哈希验收：公开文档记录过构建产物与线上清单 SHA-256 零差异。
- 语言风格优化：公开文档记录了多轮"永久规则下沉到代码层"、真实语料蒸馏、反编造、称呼按场景等改动。
- 事故复盘：一次"不回消息"的根因是内存耗尽叠加上游 API 中断，不是掉线或鉴权失效。

## 待整理

| 项 | 状态 |
| --- | --- |
| 本人亲自运维的现场记录 | 📋 待整理 |
| 语言风格优化的前后对比样例 | 📋 待整理 |
| NapCat 历史阶段的实现细节 | 📋 待整理 |

详见 [007 鲸戒实验记录](../../experiments/007-whale-qq-bot.md) 与 [002 VPS 自动化](../../experiments/002-vps-automation.md)。
