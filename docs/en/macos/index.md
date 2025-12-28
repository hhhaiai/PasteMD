---
layout: doc
---

# macOS Guide

PasteMD provides comprehensive macOS support, but due to platform differences, the macOS version uses different technical approaches and requires additional system permissions.

::: warning Important
**WPS Writer (macOS)**: Formulas will display as LaTeX code (e.g., `$E=mc^2$` and `$$formula$$`) and require manual conversion. Please read [WPS formula handling](/en/macos/wpslatex).

**Microsoft Word (macOS)**: Experience is basically the same as Windows and supports formulas.
:::

::: tip Important
If you're using PasteMD for the first time, please read this guide, especially the [Permissions](/en/macos/permissions) section.
:::

## Platform Differences

### Windows vs macOS

| Feature | Windows | macOS |
|---------|---------|-------|
| Word insertion / Excel write | COM Automation | AppleScript |
| WPS insertion | COM Automation | Clipboard Bridge |
| App detection | Win32 API | NSWorkspace + Quartz |
| Hotkey listening | System hook | CGEvent Tap |
| Permission requirements | No special permissions | Multiple permissions required |

### Technical Implementation

#### Microsoft Word/Excel

Uses **AppleScript** to control Office applications:

```applescript
tell application "Microsoft Word"
    tell active document
        insert file "path/to/file.docx" at selection
    end tell
end tell
```

**Features**:
- ✅ Direct insertion at cursor position
- ✅ Preserves complete formatting
- ✅ Supports complex document structures
- ⚠️ Requires "Automation" permission

#### WPS Writer/Spreadsheet

Uses **Clipboard Bridge** approach:

1. Generate DOCX/XLSX file
2. Read file content as HTML/RTF
3. Write to clipboard (rich text format)
4. Simulate `Cmd+V` paste

**Features**:
- ✅ Good compatibility
- ✅ No AppleScript support required
- ⚠️ Requires "Input Monitoring" permission
- ⚠️ Slightly lower format preservation than AppleScript

## Required Permissions

macOS sandbox security requires apps to obtain the following permissions:

### 1. **Accessibility** (Accessibility)

**Purpose**: Simulate keyboard input (for WPS paste)

**Impact**: WPS auto-paste won't work without authorization

### 2. **Screen Recording** (Screen Recording)

**Purpose**: Detect foreground windows and app names

**System Requirement**: macOS 10.15 Catalina and above

**Impact**: Cannot auto-detect current app without authorization

### 3. **Input Monitoring** (Input Monitoring)

**Purpose**: Listen to global hotkeys

**Impact**: Hotkeys won't work without authorization

### 4. **Automation** (Automation)

**Purpose**: Control Microsoft Word/Excel (via AppleScript)

**Impact**: Office app auto-insertion won't work without authorization

See detailed setup at [Permissions Guide](/en/macos/permissions).

## First Launch

### Auto-open Usage Guide

On first launch, PasteMD automatically opens the online usage guide:

**https://pastemd.richqaq.cn/macos**

This page includes:
- macOS version special notes
- Permission setup video tutorials
- FAQ

### Permission Check

1. Click menu bar icon
2. Select "Settings" -> "Permissions"
3. View status of each permission
4. Click "Open System Settings" to configure

::: warning Important
**All permissions must be granted** or some features won't work properly.
:::

## Menu Bar and Dock

### Menu Bar Icon

PasteMD primarily interacts via the **menu bar** (top-right), not the Dock.

Click the menu bar icon to:
- View current hotkey
- Toggle feature switches
- Open settings window
- Check permission status
- View logs and config

### Dock Icon

By default, PasteMD **does not appear in the Dock** to avoid taking space.

**Special cases**:
- When the "Settings" window is open, the Dock icon appears temporarily
- After closing the settings window, the Dock icon hides automatically

### Reopen Event

If you click the PasteMD Dock icon (on first launch or when it temporarily appears), it will open the settings window.

## File Paths

### Config File

```
~/Library/Application Support/PasteMD/config.json
```

### Log File

```
~/Library/Logs/PasteMD/pastemd.log
```

