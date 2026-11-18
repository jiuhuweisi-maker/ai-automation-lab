# 方向 5 · AI 网站开发

**状态**：✅ 已验证

## 项目

[Bistro's Tavern](https://jiuhuweisi.me) — 像素风个人主页，AI 辅助设计、开发与互动系统。

## 已验证

- 技术栈：Astro + TypeScript + 手写 CSS；GitHub Pages 从 `/docs` 发布；自定义域名。
- 内容数据化：项目卡、社交链接、伙伴立绘、首屏插画都由数据文件驱动，改数据不动组件。
- 互动系统：伙伴卡点击抽台词、头图轻量图层（暖灯光晕、月亮呼吸、Zzz 上浮、桌面高光）、随机星点 ±3px 鼠标视差；`prefers-reduced-motion` 下全部停用。
- 部署 V1 与未启用的 Actions 模板分开记录，不把"写好配置"写成"已自动部署"。
- 站点与 6 个 GitHub 链接在 2026-11-18 逐一核验。

完整细节见 [001 实验记录](../../experiments/001-bistros-tavern-site.md)，源码见 <https://github.com/jiuhuweisi-maker/jiuhuweisi-maker.github.io>。

## 待整理

后续可扩展：图片格式自动选择、构建期字段校验、Actions 自动部署切换。📋 待整理。
