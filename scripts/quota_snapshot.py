#!/usr/bin/env python3
"""从 Codex 会话 JSONL 里读取额度快照的脱敏摘要。

只输出窗口百分比；不输出会话正文、Token 明细或任何凭据。
字段结构是演练用的通用写法：实际情况请先用 --keys 确认键名，再按需调整 extract_percent。
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Iterator


def find_rate_limits(obj: Any, path: str = "") -> Iterator[tuple[str, dict]]:
    if isinstance(obj, dict):
        for key, value in obj.items():
            here = f"{path}.{key}" if path else key
            if "rate_limit" in key.lower() and isinstance(value, dict):
                yield here, value
            yield from find_rate_limits(value, here)
    elif isinstance(obj, list):
        for index, value in enumerate(obj):
            yield from find_rate_limits(value, f"{path}[{index}]")


def extract_percent(window: Any) -> float | None:
    if not isinstance(window, dict):
        return None
    for key, value in window.items():
        name = key.lower()
        if "remaining" in name and "percent" in name and isinstance(value, (int, float)):
            return float(value)
    return None


def read_snapshots(source: Path) -> list[tuple[str, dict]]:
    found: list[tuple[str, dict]] = []
    with source.open("r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            for path, limits in find_rate_limits(event):
                found.append((path, limits))
    return found


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("jsonl", help="会话 JSONL 文件路径")
    parser.add_argument(
        "--keys",
        action="store_true",
        help="只列出发现的键名（不列值），用于确认实际字段结构",
    )
    args = parser.parse_args()

    source = Path(args.jsonl)
    if not source.is_file():
        parser.error(f"文件不存在：{source}")

    snapshots = read_snapshots(source)
    if not snapshots:
        print("未找到 rate_limits 字段。")
        return 0

    if args.keys:
        for path, limits in snapshots[:5]:
            print(f"{path}: {sorted(limits.keys())}")
        return 0

    percents: list[float] = []
    for path, limits in snapshots[-3:]:
        parts = []
        for window in ("primary", "secondary"):
            value = extract_percent(limits.get(window))
            if value is not None:
                percents.append(value)
                parts.append(f"{window}={value:.1f}%")
        if parts:
            print(f"{source.name}: " + ", ".join(parts))

    if percents:
        print(f"较低窗口剩余：{min(percents):.1f}%（历史快照，不是实时余额）")
    else:
        print("字段存在但没有可解析的百分比；请先用 --keys 确认结构。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
