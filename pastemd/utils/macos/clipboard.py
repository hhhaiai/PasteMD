"""macOS clipboard operations using AppKit.NSPasteboard."""

import pyperclip
from AppKit import (
    NSPasteboard,
    NSPasteboardTypeHTML,
    NSPasteboardTypeRTF,
    NSPasteboardItem,
    NSPasteboardTypeString,
    NSFilenamesPboardType,
    NSURL,
)
from Foundation import NSData
from ...core.errors import ClipboardError
from ...core.state import app_state
from ..clipboard_file_utils import read_file_with_encoding, filter_markdown_files, read_markdown_files
from ..logging import log

DOCX_UTIS = [
    "org.openxmlformats-officedocument.wordprocessingml.document",
    "org.openxmlformats.wordprocessingml.document",   # 有些环境/资料用这个 :contentReference[oaicite:2]{index=2}
    "com.microsoft.word.docx",                        # 试探性补一个（不保证 Word 用它）
]

RTF_UTI = "public.rtf"
HTML_UTI = "public.html"
PLAIN_UTI = "public.utf8-plain-text"


def get_clipboard_text() -> str:
    """
    获取剪贴板文本内容
    
    Returns:
        剪贴板文本内容
        
    Raises:
        ClipboardError: 剪贴板操作失败时
    """
    try:
        text = pyperclip.paste()
        if text is None:
            return ""
        return text
    except Exception as e:
        raise ClipboardError(f"Failed to read clipboard: {e}")


def is_clipboard_empty() -> bool:
    """
    检查剪贴板是否为空
    
    Returns:
        True 如果剪贴板为空或只包含空白字符
    """
    try:
        text = get_clipboard_text()
        return not text or not text.strip()
    except ClipboardError:
        return True


def is_clipboard_html() -> bool:
    """
    检查剪切板内容是否为 HTML 富文本

    Returns:
        True 如果剪贴板中存在 HTML 富文本格式；否则 False
    """
    try:
        pasteboard = NSPasteboard.generalPasteboard()
        # 检查是否存在 HTML 类型
        types = pasteboard.types()
        if types is None:
            return False
        
        # macOS 使用 NSPasteboardTypeHTML (public.html)
        return NSPasteboardTypeHTML in types
    except Exception:
        return False


def get_clipboard_html(config: dict | None = None) -> str:
    """
    获取剪贴板 HTML 富文本内容，并清理 SVG 等不可用内容

    Returns:
        清理后的 HTML 富文本内容

    Raises:
        ClipboardError: 剪贴板操作失败时
    """
    try:
        config = config or getattr(app_state, "config", {})

        pasteboard = NSPasteboard.generalPasteboard()

        # 尝试获取 HTML 数据
        html_data = pasteboard.stringForType_(NSPasteboardTypeHTML)

        if html_data is None:
            raise ClipboardError("No HTML format data in clipboard")

        # macOS 返回的已经是 HTML 内容字符串，不需要像 Windows 那样解析 CF_HTML 格式
        html_content = str(html_data)

        # 直接返回原始 HTML，不在剪贴板层进行清理
        return html_content

    except Exception as e:
        raise ClipboardError(f"Failed to read HTML from clipboard: {e}")


def set_clipboard_rich_text(
    *,
    html: str | None = None,
    rtf_bytes: bytes | None = None,
    docx_bytes: bytes | None = None,
    text: str | None = None,
) -> None:
    """
    写入富文本剪贴板（HTML/RTF/纯文本可多格式同时写入）。

    Note:
        - 目标应用会优先选择其支持的格式（WPS 文字通常偏好 HTML）。
    """
    try:
        pasteboard = NSPasteboard.generalPasteboard()
        pasteboard.clearContents()

        item = NSPasteboardItem.alloc().init()

        # 1) DOCX（写多个 UTI，尽量覆盖 Word 的选择）
        if docx_bytes is not None:
            docx_data = NSData.dataWithBytes_length_(docx_bytes, len(docx_bytes))
            for uti in DOCX_UTIS:
                item.setData_forType_(docx_data, uti)
                log(f"set DOCX type={uti} len={len(docx_bytes)}")

        # 2) RTF（确保样式最容易被 Word 吃到）
        if rtf_bytes is not None:
            rtf_data = NSData.dataWithBytes_length_(rtf_bytes, len(rtf_bytes))
            item.setData_forType_(rtf_data, NSPasteboardTypeRTF)
            log(f"set RTF type={NSPasteboardTypeRTF} len={len(rtf_bytes)}")
            
        # 3) HTML（再给一个富文本备选）
        if html is not None:
            html_data = NSData.dataWithBytes_length_(html.encode("utf-8"), len(html.encode("utf-8")))
            item.setData_forType_(html_data, NSPasteboardTypeHTML)
            log(f"set HTML type={NSPasteboardTypeHTML} len={len(html.encode('utf-8'))}")

        # 4) Plain（兜底）
        if text is not None:
            item.setString_forType_(text, PLAIN_UTI)
            log(f"set PLAIN type={PLAIN_UTI} len={len(text.encode('utf-8'))}")
        
        wrote = pasteboard.writeObjects_([item])
        if not wrote:
            raise ClipboardError("Failed to write rich text to clipboard")
    except Exception as e:
        raise ClipboardError(f"Failed to write rich text to clipboard: {e}")


