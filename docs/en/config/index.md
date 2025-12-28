# Configuration Options

PasteMD provides a rich set of configuration options, allowing you to customize its behavior according to your needs.

## Configuration File Location

### Windows
```

C:\Users<Username>.pastemd\config.json

```

### macOS
```

~/Library/Application Support/PasteMD/config.json

````

## Quick Access

You can quickly open the configuration file from the system tray menu:

1. Right-click the tray icon  
2. Select **"Edit Configuration File"**  
3. The configuration file will open in your default text editor  

## Full Configuration Example

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
````

## Configuration Options Explained

### Basic Settings

#### `hotkey`

* **Type**: string
* **Default**: `"<ctrl>+<shift>+b"`
* **Description**: Global hotkey configuration

**Supported modifier keys**:

* `<ctrl>` – Ctrl key (mapped to Cmd on macOS)
* `<shift>` – Shift key
* `<alt>` – Alt key (Option on macOS)
* `<cmd>` – macOS only, Command key
* `<win>` – Windows only, Windows key

**Examples**:

```json
"hotkey": "<ctrl>+<shift>+v"
"hotkey": "<ctrl>+<alt>+m"
"hotkey": "<cmd>+<shift>+b"  // macOS
```

::: tip Recommendation
Use a combination with at least two modifier keys to avoid conflicts with common shortcuts.
:::

---

#### `language`

* **Type**: string
* **Default**: `"zh"`
* **Options**: `"zh"` | `"en"`
* **Description**: UI language setting

Restart the application after changing the language.

---

#### `notify`

* **Type**: boolean
* **Default**: `true`
* **Description**: Whether to display system notifications

**Notification contents**:

* Success messages
* Error messages
* Application detection results

---

### Pandoc Settings

#### `pandoc_path`

* **Type**: string
* **Default**: `"pandoc"`
* **Description**: Path to the Pandoc executable

**Default behavior**: Pandoc is resolved from the system `PATH`.

**Custom paths**:

```json
// Windows
"pandoc_path": "C:\\Program Files\\Pandoc\\pandoc.exe"

// macOS
"pandoc_path": "/usr/local/bin/pandoc"

