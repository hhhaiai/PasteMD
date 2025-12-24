"""Utilities for cleaning and formatting HTML fragments before conversion."""

from __future__ import annotations

import re
from typing import Dict, Optional

from bs4 import BeautifulSoup, NavigableString


def clean_html_content(soup: BeautifulSoup, options: Optional[Dict[str, object]] = None) -> None:
    """
    清理 HTML 内容，移除不可用元素，并按配置应用格式化规则。

    Args:
        html: 原始 HTML 内容。
        options: 可选格式化配置，如 ``{"strikethrough_to_del": True}``。

    Returns:
        清理后的 HTML 内容。
    """

    options = options or {}

    # 删除所有 <svg> 标签
    for svg in soup.find_all("svg"):
        svg.decompose()

    # 删除 src 指向 .svg 的 <img> 标签
    for img in soup.find_all("img", src=True):
        if img["src"].lower().endswith(".svg"):
            img.decompose()
    
    # 清理 LaTeX 公式块中的 <br> 标签
    _clean_latex_br_tags(soup)


def convert_strikethrough_to_del(soup) -> None:
    """
    在 BeautifulSoup 解析树中查找文本节点，将 ``~~text~~`` 替换为 ``<del>text</del>``。

    Args:
        soup: BeautifulSoup 对象，会被原地修改。
    """
    # 递归处理所有文本节点
    for element in soup.find_all(text=True):
        if isinstance(element, NavigableString):
            if "~~" not in element:
                continue
            pattern = r'~~([^~]+?)~~'
            if not re.search(pattern, element):
                continue

            new_content = []
            last_end = 0
            for match in re.finditer(pattern, element):
                if match.start() > last_end:
                    new_content.append(element[last_end:match.start()])

                del_tag = soup.new_tag("del")
                del_tag.string = match.group(1)
                new_content.append(del_tag)
                last_end = match.end()

            if last_end < len(element):
                new_content.append(element[last_end:])

            parent = element.parent
            if not parent:
                continue
            index = parent.contents.index(element)
            element.extract()
            for i, item in enumerate(new_content):
                if isinstance(item, str):
                    parent.insert(index + i, NavigableString(item))
                else:
                    parent.insert(index + i, item)


def _clean_latex_br_tags(soup) -> None:
    """
    清理 HTML 中 LaTeX 公式块内的 <br> 标签。
    
    LaTeX 公式块通常包裹在 class="katex" 或 class="katex-display" 的元素中，
    公式内容的 <br> 标签会破坏 LaTeX 语法，需要移除或替换为换行符。
    
    Args:
        soup: BeautifulSoup 对象，会被原地修改。
    """  
    # 查找所有包含 katex 的元素（行内公式和块级公式）
    katex_elements = soup.find_all(class_=re.compile(r'katex'))
    
    for katex_elem in katex_elements:
        # 在 katex 元素内查找所有 <br> 标签
        br_tags = katex_elem.find_all('br')
        
        for br in br_tags:
            # 删除 <br> 标签
            br.replace_with('')


def unwrap_li_paragraphs(soup) -> None:
    """
    处理 <li><p>...</p></li>：将 li 下的直接子元素 p “展开/去壳”。

    目标：
      - <li><p>文本</p></li> => <li>文本</li>
      - 如果 <li> 里是 <p>文本</p><ul>...</ul>，则变为 <li>文本<ul>...</ul></li>
      - 尽量不动嵌套更深的 p（只处理 li 的“直接子 p”）
    """
    for li in soup.find_all("li"):
        # 找出 li 的直接子节点里是 <p> 的那些
        direct_ps = [c for c in li.contents if getattr(c, "name", None) == "p"]
        if not direct_ps:
            continue

        for p in direct_ps:
            p.unwrap()

        # 清一下 li 开头结尾可能多出来的空白文本节点
        _trim_whitespace_text_nodes(li)


def remove_empty_paragraphs(soup) -> None:
    """
    删除空 <p>：
      - 只有空白
      - 或只有 &nbsp; / \u00a0
      - 或只包含空白的 span/br 等（尽量温和：只在“可判定为空”时删除）
    """
    for p in soup.find_all("p"):
        text = p.get_text(strip=True).replace("\u00a0", "").strip()
        # 如果完全没内容，并且没有 img/iframe 等“非文本但有意义”的元素
        has_meaningful_media = bool(p.find(["img", "iframe", "video", "audio", "svg"]))
        if (not text) and (not has_meaningful_media):
            p.decompose()


def _trim_whitespace_text_nodes(tag) -> None:
    """
    去掉某个 tag 开头/结尾的纯空白 NavigableString，避免 unwrap 后出现奇怪空白。
    """
    # 头部
    while tag.contents and isinstance(tag.contents[0], NavigableString) and not str(tag.contents[0]).strip():
        tag.contents[0].extract()
    # 尾部
    while tag.contents and isinstance(tag.contents[-1], NavigableString) and not str(tag.contents[-1]).strip():
        tag.contents[-1].extract()


