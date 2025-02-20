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



<div class="shadow-wrapper">
<picture class="responsive-picture">
  <!-- Desktop (≥1200px) - Original aspect ratio -->
  <source media="(min-width: 1200px)" type="image/jxl"
          sizes="40vw"
          srcset="
            https://res.cloudinary.com/.../c_scale,w_860/dpr_1.0/... 860w,
            https://res.cloudinary.com/.../c_scale,w_860/dpr_2.0/... 1720w,
            <!-- ... other width variants ... -->
          ">
  <source media="(min-width: 1200px)" type="image/avif"
          sizes="40vw"
          srcset="
            https://res.cloudinary.com/.../c_scale,w_860/dpr_1.0/... 860w,
            https://res.cloudinary.com/.../c_scale,w_860/dpr_2.0/... 1720w,
            <!-- ... other width variants ... -->
          ">
  <source media="(min-width: 1200px)" type="image/jpeg"
          sizes="40vw"
          srcset="
            https://res.cloudinary.com/.../c_scale,w_860/dpr_1.0/... 860w,
            https://res.cloudinary.com/.../c_scale,w_860/dpr_2.0/... 1720w,
            <!-- ... other width variants ... -->
          ">

  <!-- Small laptops (992-1199px) - 16:9 aspect ratio -->
  <source media="(min-width: 992px) and (max-width: 1199px)" type="image/jxl"
          sizes="60vw"
          srcset="
            https://res.cloudinary.com/.../ar_16:9,c_fill,w_1290/dpr_1.0/... 1290w,
            https://res.cloudinary.com/.../ar_16:9,c_fill,w_1290/dpr_2.0/... 2580w,
            <!-- ... other width variants ... -->
          ">
  <source media="(min-width: 992px) and (max-width: 1199px)" type="image/avif"
          sizes="60vw"
          srcset="
            https://res.cloudinary.com/.../ar_16:9,c_fill,w_1290/dpr_1.0/... 1290w,
            https://res.cloudinary.com/.../ar_16:9,c_fill,w_1290/dpr_2.0/... 2580w,
            <!-- ... other width variants ... -->
          ">
  <source media="(min-width: 992px) and (max-width: 1199px)" type="image/jpeg"
          sizes="60vw"
          srcset="
            https://res.cloudinary.com/.../ar_16:9,c_fill,w_1290/dpr_1.0/... 1290w,
            https://res.cloudinary.com/.../ar_16:9,c_fill,w_1290/dpr_2.0/... 2580w,
            <!-- ... other width variants ... -->
          ">

  <!-- Tablets (768-991px) - 4:3 aspect ratio -->
  <source media="(min-width: 768px) and (max-width: 991px)" type="image/jxl"
          sizes="70vw"
          srcset="
            https://res.cloudinary.com/.../ar_4:3,c_fill,w_700/dpr_1.0/... 700w,
            https://res.cloudinary.com/.../ar_4:3,c_fill,w_700/dpr_2.0/... 1400w,
            <!-- ... other width variants ... -->
          ">
  <source media="(min-width: 768px) and (max-width: 991px)" type="image/avif"
          sizes="70vw"
          srcset="
            https://res.cloudinary.com/.../ar_4:3,c_fill,w_700/dpr_1.0/... 700w,
            https://res.cloudinary.com/.../ar_4:3,c_fill,w_700/dpr_2.0/... 1400w,
            <!-- ... other width variants ... -->
          ">
  <source media="(min-width: 768px) and (max-width: 991px)" type="image/jpeg"
          sizes="70vw"
          srcset="
            https://res.cloudinary.com/.../ar_4:3,c_fill,w_700/dpr_1.0/... 700w,
            https://res.cloudinary.com/.../ar_4:3,c_fill,w_700/dpr_2.0/... 1400w,
            <!-- ... other width variants ... -->
          ">

  <!-- Smartphones (<767px) - 1:1 aspect ratio -->
  <source media="(max-width: 767px)" type="image/jxl"
          sizes="100vw"
          srcset="
            https://res.cloudinary.com/.../ar_1:1,c_fill,w_400/dpr_1.0/... 400w,
            https://res.cloudinary.com/.../ar_1:1,c_fill,w_400/dpr_2.0/... 800w,
            <!-- ... other width variants ... -->
          ">
  <source media="(max-width: 767px)" type="image/avif"
          sizes="100vw"
          srcset="
            https://res.cloudinary.com/.../ar_1:1,c_fill,w_400/dpr_1.0/... 400w,
            https://res.cloudinary.com/.../ar_1:1,c_fill,w_400/dpr_2.0/... 800w,
            <!-- ... other width variants ... -->
          ">
  <source media="(max-width: 767px)" type="image/jpeg"
          sizes="100vw"
          srcset="
            https://res.cloudinary.com/.../ar_1:1,c_fill,w_400/dpr_1.0/... 400w,
            https://res.cloudinary.com/.../ar_1:1,c_fill,w_400/dpr_2.0/... 800w,
            <!-- ... other width variants ... -->
          ">

  <img src="fallback.jpg" alt="Descriptive alt text" loading="lazy">
</picture>
</div>
