#!/usr/bin/env python3
"""扫描仓库文本文件里的疑似敏感信息。

只输出「类型 + 路径 + 行号」，不打印命中内容本身，避免把秘密复制到终端日志。
这是辅助检查，不是保证；提交前仍需人工看 git diff --cached。
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# 拼接构造，避免规则文本被规则自身命中
_PRIVATE_KEY_HEAD = "-----BEGIN " + "PRIVATE KEY-----"

SKIP_DIRS = {
    ".git", ".venv", "venv", "node_modules", "dist", "build",
    "__pycache__", ".state", ".pytest_cache", ".mypy_cache",
}
SKIP_SUFFIXES = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".ico", ".svg",
    ".pdf", ".7z", ".zip", ".tar", ".gz", ".woff", ".woff2", ".ttf",
    ".eot", ".mp3", ".mp4", ".pyc", ".exe", ".dll",
}

PATTERNS = [
    ("私钥头部", re.compile(re.escape(_PRIVATE_KEY_HEAD))),
    ("OpenAI 风格密钥", re.compile(r"\bsk-[A-Za-z0-9_-]{16,}")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}")),
    ("GitHub 细粒度 token", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}")),
    ("Slack token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}")),
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}")),
    (
        "凭据赋值",
        re.compile(
            r"(?i)\b(api[_-]?key|access[_-]?token|secret|password|passwd)"
            r"\s*[:=]\s*[\"']?[A-Za-z0-9_/+.-]{8,}"
        ),
    ),
    ("本机用户目录绝对路径", re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+")),
]

IPV4 = re.compile(
    r"\b(?:(?:25[0-5]|2[0-4]\d|1?\d?\d)\.){3}"
    r"(?:25[0-5]|2[0-4]\d|1?\d?\d)\b"
)
SAFE_IPS = {"127.0.0.1", "0.0.0.0", "255.255.255.255", "8.8.8.8", "1.1.1.1"}


def iter_text_files(root: Path):
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() in SKIP_SUFFIXES:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def scan_file(path: Path) -> list[tuple[str, int]]:
    hits: list[tuple[str, int]] = []
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return hits

    for lineno, line in enumerate(text.splitlines(), 1):
        for name, pattern in PATTERNS:
            if pattern.search(line):
                hits.append((name, lineno))
        if any(ip not in SAFE_IPS for ip in IPV4.findall(line)):
            hits.append(("公网 IP 地址", lineno))
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--path",
        default=str(Path(__file__).resolve().parent.parent),
        help="要扫描的目录，默认是仓库根目录",
    )
    args = parser.parse_args()

    root = Path(args.path).resolve()
    if not root.is_dir():
        parser.error(f"目录不存在：{root}")

    scanned = 0
    total = 0
    for path in iter_text_files(root):
        scanned += 1
        rel = path.relative_to(root)
        for name, lineno in scan_file(path):
            total += 1
            print(f"[{name}] {rel}:{lineno}")

    print(f"扫描 {scanned} 个文本文件，命中 {total} 处。")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
