import mistune

from mistune_telegram import TelegramMarkdownRenderer

formater = mistune.create_markdown(renderer=TelegramMarkdownRenderer())


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


def test_paragraphs() -> None:
    """Test paragraphs."""

    assert (
        formater("First paragraph.\n\nSecond paragraph.")
        == "First paragraph.\n\nSecond paragraph.\n"
    )


def test_line_breaks() -> None:
    """Test line breaks."""

    assert formater("First line.\nSecond line.") == "First line.\nSecond line.\n"


def test_bold() -> None:
    """Test bold."""

    assert formater("**bold**") == "*bold*\n"
    assert formater("__bold__") == "*bold*\n"


def test_italic() -> None:
    """Test italic."""

    assert formater("*italic*") == "_italic_\n"
    assert formater("_italic_") == "_italic_\n"


def test_code() -> None:
    """Test code."""

    assert formater("`code`") == "`code`\n"


def test_code_blocks() -> None:
    """Test code blocks."""

    assert formater("```\ncode block\n```") == "```\ncode block\n```\n"
    assert formater("```python\ncode block\n```") == "```python\ncode block\n```\n"


def test_links() -> None:
    """Test links."""

    assert formater("[example](http://www.example.com/)") == "[example](http://www.example.com/)\n"