### Temporary Files

PasteMD uses **fixed temporary file paths** to avoid repeated permission prompts:

```
~/Library/Application Support/PasteMD/temp/pastemd_word_insert.docx
~/Library/Application Support/PasteMD/temp/pastemd_excel_insert.applescript
```

::: tip Why fixed paths?
macOS automation permissions are path-based. If every run uses a different temp filename, Office will keep prompting for authorization. Fixed paths mean "authorize once, works forever."
:::

## Supported Apps

### Microsoft Word

- **Version**: Microsoft 365, Office 2019/2021
- **Insertion**: AppleScript
- **Permissions**: Accessibility, Screen Recording, Automation
- **Format preservation**: ✅ Perfect

### Microsoft Excel

- **Version**: Microsoft 365, Office 2019/2021
- **Insertion**: AppleScript
- **Permissions**: Accessibility, Screen Recording, Automation
- **Format preservation**: ✅ Perfect (bold, italic, strike, code, etc.)

### WPS Writer

- **Version**: WPS Office for Mac
- **Insertion**: Clipboard Bridge
- **Permissions**: Accessibility, Screen Recording, Input Monitoring
- **Format preservation**: ⚠️ Basic formatting (bold, italic, hyperlinks)

### WPS Spreadsheet

- **Version**: WPS Office for Mac
- **Insertion**: Clipboard Bridge
- **Permissions**: Accessibility, Screen Recording, Input Monitoring
- **Format preservation**: ✅ Perfect (bold, italic, strike, code, etc.)

## App Detection

PasteMD uses the following methods to detect the foreground app:

### 1. NSWorkspace API

Get the active app name:

```python
app_name = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
```

Supported:
- `Microsoft Word`
- `Microsoft Excel`
- `wpsoffice` (WPS)

### 2. Quartz Window API

Get the foreground window title and owner:

```python
window_list = CGWindowListCopyWindowInfo(...)
```

Used to:
- Distinguish WPS Writer vs WPS Spreadsheet (by window title)
- Identify document type (.doc, .xls, .xlsx, etc.)

### Detection Logic

```
1. Get foreground app name
2. If Office app -> identify as Word/Excel
3. If WPS -> further check window title
   - Contains .doc/.docx -> WPS Writer
   - Contains .xls/.xlsx/.et -> WPS Spreadsheet
4. If table content + Excel enabled -> Excel workflow
5. Otherwise -> Word workflow
6. If no app detected -> fallback workflow
```

## macOS-only Features

### Permission Status Check

In the settings UI, you can view permission status in real time:

- ✅ **Authorized**: green
- ❌ **Not authorized**: red
- ⚠️ **Unknown**: gray

Click "Open System Settings" to jump directly to each permission page.

### Single-instance Detection

The macOS version uses **socket-based IPC** to ensure only one instance runs:

- If PasteMD is already running, launching again opens the settings window
- Uses Unix domain socket communication
- Socket path: `$TMPDIR/PasteMD.sock`

### Localization

macOS version supports system-level localization:

- **Info.plist localization**: app name, permission descriptions
- **Menu localization**: menus follow system language
- **Notification localization**: system notification texts

Localization files:
```
PasteMD.app/Contents/Resources/zh-Hans.lproj/InfoPlist.strings
PasteMD.app/Contents/Resources/en.lproj/InfoPlist.strings
```

## Known Limitations

### 1. Pages/Numbers not supported

Currently only Microsoft Office and WPS Office are supported. Apple Pages/Numbers are not supported.

**Reason**: Pages/Numbers AppleScript support is limited and cannot insert documents directly.

### 2. WPS format preservation

WPS Spreadsheet uses clipboard paste, so formatting retention is lower than Microsoft Excel.

**Suggestion**: If you need perfect formatting, use Microsoft Excel.

### 3. Permission dialogs

On first use, you may see multiple permission dialogs. This is normal macOS security behavior.

**Suggestion**: Grant all permissions patiently. You will not be prompted again afterward.

## More Resources

- [Permissions Guide](/en/macos/permissions)
- [Online Guide](https://pastemd.richqaq.cn/macos)