def postprocess_pandoc_html(html: str) -> str:
    """
    后处理 Pandoc 输出的 HTML，修复格式问题。
    
    处理内容：
    1. 修复代码块格式（移除属性标记，恢复换行）
    2. 清理 data-* 属性（如 data-start, data-end）
    
    Args:
        html: Pandoc 输出的 HTML 文本
        
    Returns:
        后处理后的 HTML 文本
    """
    soup = BeautifulSoup(html, "html.parser")
    
    # 修复粗体加斜体的嵌套标签（WPS 兼容性）
    _fix_bold_italic_nesting(soup)
    
    # 修复代码块格式
    _fix_pandoc_code_blocks(soup)
    
    # 清理多余的属性
    _clean_pandoc_attributes(soup)
    
    return str(soup)


def _fix_bold_italic_nesting(soup) -> None:
    """
    修复粗体加斜体的嵌套标签，以兼容 WPS。
    
    将 <strong><em>text</em></strong> 或 <em><strong>text</strong></em>
    转换为 <span style="font-weight: bold; font-style: italic;">text</span>
    
    WPS 对嵌套的 <strong><em> 标签支持不好，只会显示斜体效果。
    使用 inline style 可以确保粗体和斜体效果同时生效。
    
    Args:
        soup: BeautifulSoup 对象，会被原地修改。
    """
    # 处理 <strong><em>text</em></strong> 模式
    for strong in soup.find_all('strong'):
        # 检查 strong 标签是否只包含一个 em 标签
        children = [c for c in strong.children if c.name or (isinstance(c, NavigableString) and c.strip())]
        if len(children) == 1 and children[0].name == 'em':
            em = children[0]
            text = em.get_text()
            
            # 创建新的 span 标签，使用 inline style
            span = soup.new_tag('span', style='font-weight: bold; font-style: italic;')
            span.string = text
            
            # 替换原来的 strong 标签
            strong.replace_with(span)
    
    # 处理 <em><strong>text</strong></em> 模式
    for em in soup.find_all('em'):
        # 检查 em 标签是否只包含一个 strong 标签
        children = [c for c in em.children if c.name or (isinstance(c, NavigableString) and c.strip())]
        if len(children) == 1 and children[0].name == 'strong':
            strong = children[0]
            text = strong.get_text()
            
            # 创建新的 span 标签，使用 inline style
            span = soup.new_tag('span', style='font-weight: bold; font-style: italic;')
            span.string = text
            
            # 替换原来的 em 标签
            em.replace_with(span)


def _fix_pandoc_code_blocks(soup) -> None:
    """
    修复 Pandoc 输出的代码块格式问题。
    
    Pandoc 在某些情况下会将代码块输出为：
    <p><code>{.class! attr="value"} actual code here</code></p>
    
    需要转换为：
    <pre><code>actual code here</code></pre>
    
    同时恢复代码中的换行。
    
    Args:
        soup: BeautifulSoup 对象，会被原地修改。
    """
    # 查找所有 <p> 标签中包含 <code> 的情况
    for p in soup.find_all('p'):
        # 获取 p 标签的所有子节点（排除纯空白文本节点）
        meaningful_contents = [
            c for c in p.contents 
            if c.name or (isinstance(c, NavigableString) and c.strip())
        ]
        
        # 检查 p 是否只包含一个 code 标签
        code_tags = p.find_all('code', recursive=False)
        if len(code_tags) == 1 and len(meaningful_contents) == 1:
            code = code_tags[0]
            code_text = code.get_text()
            
            # 检查是否包含 Pandoc 属性标记（以 { 开头）
            if code_text.strip().startswith('{'):
                # 尝试提取属性和实际代码
                # 格式：{.class! attr="value"} actual code here
                match = re.match(r'^\{[^}]+\}\s*(.+)$', code_text, re.DOTALL)
                if match:
                    actual_code = match.group(1)
                    
                    # 恢复代码中的换行
                    # Pandoc 将多行代码压缩成单行，用多个空格代替换行
                    # 检测连续的多个空格（通常是 4+ 空格），替换为换行+缩进
                    actual_code = re.sub(r'    +', '\n    ', actual_code)
                    
                    # 创建新的 pre > code 结构
                    pre = soup.new_tag('pre')
                    new_code = soup.new_tag('code')
                    new_code.string = actual_code
                    pre.append(new_code)
                    
                    # 替换原来的 p 标签
                    p.replace_with(pre)


def _clean_pandoc_attributes(soup) -> None:
    """
    清理 Pandoc 输出的 HTML 中的额外属性。
    
    移除：
    - data-start, data-end（来自某些 Markdown 编辑器的位置信息）
    - 其他 data-* 属性
    
    Args:
        soup: BeautifulSoup 对象，会被原地修改。
    """
    for tag in soup.find_all(True):
        # 移除所有 data-* 属性
        attrs_to_del = [attr for attr in tag.attrs if attr.startswith('data-')]
        for attr in attrs_to_del:
            del tag.attrs[attr]

