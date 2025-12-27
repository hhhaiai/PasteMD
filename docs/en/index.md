---
layout: home

hero:
  name: "PasteMD"
  text: "Smart Markdown Converter"
  tagline: Seamlessly paste AI conversations to Word/WPS with perfect formulas and formatting
  image:
    src: /logo.png
    alt: PasteMD
  actions:
    - theme: brand
      text: Get Started
      link: /en/guide/getting-started
    - theme: alt
      text: What is PasteMD?
      link: /en/guide/what-is-pastemd
    - theme: alt
      text: GitHub
      link: https://github.com/RichQAQ/PasteMD

features:
  - icon: ⚡️
    title: One-Key Conversion
    details: Press hotkey (Ctrl+Shift+B) to instantly convert and insert Markdown from clipboard to Word/WPS
  - icon: 🎯
    title: Smart Recognition
    details: Automatically detects content type (Markdown/HTML/Table) and target application
  - icon: 📐
    title: Perfect Formulas
    details: Correctly handles LaTeX math formulas for paste conversion (macOS WPS does not support direct formula display)
  - icon: 📊
    title: Format Preservation
    details: Preserves bold, italic, strikethrough, code formatting when pasting tables to Excel
  - icon: 🖥️
    title: Cross-Platform
    details: Supports Windows and macOS, works with Microsoft Office and WPS Office
  - icon: 🎨
    title: Highly Customizable
    details: Custom hotkeys, style templates, Pandoc filters, and more

---

## Why PasteMD?

When copying content from ChatGPT, DeepSeek, Kimi, and other AI websites to Word, do you encounter these issues?

- ❌ Math formulas turn into gibberish
- ❌ Markdown formatting is completely lost
- ❌ Code blocks display incorrectly
- ❌ Tables need manual reformatting

**PasteMD solves all these problems with one keystroke!**

## Supported Applications

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0;">
  <div class="feature-card">
    <div style="font-size: 32px; margin-bottom: 8px;">📝</div>
    <h3>Microsoft Word</h3>
    <p>Windows & macOS</p>
  </div>
  <div class="feature-card">
    <div style="font-size: 32px; margin-bottom: 8px;">📄</div>
    <h3>WPS Writer</h3>
    <p>Windows & macOS</p>
  </div>
  <div class="feature-card">
    <div style="font-size: 32px; margin-bottom: 8px;">📊</div>
    <h3>Microsoft Excel</h3>
    <p>Windows & macOS</p>
  </div>
  <div class="feature-card">
    <div style="font-size: 32px; margin-bottom: 8px;">📈</div>
    <h3>WPS Spreadsheet</h3>
    <p>Windows & macOS</p>
  </div>
</div>

## Quick Start

:::: code-group
::: code-group-item Windows
\`\`\`bash
# Download installer
# Run PasteMD-Setup.exe

# Or use portable version
# Extract and run PasteMD.exe
\`\`\`
:::

::: code-group-item macOS
\`\`\`bash
# Download DMG file
# Drag to Applications folder

# Grant permissions on first launch
# See macOS Guide for details
\`\`\`
:::
::::

## Usage Flow

1. **Launch PasteMD** - App stays in system tray
2. **Copy Content** - Copy Markdown from AI websites or elsewhere
3. **Open Document** - Position cursor in Word/WPS
4. **Press Hotkey** - Default \`Ctrl+Shift+B\`
5. **Done!** - Content automatically converted and inserted

## Featured Capabilities

### 🔬 Math Formula Support

Automatically recognizes and correctly processes \`$...$\` and \`$$...$$\` formulas:

\`\`\`markdown
Inline formula: $E = mc^2$

Block formula:
$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
\`\`\`

::: warning macOS WPS Users
Due to macOS WPS not supporting AppleScript automation, formulas will display as LaTeX code (e.g., \`$E=mc^2$\` and \`$$formula$$\`) and require manual conversion. We recommend macOS users use Microsoft Word for perfect formula support.
:::

### 📋 Table Format Preservation

Preserves all Markdown formatting when pasting to Excel:

| Feature | Supported |
|---------|-----------|
| **Bold** | ✅ |
| *Italic* | ✅ |
| ~~Strikethrough~~ | ✅ |
| \`Code\` | ✅ |

### 🎯 Smart Fallback Mode

Even without Word/Excel open, you can:
- Auto-open the application
- Save as file only
- Copy rich text to clipboard
- Or do nothing

## Get Started Now

<div style="text-align: center; margin: 48px 0;">
  <a href="/en/guide/getting-started" style="display: inline-block; padding: 12px 32px; background: linear-gradient(135deg, #5f9ea0, #4a8a8c); color: white; border-radius: 8px; text-decoration: none; font-weight: 600; font-size: 16px;">
    View Getting Started Guide →
  </a>
</div>
