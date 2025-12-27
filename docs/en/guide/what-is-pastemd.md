# What is PasteMD?

PasteMD is a cross-platform smart Markdown converter designed to solve the problem of format loss and formula corruption when copying content from AI conversation websites (like ChatGPT, DeepSeek, Kimi, etc.) to Word/WPS.

## The Core Problem

When you copy Markdown-formatted content from AI websites and paste it directly into Word, you encounter:

- **Garbled Math Formulas**: `$E=mc^2$` becomes plain text, complex formulas are completely unreadable
- **Lost Formatting**: Bold, italic, code blocks, and other formatting all disappear
- **Messy Tables**: Markdown tables need manual adjustment after pasting
- **Code Display Issues**: Code blocks lack syntax highlighting and display incorrectly

## PasteMD's Solution

PasteMD provides an elegant solution:

1. **One-Key Conversion**: Press hotkey (default `Ctrl+Shift+B`) to automatically convert and insert
2. **Smart Recognition**: Automatically detects clipboard content type and current application
3. **Perfect Formatting**: Math formulas, code blocks, tables rendered perfectly
4. **Seamless Integration**: Content inserted directly at cursor position, no manual steps needed

## How It Works

```mermaid
graph LR
    A[Copy Markdown] --> B[Press Hotkey]
    B --> C[Read Clipboard]
    C --> D[Preprocess Content]
    D --> E[Pandoc Convert]
    E --> F[Insert to App]
    F --> G[Done!]
```

PasteMD's core workflow:

1. **Listen for Hotkey**: Global monitoring of custom hotkey
2. **Read Clipboard**: Get Markdown, HTML, or file paths
3. **Preprocess**: Normalize format, process formulas, clean HTML
4. **Pandoc Conversion**: Call Pandoc to convert to DOCX or XLSX format
5. **Application Insert**: Insert to target app via platform-specific APIs

## Supported Platforms and Applications

### Windows

- ✅ Microsoft Word (via COM Automation)
- ✅ Microsoft Excel (via COM Automation)
- ✅ WPS Writer (via COM Automation)
- ✅ WPS Spreadsheet (via COM Automation)

### macOS

- ✅ Microsoft Word (via AppleScript)
- ✅ Microsoft Excel (via AppleScript)
- ✅ WPS Writer (via Clipboard Rich Text)
- ✅ WPS Spreadsheet (via Clipboard)

::: tip macOS Note
The macOS version uses different technical approaches and requires additional system permissions. See [macOS Guide](/en/macos/) for details.
:::

## Key Features

### 🎯 Smart Content Recognition

Automatically detects clipboard content type:

- **Markdown Text**: Standard Markdown syntax
- **HTML Rich Text**: Content copied from web pages
- **Markdown Tables**: Auto-detected and converted to Excel
- **.md Files**: Files copied from file manager

### 📐 Perfect Math Formula Support

- Supports inline formulas: `$...$`
- Supports block formulas: `$$...$$`
- Auto-fixes common LaTeX syntax issues
- Compatible with formula formats from popular AI websites

### 📊 Table Format Preservation

Completely preserves formatting when pasting to Excel:

- **Bold**: `**text**`
- *Italic*: `*text*`
- ~~Strikethrough~~: `~~text~~`
- `Inline Code`: `` `code` ``
- Code Blocks: ` ```code``` `
- Hyperlinks: `[text](url)`

### 🎨 Highly Customizable

- Custom global hotkey
- Custom style templates (reference DOCX)
- Custom Pandoc filters
- Custom save directory and file retention policy
- Multi-language support (Chinese/English)

### 🔄 Smart Fallback Mode

When no target application is detected, you can:

- **Auto-Open**: Automatically launch Word and insert content
- **Save Only**: Save as file to specified directory
- **Copy to Clipboard**: Convert to rich text and copy to clipboard
- **No Action**: Just show notification

## Technical Architecture

PasteMD uses a layered architecture design:

- **Presentation Layer**: Tray menu, hotkey settings, permission management UI
- **Service Layer**: Document generation, spreadsheet generation, preprocessors, notification service
- **Core Layer**: Workflow routing, application detection, clipboard operations
- **Integration Layer**: Pandoc integration, platform-specific APIs

## Dependencies

- **Pandoc**: Powerful document conversion engine (required)
- **Python 3.12+**: Runtime environment
- **Platform-Specific Libraries**: pywin32 (Windows), pyobjc (macOS)

## License

PasteMD is open source under the [MIT License](https://github.com/RichQAQ/PasteMD/blob/main/LICENSE). You are free to use, modify, and distribute it.

## Next Steps

- [Getting Started](/en/guide/getting-started) - Start using PasteMD now
- [Installation](/en/guide/installation) - Detailed installation steps
- [macOS Guide](/en/macos/) - macOS-specific instructions
