# 工作流：静态站发布（V1）

来源：[实验 001](../experiments/001-bistros-tavern-site.md)。状态：✅ 当前线上采用此方式；Actions 方式未启用。

## 当前做法（`docs/` 静态发布）

```bash
npm ci
npm run check
npm run build
rm -rf docs && cp -r dist docs && touch docs/.nojekyll
git add -A && git commit -m "Update site" && git push origin main
```

GitHub Pages 的 Source 设为 `main` 分支的 `/docs` 目录。

## 三个容易踩的点

1. **`.nojekyll` 必须有**，否则 `_astro/` 里的 CSS 和字体不会被正确发布。
2. **CNAME 要放三处**：仓库根、`public/`、`docs/`。少放一处，自定义域名可能被清掉。
3. **安装依赖用 `npm ci`**，让锁文件真正生效。

## 备用做法（Actions 自动构建，尚未启用）

根目录 `deploy-workflow.yml` 保存了等价配置：checkout → setup Node → `npm ci` → build → 上传 artifact → 发布 Pages。

启用条件：先给 GitHub CLI token 补 `workflow` scope，然后把文件复制到 `.github/workflows/deploy.yml`，最后在仓库设置里把 Pages 的 Source 改成 GitHub Actions。

**注意：配置文件已经写好，但这一步还没做。** 不要把它描述成已经自动部署。

## 适用边界

这个流程针对"构建产物是纯静态文件、仓库规模小、发布频率不高"的场景。如果以后需要预览部署、多环境或更频繁的发布，再评估切换。
