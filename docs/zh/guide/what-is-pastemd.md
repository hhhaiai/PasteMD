# 什么是 PasteMD？

PasteMD 是一个跨平台的智能 Markdown 转换工具，专门用于解决从 AI 对话网站（如 ChatGPT、DeepSeek、Kimi 等）复制内容到 Word/WPS 时格式丢失、公式乱码的问题。

## 核心问题

当你从 AI 网站复制带有 Markdown 格式的内容时，直接粘贴到 Word 会遇到：

- **数学公式乱码**：`$E=mc^2$` 变成普通文本，复杂公式完全不可读
- **格式丢失**：粗体、斜体、代码块等格式全部消失
- **表格混乱**：Markdown 表格粘贴后需要手动调整
- **代码显示问题**：代码块没有语法高亮，显示混乱

## PasteMD 的解决方案

PasteMD 提供了一个优雅的解决方案：

1. **一键转换**：按下热键（默认 `Ctrl+Shift+B`），自动完成转换和插入
2. **智能识别**：自动判断剪贴板内容类型和当前应用
3. **格式完美**：数学公式、代码块、表格等完美呈现
4. **无缝集成**：内容直接插入到光标位置，无需手动操作

## 工作原理

```mermaid
graph LR
    A[复制 Markdown] --> B[按下热键]
    B --> C[读取剪贴板]
    C --> D[预处理内容]
    D --> E[Pandoc 转换]
    E --> F[插入到应用]
    F --> G[完成！]
```

PasteMD 的核心流程：

1. **监听热键**：全局监听自定义热键
2. **读取剪贴板**：获取 Markdown、HTML 或文件路径
3. **预处理**：标准化格式、处理公式、清理 HTML
4. **Pandoc 转换**：调用 Pandoc 转换为 DOCX 或 XLSX 格式
5. **应用插入**：通过平台特定的 API 插入到目标应用

## 支持的平台和应用

### Windows

- ✅ Microsoft Word（通过 COM 自动化）
- ✅ Microsoft Excel（通过 COM 自动化）
- ✅ WPS 文字（通过 COM 自动化）
- ✅ WPS 表格（通过 COM 自动化）

### macOS

- ✅ Microsoft Word（通过 AppleScript）
- ✅ Microsoft Excel（通过 AppleScript）
- ✅ WPS 文字（通过剪贴板富文本）
- ✅ WPS 表格（通过剪贴板）

::: tip macOS 特别说明
macOS 版本使用不同的技术方案，需要额外的系统权限。详见 [macOS 指南](/zh/macos/)。
:::

## 主要特性

### 🎯 智能内容识别

自动识别剪贴板内容类型：

- **Markdown 文本**：标准 Markdown 语法
- **HTML 富文本**：从网页复制的内容
- **Markdown 表格**：自动识别并转换为 Excel
- **.md 文件**：从文件管理器复制的文件

### 📐 数学公式完美支持

- 支持行内公式：`$...$`
- 支持块级公式：`$$...$$`
- 自动修复常见 LaTeX 语法问题
- 兼容主流 AI 网站的公式格式

### 📊 表格格式保留

Excel 粘贴时完整保留：

- **粗体**：`**text**`
- *斜体*：`*text*`
- ~~删除线~~：`~~text~~`
- `行内代码`：`` `code` ``
- 代码块：` ```code``` `
- 超链接：`[text](url)`

### 🎨 高度可定制

- 自定义全局热键
- 自定义样式模板（reference DOCX）
- 自定义 Pandoc 过滤器
- 自定义保存目录和文件保留策略
- 多语言支持（中文/英文）

### 🔄 智能兜底模式

当没有检测到目标应用时，可以：

- **自动打开**：自动启动 Word 并插入内容
- **仅保存**：保存为文件到指定目录
- **复制到剪贴板**：转换为富文本复制到剪贴板
- **无操作**：仅显示通知

## 技术架构

PasteMD 采用分层架构设计：

- **展示层**：托盘菜单、热键设置、权限管理界面
- **服务层**：文档生成、表格生成、预处理器、通知服务
- **核心层**：工作流路由、应用检测、剪贴板操作
- **集成层**：Pandoc 集成、平台特定 API

## 依赖

- **Pandoc**：强大的文档转换引擎（必需）
- **Python 3.12+**：运行环境
- **平台特定库**：pywin32（Windows）、pyobjc（macOS）

## 开源协议

PasteMD 基于 [MIT 协议](https://github.com/RichQAQ/PasteMD/blob/main/LICENSE) 开源，你可以自由使用、修改和分发。

## 下一步

- [快速开始](/zh/guide/getting-started) - 立即开始使用 PasteMD
- [安装指南](/zh/guide/installation) - 详细的安装步骤
- [macOS 指南](/zh/macos/) - macOS 特定说明
