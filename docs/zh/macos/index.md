---
layout: doc
---

# macOS 指南

PasteMD 为 macOS 提供了全面支持，但由于平台差异，macOS 版本使用了不同的技术方案，并需要额外的系统权限设置。

::: warning 重要说明
**WPS 文字（macOS）**：公式会以 LaTeX 代码形式显示（如 `$E=mc^2$` 和 `$$公式$$`），需要手动转换为公式。请阅读参考[wps公式处理](/zh/macos/wpslatex)

**Microsoft Word（macOS）**：体验基本和 Windows 版本一致，支持公式。


:::

::: tip 重要提示
如果你是第一次使用 PasteMD，请务必阅读本指南，特别是[权限设置](/zh/macos/permissions)部分。
:::

## 平台差异

### Windows vs macOS

| 特性 | Windows | macOS |
|------|---------|-------|
| Word 插入 / Excel 写入 | COM 自动化 | AppleScript |
| WPS 插入 | COM 自动化 | 剪贴板桥接 |
| 应用检测 | Win32 API | NSWorkspace + Quartz |
| 热键监听 | 系统钩子 | CGEvent Tap |
| 权限需求 | 无需特殊权限 | 需要多项权限 |

### 技术实现

#### Microsoft Word/Excel

使用 **AppleScript** 控制 Office 应用：

```applescript
tell application "Microsoft Word"
    tell active document
        insert file "path/to/file.docx" at selection
    end tell
end tell
```

**特点**：
- ✅ 直接插入到光标位置
- ✅ 保留完整格式
- ✅ 支持复杂的文档结构
- ⚠️ 需要"自动化"权限

#### WPS 文字/表格

使用 **剪贴板桥接** 方案：

1. 生成 DOCX/XLSX 文件
2. 读取文件内容为 HTML/RTF
3. 写入剪贴板（富文本格式）
4. 模拟 `Cmd+V` 粘贴

**特点**：
- ✅ 兼容性好
- ✅ 不需要 AppleScript 支持
- ⚠️ 需要"输入监控"权限
- ⚠️ 格式保留度略低于 AppleScript

## 所需权限

macOS 的沙盒安全机制要求应用获得以下权限：

### 1. **辅助功能** (Accessibility)

**用途**：模拟键盘输入（用于 WPS 粘贴）

**影响**：如果未授权，WPS 自动粘贴将不可用

### 2. **录屏** (Screen Recording)

**用途**：检测前台窗口和应用名称

**系统要求**：macOS 10.15 Catalina 及以上

**影响**：如果未授权，无法自动检测当前应用，可能导致功能异常

### 3. **输入监控** (Input Monitoring)

**用途**：监听全局热键

**影响**：如果未授权，热键将无法工作

### 4. **自动化** (Automation)

**用途**：控制 Microsoft Word/Excel（通过 AppleScript）

**影响**：如果未授权，Office 应用的自动插入/写入功能将不可用

详细的权限设置步骤请参考 [权限设置指南](/zh/macos/permissions)。

## 首次启动

### 自动打开使用说明

首次启动 PasteMD 时，会自动打开在线使用说明页面：

**https://pastemd.richqaq.cn/macos**

这个页面包含：
- macOS 版本的特殊说明
- 权限设置视频教程
- 常见问题解答

### 权限检查

1. 点击菜单栏图标 📋
2. 选择"设置" → "权限"
3. 查看各项权限的状态
4. 点击"打开系统设置"按钮设置权限

::: warning 重要
**所有权限必须全部授予**，否则部分功能将无法正常工作。
:::

## 菜单栏与 Dock

### 菜单栏图标

PasteMD 主要通过**菜单栏**（右上角）交互，而非 Dock。

点击菜单栏图标可以：
- 查看当前热键
- 切换功能开关
- 打开设置窗口
- 检查权限状态
- 查看日志和配置

### Dock 图标

默认情况下，PasteMD **不显示在 Dock** 中，以避免占用空间。

**特殊情况**：
- 打开"设置"窗口时，Dock 图标会临时显示
- 关闭设置窗口后，Dock 图标自动隐藏

### Reopen 事件

如果你在 Dock 中点击 PasteMD 图标（首次启动或临时显示时），会自动打开设置窗口。

## 文件路径

### 配置文件

```
~/Library/Application Support/PasteMD/config.json
```

### 日志文件

