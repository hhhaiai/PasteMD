# 配置选项

PasteMD 提供了丰富的配置选项，让你可以根据个人需求定制功能。

## 配置文件位置

### Windows
```
C:\Users\<用户名>\.pastemd\config.json
```

### macOS
```
~/Library/Application Support/PasteMD/config.json
```

## 快速访问

通过托盘菜单快速访问配置文件：

1. 右键点击托盘图标
2. 选择"编辑配置文件"
3. 配置文件会在默认文本编辑器中打开

## 完整配置示例

```json
{
  "hotkey": "<ctrl>+<shift>+b",
  "pandoc_path": "pandoc",
  "reference_docx": null,
  "save_dir": "~/Documents/pastemd",
  "keep_file": false,
  "notify": true,
  "enable_excel": true,
  "excel_keep_format": true,
  "no_app_action": "open",
  "md_disable_first_para_indent": true,
  "html_disable_first_para_indent": true,
  "html_formatting": {
    "strikethrough_to_del": true
  },
  "move_cursor_to_end": true,
  "Keep_original_formula": false,
  "language": "zh",
  "enable_latex_replacements": true,
  "fix_single_dollar_block": true,
  "pandoc_filters": []
}
```

## 配置项详解

### 基础设置

#### `hotkey`
- **类型**：字符串
- **默认值**：`"<ctrl>+<shift>+b"`
- **说明**：全局热键配置

**支持的修饰键**：
- `<ctrl>` - Ctrl 键（macOS 上映射为 Cmd）
- `<shift>` - Shift 键
- `<alt>` - Alt 键（macOS 上为 Option）
- `<cmd>` - 仅 macOS，Command 键
- `<win>` - 仅 Windows，Windows 键

**示例**：
```json
"hotkey": "<ctrl>+<shift>+v"
"hotkey": "<ctrl>+<alt>+m"
"hotkey": "<cmd>+<shift>+b"  // macOS
```

::: tip 建议
使用至少两个修饰键的组合，避免与常用快捷键冲突。
:::

---

#### `language`
- **类型**：字符串
- **默认值**：`"zh"`
- **可选值**：`"zh"` | `"en"`
- **说明**：界面语言设置

切换语言后需要重启应用。

---

#### `notify`
- **类型**：布尔值
- **默认值**：`true`
- **说明**：是否显示系统通知

**通知内容**：
- 操作成功提示
- 错误信息提示
- 应用检测结果

---

### Pandoc 设置

#### `pandoc_path`
- **类型**：字符串
- **默认值**：`"pandoc"`
- **说明**：Pandoc 可执行文件的路径

**默认行为**：从系统 PATH 中查找 `pandoc`

**自定义路径**：
```json
// Windows
"pandoc_path": "C:\\Program Files\\Pandoc\\pandoc.exe"

// macOS
"pandoc_path": "/usr/local/bin/pandoc"

// 相对路径（相对于 PasteMD 可执行文件）
"pandoc_path": "./third_party/pandoc/pandoc"
```

::: warning 注意
Windows 路径中的反斜杠需要转义（使用 `\\`）或使用正斜杠（`/`）。
:::

---

#### `reference_docx` (一般不用)
- **类型**：字符串 | null
- **默认值**：`null`
- **说明**：参考 DOCX 模板文件路径

使用参考模板可以：
- 应用自定义样式（标题、正文、代码等）
- 设置页面布局（页边距、页眉页脚）
- 统一字体和颜色

**示例**：
```json
"reference_docx": "~/Documents/my-template.docx"
"reference_docx": "C:/Users/YourName/template.docx"
```

**创建参考模板**：
1. 在 Word 中创建一个文档
2. 设置所需的样式（标题 1-6、正文、代码等）
3. 保存为 `.docx` 文件
4. 在配置中指定路径

---

#### `pandoc_filters`
- **类型**：字符串数组
- **默认值**：`[]`
- **说明**：自定义 Pandoc 过滤器列表

Pandoc 过滤器是用于扩展或修改转换行为的脚本（Lua、Python 等）。

**示例**：
```json
"pandoc_filters": [
  "mermaid-filter",
  "~/filters/custom-filter.lua"
]
```

详见 [自定义过滤器](/zh/guide/custom-filters)。

---

### 文件管理

#### `save_dir`
- **类型**：字符串
- **默认值**：`"~/Documents/pastemd"`
- **说明**：转换后文件的保存目录

**支持的路径格式**：
- `~` 展开为用户主目录
- 相对路径（相对于配置文件目录）
- 绝对路径

**示例**：
```json
"save_dir": "~/Desktop/PasteMD"
"save_dir": "D:/Work/Documents"
```

---

#### `keep_file`
- **类型**：布尔值
- **默认值**：`false`
- **说明**：转换并插入后是否保留生成的文件

