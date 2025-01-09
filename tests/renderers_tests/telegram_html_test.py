import mistune
from mistune.plugins.formatting import strikethrough

from mistune_telegram import TelegramHTMLRenderer

formater = mistune.create_markdown(renderer=TelegramHTMLRenderer(), plugins=[strikethrough])


def test_heading() -> None:
    """Test heading."""

    # Base syntax
    assert formater("# Heading level 1") == "<strong>Heading level 1</strong>\n\n"
    assert formater("## Heading level 2") == "<strong>Heading level 2</strong>\n\n"
    assert formater("### Heading level 3") == "<strong>Heading level 3</strong>\n\n"
    assert formater("#### Heading level 4") == "<strong>Heading level 4</strong>\n\n"
    assert formater("##### Heading level 5") == "<strong>Heading level 5</strong>\n\n"
    assert formater("###### Heading level 6") == "<strong>Heading level 6</strong>\n\n"

    # Alternate syntax
    assert formater("Heading level 1\n===============") == "<strong>Heading level 1</strong>\n\n"
    assert formater("Heading level 2\n---------------") == "<strong>Heading level 2</strong>\n\n"


def test_paragraphs() -> None:
    """Test paragraphs."""

    assert (
        formater("First paragraph.\n\nSecond paragraph.")
        == "First paragraph.\n\nSecond paragraph.\n\n"
    )


def test_line_breaks() -> None:
    """Test line breaks."""

    assert formater("First line.\nSecond line.") == "First line.\nSecond line.\n\n"


def test_bold() -> None:
    """Test bold."""

    assert formater("**bold**") == "<strong>bold</strong>\n\n"
    assert formater("__bold__") == "<strong>bold</strong>\n\n"


def test_italic() -> None:
    """Test italic."""

    assert formater("*italic*") == "<em>italic</em>\n\n"
    assert formater("_italic_") == "<em>italic</em>\n\n"


def test_code() -> None:
    """Test code."""

    assert formater("`code`") == "<code>code</code>\n\n"


def test_code_blocks() -> None:
    """Test code blocks."""

    assert formater("```\ncode block\n```") == "<pre>code block\n</pre>\n"
    assert (
        formater("```python\ncode block\n```")
        == '<pre><code class="language-python">code block\n</code></pre>\n'
    )


def test_links() -> None:
    """Test links."""

    assert (
        formater("[example](http://www.example.com/)")
        == '<a href="http://www.example.com/">example</a>\n\n'
    )


def test_strikethrough() -> None:
    """Test strikethrough."""

    assert formater("~~strikethrough~~") == "<del>strikethrough</del>\n\n"
