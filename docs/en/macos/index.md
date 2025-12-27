---
layout: doc
---

# macOS Guide

PasteMD provides comprehensive macOS support, but due to platform differences, the macOS version uses different technical approaches and requires additional system permissions.

::: tip Important
If you're using PasteMD for the first time, please read this guide, especially the [Permissions](/en/macos/permissions) section.
:::

## Platform Differences

### Windows vs macOS

| Feature | Windows | macOS |
|---------|---------|-------|
| Word/Excel Insertion | COM Automation | AppleScript |
| WPS Insertion | COM Automation | Clipboard Bridge |
| App Detection | Win32 API | NSWorkspace + Quartz |
| Hotkey Listening | System Hook | CGEvent Tap |
| Permission Requirements | No special permissions | Multiple permissions required |

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
- ✅ Doesn't require AppleScript support
- ⚠️ Requires "Input Monitoring" permission
- ⚠️ Slightly lower format preservation than AppleScript

## Required Permissions

macOS sandbox security requires apps to obtain the following permissions:

### 1. **Accessibility**

**Purpose**: Listen to global hotkeys

**Impact**: Hotkeys won't work without authorization

### 2. **Screen Recording**

**Purpose**: Detect foreground windows and app names

**System Requirement**: macOS 10.15 Catalina and above

**Impact**: Cannot auto-detect current app without authorization

### 3. **Input Monitoring**

**Purpose**: Simulate keyboard input (for WPS paste)

**Impact**: WPS auto-paste won't work without authorization

### 4. **Automation**

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

1. Click menu bar icon 📋
2. Select "Settings" → "Permissions"
3. View status of each permission
4. Click "Open System Settings" to configure

::: warning Important
**All permissions must be granted** or some features won't work properly.
:::

## More Resources

- [Online Guide](https://pastemd.richqaq.cn/macos)