// Relative path (relative to PasteMD executable)
"pandoc_path": "./third_party/pandoc/pandoc"
```

::: warning Note
On Windows, backslashes must be escaped (`\\`) or replaced with forward slashes (`/`).
:::

---

#### `reference_docx` (usually not needed)

* **Type**: string | null
* **Default**: `null`
* **Description**: Reference DOCX template path

Using a reference template allows you to:

* Apply custom styles (headings, body text, code blocks, etc.)
* Configure page layout (margins, headers, footers)
* Unify fonts and colors

**Examples**:

```json
"reference_docx": "~/Documents/my-template.docx"
"reference_docx": "C:/Users/YourName/template.docx"
```

**How to create a reference template**:

1. Create a document in Word
2. Configure the desired styles (Heading 1–6, Body Text, Code, etc.)
3. Save it as a `.docx` file
4. Specify the path in the configuration

---

#### `pandoc_filters`

* **Type**: array of strings
* **Default**: `[]`
* **Description**: Custom Pandoc filter list

Pandoc filters are scripts (Lua, Python, etc.) used to extend or modify conversion behavior.

**Example**:

```json
"pandoc_filters": [
  "mermaid-filter",
  "~/filters/custom-filter.lua"
]
```

See [Custom Filters](/zh/guide/custom-filters) for details.

---

### File Management

#### `save_dir`

* **Type**: string
* **Default**: `"~/Documents/pastemd"`
* **Description**: Directory where converted files are saved

**Supported path formats**:

* `~` expands to the user home directory
* Relative paths (relative to the configuration file directory)
* Absolute paths

**Examples**:

```json
"save_dir": "~/Desktop/PasteMD"
"save_dir": "D:/Work/Documents"
```

---

#### `keep_file`

* **Type**: boolean

* **Default**: `false`

* **Description**: Whether to keep generated files after insertion

* **`false`**: Temporary files are deleted automatically after insertion

* **`true`**: Files are kept in the `save_dir` directory

::: tip Use cases

* `false` (default): Daily usage, reduces disk clutter
* `true`: Archiving converted files or debugging issues
  :::

---

### Excel Table Settings

#### `enable_excel`

* **Type**: boolean

* **Default**: `true`

* **Description**: Enable automatic Excel table pasting

* **`true`**: When a Markdown table is detected and Excel is the active app, it is converted to native Excel format

* **`false`**: Excel functionality is disabled

---

#### `excel_keep_format`

* **Type**: boolean
* **Default**: `true`
* **Description**: Preserve formatting when pasting into Excel

**Preserved formatting (when `true`)**:

* **Bold**: `**text**` → Bold cells

* *Italic*: `*text*` → Italic cells

* ~~Strikethrough~~: `~~text~~` → Strikethrough

* `Code`: `` `code` `` → Gray background + monospace font

* Hyperlinks: `[text](url)` → Clickable links

* **`false`**: Only plain text is inserted, no formatting

---

### Formatting Options

#### `md_disable_first_para_indent`

* **Type**: boolean
* **Default**: `true`
* **Description**: Disable first-paragraph indentation for Markdown conversion

---

#### `html_disable_first_para_indent`

* **Type**: boolean
* **Default**: `true`
* **Description**: Disable first-paragraph indentation for HTML conversion

---

#### `html_formatting`

* **Type**: object
* **Description**: HTML preprocessor formatting options

**Sub-options**:

##### `strikethrough_to_del`

* **Type**: boolean
* **Default**: `true`
* **Description**: Convert `~~` to `<del>` tags

Some websites do not render `~~` as strikethrough properly and instead show it as plain text. Enabling this option ensures correct strikethrough rendering.

**Example**:

```json
"html_formatting": {
  "strikethrough_to_del": true
}
```

---

#### `move_cursor_to_end` (Windows only)

* **Type**: boolean

* **Default**: `true`

* **Description**: Move the cursor to the end after insertion

* **`true`**: Cursor moves to the end of inserted content for continued typing

* **`false`**: Cursor stays at the beginning of the inserted content

---

### Math Formula Settings

#### `Keep_original_formula`

* **Type**: boolean

* **Default**: `false`

* **Description**: Keep original LaTeX formulas instead of converting to MathML

* **`false`** (default): Formulas are converted to Office MathML for perfect rendering

* **`true`**: Formulas remain as `$...$` text for manual editing

**Use cases**:

* When you want to manually edit formulas in Word
* Temporary workaround if formula conversion fails

---

#### `enable_latex_replacements`

* **Type**: boolean
* **Default**: `true`
* **Description**: Enable LaTeX compatibility fixes

Automatically fixes non-standard LaTeX syntax commonly produced by AI tools, for example:

* `\kern` → `\qquad` (Pandoc does not support `\kern`)

---

#### `fix_single_dollar_block`

* **Type**: boolean
* **Default**: `true`
* **Description**: Automatically fix block-level formulas wrapped with single `$`

Some AI tools incorrectly wrap block formulas with `$...$` instead of `$$...$$`. This option detects and fixes them automatically.

**Detection criteria**:

* The formula occupies a single line
* Wrapped with single `$`
* Formula length exceeds a threshold

**Example**:

```markdown
# Original (incorrect)
$\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$

# Automatically fixed to
$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

---

### Fallback Behavior

#### `no_app_action`

* **Type**: string
* **Default**: `"open"`
* **Options**: `"open"` | `"save"` | `"clipboard"` | `"none"`
* **Description**: Behavior when no target application is detected

**Option details**:

| Value       | Behavior                                   | Use case                  |
| ----------- | ------------------------------------------ | ------------------------- |
| `open`      | Automatically open Word and insert content | Daily usage (recommended) |
| `save`      | Save as a file to `save_dir` only          | Batch file conversion     |
| `clipboard` | Convert to rich text and copy to clipboard | Paste into other apps     |
| `none`      | Show notification only, no action          | Restricted environments   |

**Example**:

```json
"no_app_action": "save"
```

---

## Applying Configuration Changes

### By Editing the Configuration File

Restart PasteMD after editing.

### Via Settings UI or Tray Menu

Changes are applied automatically without restarting.

## Troubleshooting

### Configuration File Corrupted

1. Check whether the JSON syntax is valid
2. Restore default configuration:

   * Delete the configuration file; the app will regenerate it automatically

### Configuration Not Taking Effect

1. Check logs for error messages
2. Try restarting the application

## More Information

* [Advanced Features](/zh/guide/custom-filters) – Custom Pandoc filters
* [GitHub](https://github.com/RichQAQ/PasteMD) – Source code and issue tracking

