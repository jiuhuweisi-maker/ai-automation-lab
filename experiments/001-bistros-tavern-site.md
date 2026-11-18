# 001 · Bistro's Tavern：AI 辅助网站开发

**状态**：✅ 站点已上线，提交历史与部署配置可查 ｜ ⚠️ Actions 自动部署仅写好配置，未启用

## 目标

给 Bistro's Tavern 做一个像素风个人主页，作为后续自动化实验的展示入口。硬约束：纯静态、免费托管、内容更新足够简单，不用每次改 HTML。

## 环境

- Astro + TypeScript + 手写 CSS，Node.js 由 Actions 配置指定 22.22.2
- GitHub Pages：`main` 分支的 `/docs` 目录；自定义域名 `jiuhuweisi.me`
- 本地命令：`npm ci` / `npm run dev` / `npm run build` / `npm run preview` / `npm run check`
- 源码：<https://github.com/jiuhuweisi-maker/jiuhuweisi-maker.github.io>（2026-11-18 验证 HTTP 200）

## 实际步骤

1. 初始化 Astro 项目，把 TypeScript 检查纳入 `npm run check`，构建产物进 `dist/`。
2. **内容数据化**：`src/data/projects.ts` 的 `projects` 数组驱动卡片；没有公开地址的项目省略 `url` / `repo`，显示「暂无公开链接」而不是假按钮。图标走 `src/data/icons.ts` 的 12×12 像素精灵，构建时校验尺寸。
3. **社交与伙伴**：`site.ts` 只放真实存在的地址；`companions.ts` 管立绘路径与点击台词，立绘缺失时回退问号占位卡。
4. **首屏**：桌面与手机分别用 `tavern-hero.webp` / `tavern-hero-sm.webp`；主视觉 eager 加载，其余图片 lazy。
5. **部署 V1**：`npm run build` 后把 `dist` 复制到 `docs`，加 `docs/.nojekyll`，由 Pages 从 `/docs` 发布。根目录、`public/`、`docs/` 三处都保留 CNAME。
6. **轻量动效**：CSS 叠层做暖灯光晕、月亮呼吸、Zzz 上浮、桌面高光；星点由布局生成并做 ±3px 鼠标视差。不引入视频、不加新依赖；`prefers-reduced-motion: reduce` 下全部停用。
7. **工作流模板**：Actions 版配置存在根目录 `deploy-workflow.yml`（checkout → setup Node → `npm ci` → build → 上传 artifact → 发布 Pages）。

## 实际结果

- 站点已上线。`https://jiuhuweisi.me/` 在 2026-11-18 用网页抓取确认可访问，页面标题为 `jiuhuweisi-maker.github.io | Bistro`。`www` 子域不可用，不作为入口。
- 提交顺序（公开仓库可查）：初始化 → 加 CNAME → 构建 Astro 首页 → 发布 `docs/` 静态产物 → 关闭 Jekyll 并保留 Actions 模板 → 记录 V1 部署方式 → 加入头图动效。
- 新增项目卡只需改 `projects.ts`，页面自动同步；动效未新增运行时依赖。
- **未做到**：Actions 自动部署没有启用。`deploy-workflow.yml` 在仓库根目录，不在 `.github/workflows/`。

## 失败经验

- GitHub CLI 的 OAuth token 缺 `workflow` scope，推不进 `.github/workflows/`。写完 workflow 文件不等于启用了自动部署，V1 因此退回 `docs/` 静态发布。
- `/docs` 发布必须带 `.nojekyll`，否则 `_astro/` 里的 CSS 和字体发布不正确。
- 手机端头图裁成正方形后动效图层坐标错位，需要在 640px 断点按 16:9 原画布重新对齐。
- 早期给没有公开地址的项目也放按钮，产生假链接；改成按字段有无决定渲染。
- 本机 `curl` 访问自定义域名返回 000、DNS 解析到非公网段，是本机代理环境所致；改用网页抓取得到 200。排查线上可用性时要分清「本机网络问题」和「站点故障」。

## 改进方向

- 📋 执行 `gh auth refresh -h github.com -s workflow`，把 Pages 的 Source 切到 GitHub Actions，启用已备好的工作流。
- 📋 给 `projects.ts` 加更严格的构建期字段校验。
- 📋 首屏图片按浏览器能力自动选 WebP / AVIF。

## 证据与链接

- 站点：<https://jiuhuweisi.me> — 2026-11-18 网页抓取可访问
- 源码：<https://github.com/jiuhuweisi-maker/jiuhuweisi-maker.github.io> — 2026-11-18 HTTP 200
- 依据文件：仓库内 `README.md`（含当前部署状态 V1）、`deploy-workflow.yml`、`docs/.nojekyll`
- 链接核验汇总见 [证据索引](../docs/evidence-index.md)
