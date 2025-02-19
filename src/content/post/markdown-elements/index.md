---
title: "A post of Markdown elements"
description: "This post is for testing and listing a number of different markdown elements"
publishDate: "22 Feb 2023"
updatedDate: 22 Jan 2024
tags: ["test", "markdown"]
---

## This is a H2 Heading

### This is a H3 Heading

#### This is a H4 Heading

##### This is a H5 Heading

###### This is a H6 Heading

## Horizontal Rules

---

---

---

## Emphasis

**This is bold text**

_This is italic text_

~~Strikethrough~~

## Quotes

"Double quotes" and 'single quotes'

## Blockquotes

> Blockquotes can also be nested...
>
> > ...by using additional greater-than signs right next to each other...

## References

An example containing a clickable reference[^1] with a link to the source.

Second example containing a reference[^2] with a link to the source.

[^1]: Reference first footnote with a return to content link.

[^2]: Second reference with a link.

If you check out this example in `src/content/post/markdown-elements/index.md`, you'll notice that the references and the heading "Footnotes" are added to the bottom of the page via the [remark-rehype](https://github.com/remarkjs/remark-rehype#options) plugin.

## Lists

Unordered

- Create a list by starting a line with `+`, `-`, or `*`
- Sub-lists are made by indenting 2 spaces:
  - Marker character change forces new list start:
    - Ac tristique libero volutpat at
    - Facilisis in pretium nisl aliquet
    - Nulla volutpat aliquam velit
- Very easy!

Ordered

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa

4. You can use sequential numbers...
5. ...or keep all the numbers as `1.`

Start numbering with offset:

57. foo
1. bar

## Code

Inline `code`

Indented code

    // Some comments
    line 1 of code
    line 2 of code
    line 3 of code

Block code "fences"

```
Sample text here...
```

Syntax highlighting

```js
var foo = function (bar) {
	return bar++;
};

console.log(foo(5));
```

### Expressive code examples

Adding a title

```js title="file.js"
console.log("Title example");
```

A bash terminal

```bash
echo "A base terminal example"
```

Highlighting code lines

```js title="line-markers.js" del={2} ins={3-4} {6}
function demo() {
	console.log("this line is marked as deleted");
	// This line and the next one are marked as inserted
	console.log("this is the second inserted line");

	return "this line uses the neutral default marker type";
}
```