**`false`**：插入后自动删除临时文件
**`true`**：保留文件到 `save_dir` 目录

::: tip 使用场景
- `false`（默认）：日常使用，减少磁盘占用
- `true`：需要归档转换后的文件，或调试问题
:::

---

### Excel 表格设置

#### `enable_excel`
- **类型**：布尔值
- **默认值**：`true`
- **说明**：是否启用 Excel 表格自动粘贴功能

**`true`**：检测到 Markdown 表格且前台应用是 Excel，自动转换为 Excel 格式
**`false`**：不启用 Excel 功能

---

#### `excel_keep_format`
- **类型**：布尔值
- **默认值**：`true`
- **说明**：Excel 粘贴时是否有样式

**保留的格式**（当为 `true` 时）：
- **粗体**：`**text**` → 加粗单元格
- *斜体*：`*text*` → 斜体单元格
- ~~删除线~~：`~~text~~` → 删除线
- `代码`：`` `code` `` → 灰色背景 + 等宽字体
- 超链接：`[text](url)` → 可点击的超链接

**`false`**：仅保留纯文本，不应用格式

---

### 格式化选项

#### `md_disable_first_para_indent`
- **类型**：布尔值
- **默认值**：`true`
- **说明**：Markdown 转换时，禁用第一段格式

---

#### `html_disable_first_para_indent`
- **类型**：布尔值
- **默认值**：`true`
- **说明**：HTML 转换时，禁用第一段格式

---

#### `html_formatting`
- **类型**：对象
- **说明**：HTML 预处理器的格式化选项

**子选项**：

##### `strikethrough_to_del`
- **类型**：布尔值
- **默认值**：`true`
- **说明**：将 `~~` 标签转换为 `<del>` 标签

某些网站使用 `~~` 不会在页面上渲染为删除线，而是显示为普通文本。启用此选项可确保删除线正确显示。

**示例**：
```json
"html_formatting": {
  "strikethrough_to_del": true
}
```

---

#### `move_cursor_to_end` (仅 Windows)
- **类型**：布尔值
- **默认值**：`true`
- **说明**：插入内容后，将光标移到末尾

**`true`**：光标移到插入内容的末尾，方便继续输入
**`false`**：光标保持在插入内容的开头

---

### 数学公式设置

#### `Keep_original_formula`
- **类型**：布尔值
- **默认值**：`false`
- **说明**：保留原始 LaTeX 公式（不转换为 MathML）

**`false`**（默认）：公式转换为 Office MathML，完美显示
**`true`**：公式保留为文本形式，保留 `$...$` 符号，确保个性化使用

**使用场景**：
- 需要在 Word 中手动编辑公式
- 公式转换出现问题时的临时解决方案

---

#### `enable_latex_replacements`
- **类型**：布尔值
- **默认值**：`true`
- **说明**：启用 LaTeX 语法兼容性修复

自动修复 AI 网站输出的非标准 LaTeX 语法，例如：
- `\kern` → `\qquad`（pandoc 不支持 `\kern`）

---

#### `fix_single_dollar_block`
- **类型**：布尔值
- **默认值**：`true`
- **说明**：自动修复单行块级公式

某些 AI 网站将块级公式错误地标记为 `$...$` 而非 `$$...$$`。启用此选项可自动修复。

**识别条件**：
- 公式独占一行
- 使用单个 `$` 包裹
- 公式长度超过阈值

**示例**：
```markdown
# 原始（错误）
$\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$

# 自动修复为
$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

---

### 兜底模式

#### `no_app_action`
- **类型**：字符串
- **默认值**：`"open"`
- **可选值**：`"open"` | `"save"` | `"clipboard"` | `"none"`
- **说明**：当未检测到目标应用时的行为

**选项说明**：

| 值 | 行为 | 适用场景 |
|----|------|----------|
| `open` | 自动打开 Word 并插入内容 | 日常使用（推荐） |
| `save` | 仅保存为文件到 `save_dir` | 批量转换文件 |
| `clipboard` | 转换为富文本并复制到剪贴板 | 粘贴到其他应用 |
| `none` | 仅显示通知，不执行操作 | 仅在特定应用中使用 |

**示例**：
```json
"no_app_action": "save"  // 保存文件，不自动打开
```

---

## 应用配置更改

### 通过修改配置文件

重启 PasteMD 应用

### 通过设置界面或托盘菜单

此方法会自动应用更改，无需重启。

## 故障排查

### 配置文件损坏

1. 检查配置文件的 JSON 语法是否正确
2. 恢复默认配置：
    - 删除配置文件，应用会自动生成默认配置

### 配置不生效

1. 检查日志是否有错误信息
2. 尝试重启应用

## 更多信息

- [高级功能](/zh/guide/custom-filters) - 自定义 Pandoc 过滤器
- [GitHub](https://github.com/RichQAQ/PasteMD) - 源代码和问题反馈
