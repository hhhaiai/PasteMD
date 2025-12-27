---
layout: home

hero:
  name: "PasteMD"
  text: "智能 Markdown 转换工具"
  tagline: 让 AI 对话内容完美粘贴到 Word/WPS，公式不乱码，格式不丢失
  image:
    src: /logo.png
    alt: PasteMD
  actions:
    - theme: brand
      text: 快速开始
      link: /zh/guide/getting-started
    - theme: alt
      text: 什么是 PasteMD？
      link: /zh/guide/what-is-pastemd
    - theme: alt
      text: GitHub
      link: https://github.com/RichQAQ/PasteMD

features:
  - icon: ⚡️
    title: 一键转换
    details: 按下热键（Ctrl+Shift+B），剪贴板中的 Markdown 立即转换并插入到 Word/WPS 光标位置
  - icon: 🎯
    title: 智能识别
    details: 自动识别内容类型（Markdown/HTML/表格）和目标应用，无需手动选择
  - icon: 📐
    title: 公式完美
    details: 正确处理 LaTeX 数学公式，支持粘贴转换（macOS WPS 暂不支持公式直接显示）
  - icon: 📊
    title: 表格保留格式
    details: Excel 粘贴时保留粗体、斜体、删除线、代码等 Markdown 格式
  - icon: 🖥️
    title: 跨平台支持
    details: 支持 Windows 和 macOS，适配 Microsoft Office 和 WPS Office
  - icon: 🎨
    title: 高度可定制
    details: 支持自定义热键、样式模板、Pandoc 过滤器等，满足个性化需求
---

## 为什么选择 PasteMD？

从 ChatGPT、DeepSeek、Kimi 等 AI 网站复制内容到 Word 时，是否遇到这些问题？

- ❌ 数学公式变成乱码
- ❌ Markdown 格式全部丢失
- ❌ 代码块显示混乱
- ❌ 表格格式需要手动调整

**PasteMD 帮你一键解决所有问题！**

## 支持的应用

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0;">
  <div class="feature-card">
    <div style="font-size: 32px; margin-bottom: 8px;">📝</div>
    <h3>Microsoft Word</h3>
    <p>Windows & macOS</p>
  </div>
  <div class="feature-card">
    <div style="font-size: 32px; margin-bottom: 8px;">📄</div>
    <h3>WPS 文字</h3>
    <p>Windows & macOS</p>
  </div>
  <div class="feature-card">
    <div style="font-size: 32px; margin-bottom: 8px;">📊</div>
    <h3>Microsoft Excel</h3>
    <p>Windows & macOS</p>
  </div>
  <div class="feature-card">
    <div style="font-size: 32px; margin-bottom: 8px;">📈</div>
    <h3>WPS 表格</h3>
    <p>Windows & macOS</p>
  </div>
</div>

## 快速开始

:::: code-group
::: code-group-item Windows
```bash
# 下载安装包
# 运行 PasteMD-Setup.exe

# 或使用便携版
# 解压后直接运行 PasteMD.exe
```
:::

::: code-group-item macOS
```bash
# 下载 DMG 文件
# 拖拽到 Applications 文件夹

# 首次运行需要设置权限
# 详见 macOS 指南
```
:::
::::

## 使用流程

1. **启动 PasteMD** - 程序驻留在系统托盘
2. **复制内容** - 从 AI 网站或其他地方复制 Markdown
3. **打开文档** - 在 Word/WPS 中定位光标
4. **按下热键** - 默认 `Ctrl+Shift+B`
5. **完成！** - 内容自动转换并插入

## 特色功能

### 🔬 数学公式支持

自动识别并正确处理 `$...$` 和 `$$...$$` 公式：

```markdown
行内公式：$E = mc^2$

块级公式：
$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

::: warning macOS WPS 用户注意
由于 macOS WPS 暂不支持 AppleScript 自动化，公式会以 LaTeX 代码形式显示（如 `$E=mc^2$` 和 `$$公式$$`），需要手动转换为公式。推荐 macOS 用户使用 Microsoft Word 以获得完美的公式支持。
:::

### 📊 AI 网站兼容性测试

以下是主流 AI 对话网站的复制粘贴兼容性测试结果：

| AI 网站 | 复制 Markdown<br/>（无公式） | 复制 Markdown<br/>（含公式） | 复制网页内容<br/>（无公式） | 复制网页内容<br/>（含公式） |
|---------|:----------------------------:|:----------------------------:|:---------------------------:|:---------------------------:|
| **Kimi** | ✅ 完美支持 | ✅ 完美支持 | ✅ 完美支持 | ⚠️ 无法显示公式 |
| **DeepSeek** | ✅ 完美支持 | ✅ 完美支持 | ✅ 完美支持 | ✅ 完美支持 |
| **通义千问** | ✅ 完美支持 | ✅ 完美支持 | ✅ 完美支持 | ⚠️ 无法显示公式 |
| **豆包** | ✅ 完美支持 | ✅ 完美支持 | ✅ 完美支持 | ✅ 完美支持* |
| **智谱清言/ChatGLM** | ✅ 完美支持 | ✅ 完美支持 | ✅ 完美支持 | ✅ 完美支持 |
| **ChatGPT** | ✅ 完美支持 | ⚠️ 公式显示为代码 | ✅ 完美支持 | ✅ 完美支持 |
| **Gemini** | ✅ 完美支持 | ✅ 完美支持 | ✅ 完美支持 | ✅ 完美支持 |
| **Grok** | ✅ 完美支持 | ✅ 完美支持 | ✅ 完美支持 | ✅ 完美支持 |
| **Claude** | ✅ 完美支持 | ✅ 完美支持 | ✅ 完美支持 | ✅ 完美支持 |

**图例说明：**
- ✅ **完美支持**：格式、样式、公式均正确显示
- ⚠️ **公式显示为代码**：数学公式以 LaTeX 代码形式显示，需在 Word/WPS 中手动使用公式编辑器
- ⚠️ **无法显示公式**：数学公式丢失，需在 Word/WPS 中手动输入公式内容
- **豆包***：复制网页内容（含公式）前，需在浏览器中开启"允许读取剪贴板"权限

**测试环境**：Windows 11 + Microsoft Word 2021

### 📋 表格格式保留

Excel 粘贴时保留所有 Markdown 格式：

| 功能 | 支持 |
|------|------|
| **粗体** | ✅ |
| *斜体* | ✅ |
| ~~删除线~~ | ✅ |
| `代码` | ✅ |

### 🎯 智能兜底模式

即使没有打开 Word/Excel，也可以：
- 自动打开应用
- 仅保存为文件
- 复制富文本到剪贴板
- 或不执行任何操作

## 立即开始使用

<div style="text-align: center; margin: 48px 0;">
  <a href="/zh/guide/getting-started" style="display: inline-block; padding: 12px 32px; background: linear-gradient(135deg, #5f9ea0, #4a8a8c); color: white; border-radius: 8px; text-decoration: none; font-weight: 600; font-size: 16px;">
    查看快速开始指南 →
  </a>
</div>
