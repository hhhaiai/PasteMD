# Configuration

PasteMD provides rich configuration options to customize functionality according to your needs.

## Config File Location

### Windows
```
C:\Users\<username>\.pastemd\config.json
```

### macOS
```
~/.pastemd/config.json
```

## Quick Access

Access config file quickly via tray menu:

1. Right-click tray icon
2. Select "Edit Config"
3. Config file opens in default text editor

## Complete Config Example

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

## Configuration Reference

### Basic Settings

#### `hotkey`
- **Type**: String
- **Default**: `"<ctrl>+<shift>+b"`
- **Description**: Global hotkey configuration

**Supported modifiers**:
- `<ctrl>` - Ctrl key (maps to Cmd on macOS)
- `<shift>` - Shift key
- `<alt>` - Alt key (Option on macOS)
- `<cmd>` - macOS only, Command key
- `<win>` - Windows only, Windows key

---

#### `language`
- **Type**: String
- **Default**: `"zh"`
- **Options**: `"zh"` | `"en"`
- **Description**: Interface language

Requires app restart after change.

---

#### `no_app_action`
- **Type**: String
- **Default**: `"open"`
- **Options**: `"open"` | `"save"` | `"clipboard"` | `"none"`
- **Description**: Behavior when no target app detected

| Value | Behavior | Use Case |
|-------|----------|----------|
| `open` | Auto-open Word and insert | Daily use (recommended) |
| `save` | Save to `save_dir` only | Batch file conversion |
| `clipboard` | Convert to rich text and copy | Paste to other apps |
| `none` | Show notification only | Use in specific apps only |

## Apply Configuration Changes

### Method 1: Via Tray Menu

1. Edit config file (Tray Menu → "Edit Config")
2. Save changes
3. Tray Menu → "Reload Config"

### Method 2: Restart App

After editing config file, exit and restart PasteMD.

::: tip Hot Reload
Most config options support hot reload without restart. However, `hotkey` and a few others require restart to take effect.
:::

## More Information

- [Advanced Features](/en/guide/custom-filters) - Custom Pandoc filters
- [API Reference](/en/api/) - Developer docs
- [GitHub](https://github.com/RichQAQ/PasteMD) - Source code and issues
