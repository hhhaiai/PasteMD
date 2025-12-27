# PasteMD VitePress 文档

## ✨ 已完成

我已为 PasteMD 创建了一个完整的 VitePress 文档站点，风格类似 Pinia，具有以下特性：

### 🎨 设计特点

- **淡蓝色主题**：主色调 `#5f9ea0` (Cadet Blue)，清新优雅
- **响应式布局**：完美适配桌面和移动设备
- **深色模式支持**：自动适配系统主题
- **中英文双语**：完整的国际化支持

### 📁 文档结构

```
docs/
├── .vitepress/
│   ├── config.ts              # 主配置（中英文导航、侧边栏）
│   └── theme/
│       ├── index.ts           # 主题入口
│       └── custom.css         # 自定义样式（淡蓝色主题）
├── public/
│   └── logo.svg               # Logo 图标
├── zh/                        # 中文文档
│   ├── index.md               # 首页
│   ├── guide/                 # 指南
│   │   ├── what-is-pastemd.md
│   │   ├── getting-started.md
│   │   ├── installation.md
│   │   └── markdown-conversion.md
│   ├── macos/                 # macOS 专题
│   │   ├── index.md
│   │   └── permissions.md
│   └── config/                # 配置
│       └── index.md
├── en/                        # 英文文档
│   ├── index.md
│   ├── guide/
│   │   ├── what-is-pastemd.md
│   │   └── getting-started.md
│   ├── macos/
│   │   └── index.md
│   └── config/
│       └── index.md
├── package.json
├── README.md
└── .gitignore
```

### 📚 已创建的文档

#### 中文文档
- ✅ 首页（Hero + Features + 快速开始）
- ✅ 什么是 PasteMD？
- ✅ 快速开始（详细使用流程 + 示例）
- ✅ 安装指南（Windows/macOS + Pandoc）
- ✅ Markdown 转换（完整语法支持说明）
- ✅ macOS 指南（平台差异 + 技术实现）
- ✅ macOS 权限设置（详细的 4 项权限说明）
- ✅ 配置选项（完整配置参考 + 示例）

#### 英文文档
- ✅ 首页
- ✅ What is PasteMD?
- ✅ Getting Started
- ✅ macOS Guide
- ✅ Configuration

### 🎯 核心功能

1. **中英文切换**：顶部导航栏语言切换器
2. **搜索功能**：本地全文搜索（中英文独立索引）
3. **导航系统**：
   - 指南（Guide）
   - macOS 专题（独立导航项）
   - 配置（Config）
   - API（预留）
4. **自定义组件**：
   - Feature 卡片（带 hover 效果）
   - Info 卡片（用于提示信息）
   - Platform Badge（平台标识）

## 🚀 使用方法

### 1. 安装依赖

```bash
cd docs
npm install
```

### 2. 本地开发

```bash
npm run dev
```

访问 http://localhost:5173 预览文档。

### 3. 构建生产版本

```bash
npm run build
```

构建输出在 `docs/.vitepress/dist/` 目录。

### 4. 预览构建结果

```bash
npm run preview
```

## 📦 部署

### 部署到 GitHub Pages

1. 在项目根目录创建 `.github/workflows/deploy.yml`：

```yaml
name: Deploy VitePress

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0

      - name: Setup Node
        uses: actions/setup-node@v3
        with:
          node-version: 18

      - name: Install dependencies
        working-directory: docs
        run: npm install

      - name: Build
        working-directory: docs
        run: npm run build

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: docs/.vitepress/dist
```

2. 在 GitHub 仓库设置中启用 GitHub Pages，选择 `gh-pages` 分支。

### 部署到 Vercel

1. 导入 GitHub 仓库到 Vercel
2. 配置构建设置：
   - **Root Directory**: `docs`
   - **Build Command**: `npm run build`
   - **Output Directory**: `.vitepress/dist`

### 部署到 Netlify

1. 在项目根目录创建 `netlify.toml`：

```toml
[build]
  base = "docs"
  command = "npm run build"
  publish = ".vitepress/dist"
```

2. 连接 GitHub 仓库到 Netlify。

## 🎨 自定义主题

### 颜色配置

在 `docs/.vitepress/theme/custom.css` 中修改主色调：

```css
:root {
  --vp-c-brand-1: #5f9ea0;  /* 主色调 */
  --vp-c-brand-2: #4a8a8c;  /* 深一级 */
  --vp-c-brand-3: #3a7577;  /* 更深 */
}
```

### Logo 替换

替换 `docs/public/logo.svg` 为你的 Logo 图标。

## 📝 继续完善

你可以继续添加以下内容：

### 建议添加的页面

1. **指南部分**：
   - `html-richtext.md` - HTML 富文本转换
   - `excel-tables.md` - Excel 表格功能
   - `math-formulas.md` - 数学公式详解
   - `custom-filters.md` - 自定义 Pandoc 过滤器
   - `hotkeys.md` - 热键配置
   - `fallback-mode.md` - 兜底模式

2. **macOS 部分**：
   - `technical.md` - 技术实现细节
   - `faq.md` - 常见问题

3. **配置部分**：
   - `basic.md` - 基础配置
   - `pandoc.md` - Pandoc 配置
   - `formatting.md` - 格式化选项

4. **API 部分**：
   - `index.md` - API 概览
   - `workflows.md` - 工作流 API
   - `services.md` - 服务 API
   - `utils.md` - 工具函数

5. **其他**：
   - `contributing.md` - 贡献指南
   - `changelog.md` - 更新日志

## 💡 使用建议

1. **图片资源**：将项目中的演示 GIF、截图等放到 `docs/public/` 目录
2. **多媒体**：可以嵌入 YouTube 视频、Bilibili 视频教程
3. **交互示例**：使用 VitePress 的代码组支持创建可切换的代码示例
4. **API 文档**：可以使用 TypeDoc 自动生成 API 文档并集成

## 🔗 相关链接

- [VitePress 官方文档](https://vitepress.dev/)
- [VitePress 主题定制](https://vitepress.dev/guide/custom-theme)
- [Pinia 文档示例](https://pinia.vuejs.org/)

---

**祝你的文档站点大获成功！** 🎉
