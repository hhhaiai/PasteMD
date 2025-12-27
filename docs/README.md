# PasteMD 文档

本目录包含 PasteMD 的 VitePress 文档站点。

## 开发

### 安装依赖

```bash
cd docs
npm install
```

### 本地预览

```bash
npm run dev
```

访问 http://localhost:5173

### 构建

```bash
npm run build
```

构建输出在 `.vitepress/dist` 目录。

### 预览构建结果

```bash
npm run preview
```

## 文档结构

```
docs/
├── .vitepress/           # VitePress 配置
│   ├── config.ts         # 主配置文件
│   └── theme/            # 自定义主题
│       ├── index.ts      # 主题入口
│       └── custom.css    # 自定义样式
├── public/               # 静态资源
│   └── logo.svg          # Logo
├── zh/                   # 中文文档
│   ├── index.md          # 首页
│   ├── guide/            # 指南
│   ├── macos/            # macOS 专题
│   ├── config/           # 配置文档
│   └── api/              # API 文档
└── en/                   # 英文文档
    └── ...               # 与中文结构相同
```

## 主题

使用淡蓝色主题，颜色配置：

- 主色调: `#5f9ea0` (Cadet Blue)
- 深色: `#3a7577`
- 浅色: `#7fb3b5`

## 贡献

欢迎改进文档！请提交 Pull Request 到主仓库。