[Expressive Code](https://expressive-code.com/) can do a ton more than shown here, and includes a lot of [customisation](https://expressive-code.com/reference/configuration/).

## Tables

| Option | Description                                                               |
| ------ | ------------------------------------------------------------------------- |
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default.    |
| ext    | extension to be used for dest files.                                      |

### Table Alignment

| Item         | Price | # In stock |
| ------------ | :---: | ---------: |
| Juicy Apples | 1.99  |        739 |
| Bananas      | 1.89  |          6 |

### Keyboard elements

| Action                | Shortcut                                   |
| --------------------- | ------------------------------------------ |
| Vertical split        | <kbd>Alt+Shift++</kbd>                     |
| Horizontal split      | <kbd>Alt+Shift+-</kbd>                     |
| Auto split            | <kbd>Alt+Shift+d</kbd>                     |
| Switch between splits | <kbd>Alt</kbd> + arrow keys                |
| Resizing a split      | <kbd>Alt+Shift</kbd> + arrow keys          |
| Close a split         | <kbd>Ctrl+Shift+W</kbd>                    |
| Maximize a pane       | <kbd>Ctrl+Shift+P</kbd> + Toggle pane zoom |

## Images

Image in the same folder: `src/content/post/markdown-elements/logo.png`

![Astro theme cactus logo](./logo.png)

## Links

[Content from markdown-it](https://markdown-it.github.io/)



A test image with a jxl extension.

/Users/thor4/.zshenv:.:1: no such file or directory: /Users/thor4/.cargo/env
gpg-agent: a gpg-agent is already running - not starting a new one
thor4@Mac newcode-feb19 % source venv/bin/activate
(venv) thor4@Mac newcode-feb19 % Pip3 install  python-dotenv
Collecting python-dotenv
  Using cached python_dotenv-1.0.1-py3-none-any.whl.metadata (23 kB)
Downloading python_dotenv-1.0.1-py3-none-any.whl (19 kB)
Installing collected packages: python-dotenv
Successfully installed python-dotenv-1.0.1

[notice] A new release of pip is available: 25.0 -> 25.0.1
[notice] To update, run: pip install --upgrade pip
(venv) thor4@Mac newcode-feb19 % pip3 install cloudinary
Requirement already satisfied: cloudinary in ./venv/lib/python3.13/site-packages (1.42.2)
Requirement already satisfied: six in ./venv/lib/python3.13/site-packages (from cloudinary) (1.17.0)
Requirement already satisfied: urllib3>=1.26.5 in ./venv/lib/python3.13/site-packages (from cloudinary) (2.3.0)
Requirement already satisfied: certifi in ./venv/lib/python3.13/site-packages (from cloudinary) (2025.1.31)

[notice] A new release of pip is available: 25.0 -> 25.0.1
[notice] To update, run: pip install --upgrade pip
(venv) thor4@Mac newcode-feb19 % python3 GoogleScript-Dec20-2024-NO-Shadow.py maksym-mazur-VjxDMq6pt8M-unsplash.jxl
Uploading maksym-mazur-VjxDMq6pt8M-unsplash.jxl to Cloudinary...
Upload complete. Generating HTML...
Responsive HTML written to output.html
(venv) thor4@Mac newcode-feb19 % cat output.html
<div class="shadow-wrapper">
<picture class="responsive-picture">
  <source type="image/jxl" srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_2150/v1739996062/u0xwz8kghs1idnggr4cq.jxl 2150w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_2145/v1739996062/u0xwz8kghs1idnggr4cq.jxl 2145w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_2060/v1739996062/u0xwz8kghs1idnggr4cq.jxl 2060w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_1987/v1739996062/u0xwz8kghs1idnggr4cq.jxl 1987w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_1848/v1739996062/u0xwz8kghs1idnggr4cq.jxl 1848w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_1695/v1739996062/u0xwz8kghs1idnggr4cq.jxl 1695w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_1521/v1739996062/u0xwz8kghs1idnggr4cq.jxl 1521w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_1427/v1739996062/u0xwz8kghs1idnggr4cq.jxl 1427w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_1480/v1739996062/u0xwz8kghs1idnggr4cq.jxl 1480w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_935/v1739996062/u0xwz8kghs1idnggr4cq.jxl 935w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_868/v1739996062/u0xwz8kghs1idnggr4cq.jxl 868w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_744/v1739996062/u0xwz8kghs1idnggr4cq.jxl 744w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_615/v1739996062/u0xwz8kghs1idnggr4cq.jxl 615w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_457/v1739996062/u0xwz8kghs1idnggr4cq.jxl 457w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_250/v1739996062/u0xwz8kghs1idnggr4cq.jxl 250w
  " sizes="(min-width: 1200px) 1200px, 100vw"/>
  <source type="image/avif" srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_2150/v1739996062/u0xwz8kghs1idnggr4cq.avif 2150w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_2145/v1739996062/u0xwz8kghs1idnggr4cq.avif 2145w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_2060/v1739996062/u0xwz8kghs1idnggr4cq.avif 2060w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_1987/v1739996062/u0xwz8kghs1idnggr4cq.avif 1987w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_1848/v1739996062/u0xwz8kghs1idnggr4cq.avif 1848w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_1695/v1739996062/u0xwz8kghs1idnggr4cq.avif 1695w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_1521/v1739996062/u0xwz8kghs1idnggr4cq.avif 1521w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_1427/v1739996062/u0xwz8kghs1idnggr4cq.avif 1427w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_1480/v1739996062/u0xwz8kghs1idnggr4cq.avif 1480w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_935/v1739996062/u0xwz8kghs1idnggr4cq.avif 935w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_868/v1739996062/u0xwz8kghs1idnggr4cq.avif 868w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_744/v1739996062/u0xwz8kghs1idnggr4cq.avif 744w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_615/v1739996062/u0xwz8kghs1idnggr4cq.avif 615w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_457/v1739996062/u0xwz8kghs1idnggr4cq.avif 457w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_250/v1739996062/u0xwz8kghs1idnggr4cq.avif 250w
  " sizes="(min-width: 1200px) 1200px, 100vw"/>
  <source type="image/jpeg" srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_2150/v1739996062/u0xwz8kghs1idnggr4cq.jpeg 2150w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_2145/v1739996062/u0xwz8kghs1idnggr4cq.jpeg 2145w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_2060/v1739996062/u0xwz8kghs1idnggr4cq.jpeg 2060w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_1987/v1739996062/u0xwz8kghs1idnggr4cq.jpeg 1987w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_1848/v1739996062/u0xwz8kghs1idnggr4cq.jpeg 1848w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_1695/v1739996062/u0xwz8kghs1idnggr4cq.jpeg 1695w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_1521/v1739996062/u0xwz8kghs1idnggr4cq.jpeg 1521w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_1427/v1739996062/u0xwz8kghs1idnggr4cq.jpeg 1427w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_1480/v1739996062/u0xwz8kghs1idnggr4cq.jpeg 1480w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_935/v1739996062/u0xwz8kghs1idnggr4cq.jpeg 935w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_868/v1739996062/u0xwz8kghs1idnggr4cq.jpeg 868w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_744/v1739996062/u0xwz8kghs1idnggr4cq.jpeg 744w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_615/v1739996062/u0xwz8kghs1idnggr4cq.jpeg 615w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_457/v1739996062/u0xwz8kghs1idnggr4cq.jpeg 457w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_250/v1739996062/u0xwz8kghs1idnggr4cq.jpeg 250w
  " sizes="(min-width: 1200px) 1200px, 100vw"/>
  <img src="https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_250/v1739996062/u0xwz8kghs1idnggr4cq.jxl" alt="Responsive Image" loading="lazy"></img>
</picture>
</div>