# ============================================================
# macOS 文件操作功能
# ============================================================

def copy_files_to_clipboard(file_paths: list) -> None:
    """
    将文件路径复制到剪贴板（NSFilenamesPboardType）

    Args:
        file_paths: 文件路径列表

    Raises:
        ClipboardError: 剪贴板操作失败时
    """
    try:
        import os
        # 确保文件路径是绝对路径
        absolute_paths = [os.path.abspath(path) for path in file_paths if os.path.exists(path)]
        
        if not absolute_paths:
            raise ClipboardError("No valid files to copy to clipboard")
        
        pasteboard = NSPasteboard.generalPasteboard()
        pasteboard.clearContents()
        
        # macOS 使用 NSFilenamesPboardType 存储文件路径
        success = pasteboard.setPropertyList_forType_(absolute_paths, NSFilenamesPboardType)
        
        if not success:
            raise ClipboardError("Failed to set file paths to clipboard")
        
        log(f"Successfully copied {len(absolute_paths)} files to clipboard")
        
    except Exception as e:
        raise ClipboardError(f"Failed to copy files to clipboard: {e}")


def is_clipboard_files() -> bool:
    """
    检测剪贴板是否包含文件

    Returns:
        True 如果剪贴板中存在文件；否则 False
    """
    try:
        pasteboard = NSPasteboard.generalPasteboard()
        types = pasteboard.types()
        if types is None:
            return False
        
        # macOS 使用 NSFilenamesPboardType (或 public.file-url)
        result = NSFilenamesPboardType in types
        log(f"Clipboard files check: {result}")
        return result
    except Exception as e:
        log(f"Failed to check clipboard files: {e}")
        return False


def get_clipboard_files() -> list[str]:
    """
    获取剪贴板中的文件路径列表

    Returns:
        文件绝对路径列表
    """
    file_paths = []
    try:
        pasteboard = NSPasteboard.generalPasteboard()
        
        # 尝试从 NSFilenamesPboardType 获取文件路径
        files = pasteboard.propertyListForType_(NSFilenamesPboardType)
        
        if files:
            file_paths = list(files)
            log(f"Got {len(file_paths)} files from clipboard")
        
    except Exception as e:
        log(f"Failed to get clipboard files: {e}")
    
    return file_paths


def get_markdown_files_from_clipboard() -> list[str]:
    """
    从剪贴板获取 Markdown 文件路径列表

    只返回扩展名为 .md 或 .markdown 的文件

    Returns:
        Markdown 文件的绝对路径列表（按文件名排序）
    """
    all_files = get_clipboard_files()
    return filter_markdown_files(all_files)


def read_markdown_files_from_clipboard() -> tuple[bool, list[tuple[str, str]], list[tuple[str, str]]]:
    """
    从剪贴板读取 Markdown 文件内容

    封装了"获取剪贴板 MD 文件路径 + 逐个读取内容"的完整逻辑。
    读取失败的文件会被跳过，继续处理其它文件。

    Returns:
        (found, files_data, errors) 元组：
        - found: 是否发现并成功读取至少一个 MD 文件
        - files_data: [(filename, content), ...] 成功读取的文件名和内容列表
        - errors: [(filename, error_message), ...] 读取失败的文件和错误信息
    """
    md_files = get_markdown_files_from_clipboard()
    return read_markdown_files(md_files)
