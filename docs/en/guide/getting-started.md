# Getting Started

This guide will help you start using PasteMD in minutes.

## Basic Workflow

Using PasteMD is as simple as four steps:

### 1️⃣ Launch the App

After downloading and installing PasteMD, launch the application. It will automatically reside in the system tray.

**Windows**: Look for the 📋 icon in the taskbar (bottom-right)
**macOS**: Look for the 📋 icon in the menu bar (top-right)

### 2️⃣ Copy Markdown Content

Copy Markdown-formatted content from anywhere, such as:

- AI conversation websites (ChatGPT, DeepSeek, Kimi, etc.)
- Markdown editors
- GitHub, blog posts
- Local `.md` files

::: tip Supported Content Types
- Plain Markdown text
- HTML rich text (copied from web pages)
- Markdown tables
- `.md` files (copied from file manager)
:::

### 3️⃣ Open Target Application

Open one of the following applications and position your cursor where you want to insert content:

- Microsoft Word
- Microsoft Excel (for tables)
- WPS Writer
- WPS Spreadsheet (for tables)

### 4️⃣ Press Hotkey

Press the hotkey (default `Ctrl+Shift+B`), and PasteMD will automatically:

1. Read clipboard content
2. Detect content type
3. Convert to appropriate format
4. Insert at cursor position

**Done!** 🎉

## Example: Paste from ChatGPT to Word

Let's demonstrate with a real example:

### Scenario

You ask ChatGPT a math question and get an answer with formulas:

```markdown
# Quadratic Formula

For the equation $ax^2 + bx + c = 0$, the solution is:

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

When $\Delta = b^2 - 4ac$:
- $\Delta > 0$: Two distinct real roots
- $\Delta = 0$: One repeated root
- $\Delta < 0$: Two complex conjugate roots
```

### Steps

1. **Select and Copy**: In ChatGPT, select the answer and press `Ctrl+C` (or `Cmd+C`)
2. **Open Word**: Switch to Word window and click where you want to insert
3. **Press Hotkey**: Press `Ctrl+Shift+B`
4. **View Result**: Content is immediately inserted with perfect formula display

### Result

- ✅ Title formatting is correct
- ✅ Inline formula $ax^2 + bx + c = 0$ displays as math equation
- ✅ Block formula is centered with perfect formatting
- ✅ List items maintain structure

## Configure Hotkey

If the default hotkey conflicts with other apps, you can customize it:

### Via Tray Menu

1. Right-click the tray icon
2. Select "Set Hotkey"
3. In the popup window, press your desired key combination
4. Click "Save"

::: tip Hotkey Suggestions
Recommend using combinations with `Ctrl` (or `Cmd`) + `Shift` to avoid conflicts with common shortcuts.

Examples:
- `Ctrl+Shift+V`
- `Ctrl+Shift+M`
- `Ctrl+Alt+V`
:::

## Tray Menu Features

Right-click the tray icon for:

### Basic Functions

- **Enable/Disable Hotkey**: Temporarily disable hotkey listening
- **System Notifications**: Toggle operation notifications
- **Keep Files**: Whether to keep DOCX/XLSX files after conversion

### Advanced Functions

- **Excel Toggle**: Enable/disable automatic table pasting to Excel
- **Set Hotkey**: Open hotkey settings window
- **Open Save Directory**: View converted files
- **View Logs**: Check error logs
- **Edit Config**: Advanced configuration options
- **Reload Config**: Apply config file changes

### Other Options

- **Check for Updates**: Check for new versions
- **Language**: Switch between Chinese/English
- **Exit**: Close application

## More Resources

- [Installation](/en/guide/installation) - Detailed installation steps
- [Features](/en/guide/markdown-conversion) - Learn all features
- [Configuration](/en/config/) - Customize PasteMD
- [macOS Guide](/en/macos/) - Essential for macOS users
