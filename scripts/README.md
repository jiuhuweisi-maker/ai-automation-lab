# 脚本

两个都是标准库实现的小工具，不需要安装依赖。

## `check_repo_hygiene.py`

发布前扫描仓库文本文件，报告疑似私钥、常见密钥前缀、凭据赋值、公网 IP 和本机用户目录绝对路径。

```bash
python scripts/check_repo_hygiene.py
python scripts/check_repo_hygiene.py --path /some/other/dir
```

- 只打印「类型 + 路径 + 行号」，不打印命中内容。
- 退出码 `0` = 无命中，`1` = 有命中需要人工判断。
- 误报处理：如果是规则说明里的示例，改成不完整的占位写法；不要靠加白名单掩盖真实命中。

注意它是辅助工具，不是保证。提交前仍要看一遍暂存区差异。

## `quota_snapshot.py`

从会话 JSONL 中读取额度快照摘要，只输出窗口百分比。

```bash
python scripts/quota_snapshot.py /path/to/session.jsonl
python scripts/quota_snapshot.py /path/to/session.jsonl --keys
```

- 不输出会话正文、Token 明细或凭据。
- `--keys` 只列键名，用来确认实际字段结构。
- 字段解析函数是演练用的通用写法；如果实际结构不同，先跑 `--keys` 再调整 `extract_percent`。
- 输出的是服务端历史快照，不是实时余额，也不是账单。

## 测试状态

✅ 两个脚本均已在本机 Python 3.13 上实际运行通过；`quota_snapshot.py` 使用合成 JSONL 验证。
