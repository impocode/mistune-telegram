from typing import Any, Optional

from mistune.renderers.html import HTMLRenderer
from mistune.util import escape, safe_entity


class TelegramHTMLRenderer(HTMLRenderer):
    """Markdown to Telegram HTML converter."""

    NAME = "telegram_html"

    def heading(self, text: str, level: int, **attrs: Any) -> str:
        """Convert Markdown heading to Telegram HTML format."""
        return "<strong>" + text + "</strong>\n\n"

    def paragraph(self, text: str) -> str:
        """Convert Markdown paragraph to Telegram HTML format."""
        return text + "\n\n"

    def linebreak(self) -> str:
        """Convert Markdown line break to Telegram HTML format."""
        return "\n"

    def block_code(self, code: str, info: Optional[str] = None) -> str:
        """Convert Markdown code block to Telegram HTML format."""
        html = "<pre"
        if info is not None:
            info = safe_entity(info.strip())
        if info:
            lang = info.split(None, 1)[0]
            html += '><code class="language-' + lang + '"'
            return html + ">" + escape(code) + "</code></pre>\n"
        else:
            return html + ">" + escape(code) + "</pre>\n"

    def strikethrough(self, text: str) -> str:
        """Convert Markdown strikethrough to Telegram HTML format."""
        return "<del>" + text + "</del>"


__all__ = ["TelegramHTMLRenderer"]