```
~/Library/Logs/PasteMD/pastemd.log
```

### 临时文件

PasteMD 使用**固定的临时文件路径**，以避免重复的权限授权：

```
~/Library/Application Support/PasteMD/temp/pastemd_word_insert.docx
~/Library/Application Support/PasteMD/temp/pastemd_excel_insert.applescript
```

::: tip 为什么使用固定路径？
macOS 的自动化权限是基于文件路径的。如果每次使用不同的临时文件名，Office 会不断弹出授权对话框。使用固定路径可以"一次授权，永久有效"。
:::

## 支持的应用

### Microsoft Word

- **版本**：Microsoft 365、Office 2019/2021
- **插入方式**：AppleScript
- **权限需求**：辅助功能、录屏、自动化
- **格式保留**：✅ 完美

### Microsoft Excel

- **版本**：Microsoft 365、Office 2019/2021
- **写入方式**：AppleScript
- **权限需求**：辅助功能、录屏、自动化
- **格式保留**：✅ 完美（支持粗体、斜体、删除线、代码等）

### WPS 文字

- **版本**：WPS Office for Mac
- **插入方式**：剪贴板桥接
- **权限需求**：辅助功能、录屏、输入监控
- **格式保留**：⚠️ 基本格式（粗体、斜体、超链接）

### WPS 表格

- **版本**：WPS Office for Mac
- **插入方式**：剪贴板桥接
- **权限需求**：辅助功能、录屏、输入监控
- **格式保留**：✅ 完美（支持粗体、斜体、删除线、代码等）

## 应用检测

PasteMD 使用以下方法检测前台应用：

### 1. NSWorkspace API

获取当前活动应用的名称：

```python
app_name = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
```

支持检测：
- `Microsoft Word`
- `Microsoft Excel`
- `wpsoffice`（WPS）

### 2. Quartz Window API

获取前台窗口的标题和所有者：

```python
window_list = CGWindowListCopyWindowInfo(...)
```

用于：
- 区分 WPS 文字和 WPS 表格（通过窗口标题）
- 判断文档类型（.doc, .xls, .xlsx 等）

### 检测逻辑

```
1. 获取前台应用名称
2. 如果是 Office 应用 → 识别为 Word/Excel
3. 如果是 WPS → 进一步检查窗口标题
   - 包含 .doc/.docx → WPS 文字
   - 包含 .xls/.xlsx/.et → WPS 表格
4. 如果是表格内容 + 启用了 Excel → Excel 工作流
5. 否则 → Word 工作流
6. 如果未检测到应用 → 兜底工作流
```

## 特有功能

### 权限状态检查

在设置界面中，可以实时查看所有权限的状态：

- ✅ **已授权**：绿色
- ❌ **未授权**：红色
- ⚠️ **未知**：灰色

点击"打开系统设置"可以快速跳转到对应的权限设置页面。

### 多进程检测

macOS 版本使用 **socket-based IPC** 机制，确保只有一个实例运行：

- 如果 PasteMD 已在运行，再次启动会自动打开设置窗口
- 使用 Unix domain socket 通信
- Socket 文件路径：`$TMPDIR/PasteMD.sock`

### 本地化

macOS 版本支持系统级本地化，包括：

- **Info.plist 本地化**：应用名称、权限描述
- **菜单本地化**：根据系统语言显示菜单
- **通知本地化**：系统通知的文本

本地化文件：
```
PasteMD.app/Contents/Resources/zh-Hans.lproj/InfoPlist.strings
PasteMD.app/Contents/Resources/en.lproj/InfoPlist.strings
```

## 已知限制

### 1. Pages/Numbers 不支持

目前仅支持 Microsoft Office 和 WPS Office，不支持 Apple 的 Pages/Numbers。

**原因**：Pages/Numbers 的 AppleScript 支持有限，无法直接插入文档。

### 2. WPS 格式保留度

WPS 表格通过剪贴板粘贴，格式保留度低于 Microsoft Excel。QAQ

**建议**：如果需要完美的格式，推荐使用 Microsoft Excel。

### 3. 权限对话框

首次使用时，可能会弹出多个权限授权对话框，这是 macOS 的安全机制。

**建议**：耐心授予所有权限，后续使用将不再提示。

## 更多资源

- [权限设置详细指南](/zh/macos/permissions)
- [在线使用说明](https://pastemd.richqaq.cn/macos)
