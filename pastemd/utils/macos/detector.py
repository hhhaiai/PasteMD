# -*- coding: utf-8 -*-
"""
macOS application detection utilities.

依赖:
    pip install pyobjc-framework-AppKit pyobjc-framework-Quartz

说明:
- Word / Excel：优先用 bundle id 精确识别
- WPS：mac 端通常是一个统一 App（WPS Office），再用“窗口标题”区分文字/表格
"""

from __future__ import annotations
import subprocess

from AppKit import NSWorkspace
from Quartz import (
    CGWindowListCopyWindowInfo,
    kCGWindowListOptionOnScreenOnly,
    kCGWindowListExcludeDesktopElements,
)

from ..logging import log


def detect_active_app() -> str:
    """
    检测当前活跃的插入目标应用

    Returns:
        "word", "wps", "excel", "wps_excel" 或空字符串
    """
    app = _get_frontmost_app()

    # 兜底：有时 NSWorkspace 拿到的不是你想要的 frontmost（尤其是某些终端/IDE场景）
    if not app:
        app = _get_frontmost_app_via_osascript()

    if not app:
        return ""

    bundle_id = (app.get("bundle_id") or "").lower()
    name = (app.get("name") or "").lower()
    pid = app.get("pid")

    log(f"前台应用: name={app.get('name')}, bundle_id={app.get('bundle_id')}, pid={pid}")

    # ✅ Microsoft Word：name 可能是 "Word" 或 "Microsoft Word"
    if bundle_id.endswith(".word") or bundle_id == "com.microsoft.word" or name in ("word", "microsoft word"):
        return "word"

    # ✅ Microsoft Excel：name 可能是 "Excel" 或 "Microsoft Excel"
    if bundle_id.endswith(".excel") or bundle_id == "com.microsoft.excel" or name in ("excel", "microsoft excel"):
        return "excel"

    # ✅ WPS：bundle id / name 做宽松判断
    if "kingsoft" in bundle_id or "wps" in name:
        return detect_wps_type(frontmost_pid=pid)

    return ""


def detect_wps_type(frontmost_pid: int | None = None) -> str:
    """
    检测 WPS 应用的具体类型 (文字/表格)
    macOS 不像 Windows 那样容易通过 COM 精确区分，因此主要依赖窗口标题。

    Returns:
        "wps" (文字), "wps_excel" (表格) 或空字符串
    """
    window_title = _get_frontmost_window_title(frontmost_pid=frontmost_pid)
    log(f"WPS 窗口标题: {window_title}")

    # 如果标题拿不到，就只能保守默认文字
    if not window_title:
        log("无法获取窗口标题,默认识别为 WPS 文字")
        return "wps"

    title_l = window_title.lower()

    # 优先级1: 文件后缀判断（最明确）
    excel_extensions = [".et", ".xls", ".xlsx", ".csv"]
    for ext in excel_extensions:
        if ext in title_l:
            log(f"通过窗口标题后缀 '{ext}' 识别为 WPS 表格")
            return "wps_excel"

    word_extensions = [".doc", ".docx", ".wps"]
    for ext in word_extensions:
        if ext in title_l:
            log(f"通过窗口标题后缀 '{ext}' 识别为 WPS 文字")
            return "wps"

    # 优先级2: 关键词判断（不同语言/版本的 WPS 可能不同，可按你用户群继续补充）
    excel_keywords = [
        "wps spreadsheets",
        "表格",
        "工作簿",
        "spreadsheet",
        "sheet",
    ]
    for kw in excel_keywords:
        if kw.lower() in title_l:
            log(f"通过窗口标题关键词 '{kw}' 识别为 WPS 表格")
            return "wps_excel"

    word_keywords = [
        "wps writer",
        "文字",
        "文档",
        "writer",
        "document",
    ]
    for kw in word_keywords:
        if kw.lower() in title_l:
            log(f"通过窗口标题关键词 '{kw}' 识别为 WPS 文字")
            return "wps"

    log("无明确标识,默认识别为 WPS 文字")
    return "wps"


def _get_frontmost_app() -> dict | None:
    """通过 NSWorkspace 获取前台应用信息"""
    try:
        ws = NSWorkspace.sharedWorkspace()
        app = ws.frontmostApplication()
        if not app:
            return None
        return {
            "name": str(app.localizedName() or ""),
            "bundle_id": str(app.bundleIdentifier() or ""),
            "pid": int(app.processIdentifier()),
        }
    except Exception as e:
        log(f"获取前台应用失败(NSWorkspace): {e}")
        return None


def _get_frontmost_app_via_osascript() -> dict | None:
    """
    兜底方案：通过 AppleScript 获取 frontmost app 名称（非常稳定）
    注意：这里拿不到 bundle_id/pid，就只填 name
    """
    try:
        cmd = [
            "osascript",
            "-e",
            'tell application "System Events" to get name of first application process whose frontmost is true'
        ]
        name = subprocess.check_output(cmd, text=True).strip()
        if not name:
            return None
        return {"name": name, "bundle_id": "", "pid": None}
    except Exception as e:
        log(f"获取前台应用失败(osascript): {e}")
        return None


def _get_frontmost_window_title(frontmost_pid: int | None = None) -> str:
    """
    尝试获取前台窗口标题（同一 pid 可能有多个窗口，这里取最可能的那个）
    """
    try:
        # 获取屏幕上所有窗口的基本信息（不包含桌面元素）
        options = kCGWindowListOptionOnScreenOnly | kCGWindowListExcludeDesktopElements
        win_list = CGWindowListCopyWindowInfo(options, 0) or []

        # 如果给了 pid，就只看这个进程的窗口；否则尽量取 layer=0 且有名字的
        candidates = []
        for w in win_list:
            try:
                owner_pid = int(w.get("kCGWindowOwnerPID", -1))
                layer = int(w.get("kCGWindowLayer", 999))
                title = w.get("kCGWindowName", "") or ""
                owner_name = w.get("kCGWindowOwnerName", "") or ""

                if layer != 0:
                    continue
                if frontmost_pid is not None and owner_pid != int(frontmost_pid):
                    continue

                # 有些应用窗口标题为空，但 owner_name 有值；这里优先 title
                if title.strip():
                    candidates.append((title, owner_name))
            except Exception:
                continue

        if candidates:
            # 直接取第一个通常就够用；如遇到多窗口可改成更复杂的排序策略
            return str(candidates[0][0])

        return ""
    except Exception as e:
        log(f"获取前台窗口标题失败: {e}")
        return ""


if __name__ == "__main__":
    import time

    log("开始 macOS 前台应用检测测试（每 3 秒一次，Ctrl+C 退出）")
    try:
        while True:
            app = _get_frontmost_app() or _get_frontmost_app_via_osascript()
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} frontmost={app}  detect={detect_active_app()}")
            time.sleep(3)
    except KeyboardInterrupt:
        log("检测测试已手动终止")
        print("退出检测")

