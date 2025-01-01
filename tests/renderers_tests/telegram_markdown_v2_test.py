import mistune
from mistune.plugins.formatting import strikethrough

from mistune_telegram import TelegramMarkdownV2Renderer

formater = mistune.create_markdown(renderer=TelegramMarkdownV2Renderer(), plugins=[strikethrough])


def test_heading() -> None:
    """Test heading."""

    # Base syntax
    assert formater("# Heading level 1") == "*Heading level 1*\n"
    assert formater("## Heading level 2") == "*Heading level 2*\n"
    assert formater("### Heading level 3") == "*Heading level 3*\n"
    assert formater("#### Heading level 4") == "*Heading level 4*\n"
    assert formater("##### Heading level 5") == "*Heading level 5*\n"
    assert formater("###### Heading level 6") == "*Heading level 6*\n"

    # Alternate syntax
    assert formater("Heading level 1\n===============") == "*Heading level 1*\n"
    assert formater("Heading level 2\n---------------") == "*Heading level 2*\n"


def test_strong() -> None:
    """Test bold."""

    assert formater("**bold**") == "*bold*\n"
    assert formater("__bold__") == "*bold*\n"


def test_emphasis() -> None:
    """Test italic."""

    assert formater("*italic*") == "_italic_\n"
    assert formater("_italic_") == "_italic_\n"


def test_link() -> None:
    """Test link."""

    assert formater("[example](http://www.example.com/)") == "[example](http://www.example.com/)\n"


def test_codespan() -> None:
    """Test code."""

    assert formater("`code`") == "`code`\n"


def test_block_code() -> None:
    """Test code block."""

    assert formater("```\ncode block\n```") == "```\ncode block\n```\n"
    assert formater("```python\ncode block\n```") == "```python\ncode block\n```\n"


def test_strikethrough() -> None:
    """Test strikethrough."""

    assert formater("~~strikethrough~~") == "~strikethrough~\n"
