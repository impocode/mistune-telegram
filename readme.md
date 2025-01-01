# Mistune Telegram

Plugin mistune for converting Markdown into Telegram format.

## Supported Markdown elements

|  Markdown element  | Telegram Markdown  | Telegram Markdown V2 | Telegram HTML |
| :----------------: | :---------------:  | :------------------: | :-----------: |
|      Headings      | :white_check_mark: |  :white_check_mark:  |      :x:      |
|     Paragraphs     | :white_check_mark: |  :white_check_mark:  |      :x:      |
|     Line Breaks    | :white_check_mark: |  :white_check_mark:  |      :x:      |
|        Bold        | :white_check_mark: |  :white_check_mark:  |      :x:      |
|       Italic       | :white_check_mark: |  :white_check_mark:  |      :x:      |
|     Blockquotes    |         :x:        |         :x:          |      :x:      |
|       Lists        |         :x:        |         :x:          |      :x:      |
|        Code        | :white_check_mark: |  :white_check_mark:  |      :x:      |
|     Code blocks    | :white_check_mark: |  :white_check_mark:  |      :x:      |
|  Horizontal rules  |         :x:        |         :x:          |      :x:      |
|        Links       | :white_check_mark: |  :white_check_mark:  |      :x:      |
|       Images       |         :x:        |         :x:          |      :x:      |

## Install

```shell
$ pip install mistune-telegram
```

Or use your python package manager.

## Usage

[Markdown style](https://core.telegram.org/bots/api#markdown-style) example:

````python
import mistune
from mistune_telegram import TelegramMarkdownRenderer
telegram_style = mistune.create_markdown(renderer=TelegramMarkdownRenderer())

print(telegram_style(
"""
# Heading level 1
## Heading level 2
### Heading level 3
#### Heading level 4
##### Heading level 5
###### Heading level 6

Heading level 1
===============
Heading level 2
---------------

First paragraph.

Second paragraph.

First line.
Second line.

**bold**
__bold__

*italic*
_italic_

`code`

```
code blocks
```

```python
code blocks written in the Python programming language
```

[link](http://www.example.com/)

"""))
````

Output:

````
*Heading level 1*

*Heading level 2*

*Heading level 3*

*Heading level 4*

*Heading level 5*

*Heading level 6*

*Heading level 1*

*Heading level 2*

First paragraph.

Second paragraph.

First line.
Second line.

*bold*
*bold*

_italic_
_italic_

`code`

```
code blocks
```

```python
code blocks written in the Python programming language
```

[link](http://www.example.com/)
````

[MarkdownV2 style](https://core.telegram.org/bots/api#markdownv2-style) example:

````python
import mistune
from mistune.plugins.formatting import strikethrough
from mistune_telegram import TelegramMarkdownV2Renderer

telegram_style = mistune.create_markdown(renderer=TelegramMarkdownV2Renderer(), plugins=[strikethrough])

print(telegram_style(
"""
# Heading level 1
## Heading level 2
### Heading level 3
#### Heading level 4
##### Heading level 5
###### Heading level 6

Heading level 1
===============
Heading level 2
---------------

First paragraph.

Second paragraph.

First line.
Second line.

**bold**
__bold__

*italic*
_italic_

`code`

```
code blocks
```

```python
code blocks written in the Python programming language
```

[link](http://www.example.com/)

~~strikethrough~~

"""))
````

Output:

````
*Heading level 1*

*Heading level 2*

*Heading level 3*

*Heading level 4*

*Heading level 5*

*Heading level 6*

*Heading level 1*

*Heading level 2*

First paragraph.

Second paragraph.

First line.
Second line.

*bold*
*bold*

_italic_
_italic_

`code`

```
code blocks
```

```python
code blocks written in the Python programming language
```

[link](http://www.example.com/)

~strikethrough~

````
