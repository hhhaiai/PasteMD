# 安装

PasteMD 支持 Windows 和 macOS 两个平台，提供多种安装方式。

## 前置要求

### 必需

- **Pandoc**：PasteMD 依赖 Pandoc 进行文档格式转换

### 推荐

- **Microsoft Office** 或 **WPS Office**

## 安装 Pandoc

Pandoc 是 PasteMD 的核心依赖，必须先安装。

### Windows

**方法 1：使用安装包（推荐）**

1. 访问 [Pandoc 官网](https://pandoc.org/installing.html)
2. 下载 Windows 安装包（.msi 文件）
3. 运行安装包，按提示完成安装
4. 重启命令行或终端

**方法 2：使用 Chocolatey**

```bash
choco install pandoc
```

**方法 3：使用 Scoop**

```bash
scoop install pandoc
```

**验证安装**

打开命令提示符或 PowerShell，运行：

```bash
pandoc --version
```

如果显示版本信息，说明安装成功。

### macOS

**方法 1：使用 Homebrew（推荐）**

```bash
brew install pandoc
```

**方法 2：下载安装包**

1. 访问 [Pandoc 官网](https://pandoc.org/installing.html)
2. 下载 macOS 安装包（.pkg 文件）
3. 双击安装

**验证安装**

打开终端，运行：

```bash
pandoc --version
```

::: tip PasteMD 便携版中的 Pandoc
PasteMD 的便携版和 macOS .app 包中已经包含了 Pandoc，无需单独安装。但如果你想使用系统安装的 Pandoc，可以在配置文件中指定路径。
:::

## 安装 PasteMD

### Windows

#### 方法 1：安装程序（推荐）

1. 访问 [GitHub Releases](https://github.com/RichQAQ/PasteMD/releases)
2. 下载最新版本的 `PasteMD-Setup.exe`
3. 运行安装程序，按提示完成安装
4. 安装完成后，从开始菜单启动 PasteMD

**默认安装路径**：`C:\Program Files\PasteMD\`

**开机自启动**：安装时可选择添加到开机启动项

#### 方法 2：便携版

1. 访问 [GitHub Releases](https://github.com/RichQAQ/PasteMD/releases)
2. 下载最新版本的 `PasteMD-Portable.zip`
3. 解压到任意目录
4. 运行 `PasteMD.exe`

**特点**：
- ✅ 无需安装，解压即用
- ✅ 配置文件保存在程序目录
- ✅ 适合 U 盘携带
- ✅ 包含 Pandoc，无需单独安装

### macOS

#### 方法 1：DMG 安装包（推荐）

1. 访问 [GitHub Releases](https://github.com/RichQAQ/PasteMD/releases)
2. 下载最新版本的 `PasteMD-macOS.dmg`
3. 双击 DMG 文件
4. 将 PasteMD.app 拖拽到 Applications 文件夹
5. 从启动台或 Applications 文件夹启动 PasteMD

::: warning 首次运行
macOS 可能会提示"无法打开，因为无法验证开发者"：

1. 打开"系统设置" → "隐私与安全性"
2. 找到 PasteMD 的提示
3. 点击"仍要打开"
4. 再次启动 PasteMD

**或者**使用命令行移除隔离属性：

```bash
xattr -cr /Applications/PasteMD.app
```
:::

#### 权限设置

首次运行时，PasteMD 会提示设置必要的权限：

- **辅助功能**：用于监听全局热键
- **录屏**（仅 macOS 10.15+）：用于检测前台窗口
- **输入监控**：用于模拟按键（WPS 粘贴）
- **自动化**：用于控制 Word/Excel（AppleScript）

详细设置步骤请参考 [macOS 权限设置](/zh/macos/permissions)。

### 从源码安装（开发者）

如果你想从源码运行或参与开发：

#### 1. 克隆仓库

```bash
git clone https://github.com/RichQAQ/PasteMD.git
cd PasteMD
```

#### 2. 创建虚拟环境

```bash
python -m venv .venv
```

#### 3. 激活虚拟环境

**Windows**:
```bash
.venv\Scripts\activate
```

**macOS/Linux**:
```bash
source .venv/bin/activate
```

#### 4. 安装依赖

```bash
pip install -r requirements.txt
```

#### 5. 运行

```bash
python main.py
```

## 首次运行

### Windows

1. 启动 PasteMD
2. 程序会出现在任务栏托盘区（右下角）
3. 右键托盘图标查看菜单

**提示**：
- 配置文件会自动创建在 `~\.pastemd\config.json`
- 日志文件保存在 `~\.pastemd\pastemd.log`

### macOS

1. 启动 PasteMD
2. 程序会出现在菜单栏（右上角）
3. 首次运行会自动打开使用说明页面：[https://pastemd.richqaq.cn/macos](https://pastemd.richqaq.cn/macos)
4. 点击菜单栏图标 → "设置" → "权限" 查看权限状态
5. 按提示设置所有必需权限

**提示**：
- 配置文件保存在 `~/.pastemd/config.json`
- 日志文件保存在 `~/.pastemd/pastemd.log`
- 临时文件使用固定路径（避免重复授权）

## 验证安装

### 1. 检查托盘图标

确认托盘区（Windows）或菜单栏（macOS）中有 📋 图标。

### 2. 测试基本功能

1. 复制以下 Markdown 文本：

```markdown
# 测试标题

这是一段**粗体**和*斜体*文本。

- 列表项 1
- 列表项 2

行内公式：$E = mc^2$
```

2. 打开 Word
3. 按下热键（默认 `Ctrl+Shift+B`）
4. 检查内容是否正确插入

### 3. 检查日志

如果遇到问题：

1. 右键托盘图标 → "查看日志"
2. 检查是否有错误信息

## 更新

### Windows

**安装版**：
1. 下载新版本的安装程序
2. 运行安装程序会自动覆盖旧版本

**便携版**：
1. 下载新版本的 ZIP
2. 解压到新目录或覆盖旧文件
3. 配置文件会自动保留

### macOS

1. 下载新版本的 DMG
2. 退出旧版 PasteMD
3. 覆盖 Applications 文件夹中的 PasteMD.app
4. 重新启动

::: tip 配置迁移
更新不会影响你的配置文件和数据，所有设置都会保留。
:::

## 卸载

### Windows

**安装版**：
1. 控制面板 → 程序和功能
2. 找到 PasteMD
3. 点击卸载

**便携版**：
直接删除程序目录

**清理配置**（可选）：
删除 `%USERPROFILE%\.pastemd` 目录

### macOS

1. 退出 PasteMD
2. 将 `/Applications/PasteMD.app` 移到废纸篓
3. （可选）删除配置文件：
   ```bash
   rm -rf ~/.pastemd
   ```

## 常见安装问题

### Pandoc 未找到

**错误提示**：`Pandoc not found` 或 `pandoc: command not found`

**解决方法**：
1. 确认 Pandoc 已安装：运行 `pandoc --version`
2. 如果未安装，参考上面的"安装 Pandoc"部分
3. 如果已安装但仍报错，在配置文件中指定完整路径：

```json
{
  "pandoc_path": "C:\\Program Files\\Pandoc\\pandoc.exe"  // Windows
  // 或
  "pandoc_path": "/usr/local/bin/pandoc"  // macOS
}
```

### Windows 杀毒软件拦截

某些杀毒软件可能误报 PasteMD。

**解决方法**：
1. 将 PasteMD 添加到白名单
2. 或从源码自行编译

### macOS 无法打开

**错误**：`"PasteMD.app" is damaged and can't be opened`

**解决方法**：

```bash
# 移除隔离属性
xattr -cr /Applications/PasteMD.app

# 或者在系统设置中允许
# 系统设置 → 隐私与安全性 → 仍要打开
```

### macOS 权限问题

详见 [macOS 权限设置](/zh/macos/permissions)。

## 下一步

- [快速开始](/zh/guide/getting-started) - 开始使用 PasteMD
- [配置选项](/zh/config/) - 自定义设置
- [macOS 指南](/zh/macos/) - macOS 用户必读
