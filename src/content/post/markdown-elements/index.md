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







Uploading arno-moller-mash.jxl to Cloudinary...
Upload complete. Generating HTML...
Responsive HTML written to output.html
Art direction setup:
- Desktop (≥1200px): Original aspect ratio, 40% width
- Small laptops (992-1199px): 16:9 aspect ratio, 60% width
- Tablets (768-991px): 4:3 aspect ratio, 70% width
- Smartphones (<767px): 1:1 aspect ratio, 100% width
All image variations include both standard (1x) and Retina (2x) resolutions
(venv) thor4@Pauls-MacBook-Pro Usethis-mar7 %

<div class="shadow-wrapper">
<picture class="responsive-picture">
  <source media="(min-width: 1200px)" type="image/jxl" srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_860/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 860w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_860/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1720w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_856/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 856w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_856/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1712w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_857/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 857w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_857/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1714w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_831/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 831w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_831/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1662w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_800/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 800w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_800/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1600w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_769/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 769w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_769/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1538w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_729/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 729w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_729/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1458w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_689/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 689w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_689/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1378w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_667/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 667w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_667/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1334w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_637/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 637w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_637/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1274w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_386/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 386w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_386/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 772w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_369/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 369w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_369/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 738w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_308/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 308w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_308/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 616w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_214/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 214w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_214/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 428w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_100/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 100w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_100/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 200w
  " sizes="(min-width: 1200px) 40vw, 100vw"/>
  <source media="(min-width: 1200px)" type="image/avif" srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_860/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 860w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_860/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1720w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_856/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 856w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_856/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1712w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_857/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 857w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_857/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1714w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_831/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 831w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_831/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1662w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_800/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 800w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_800/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1600w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_769/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 769w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_769/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1538w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_729/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 729w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_729/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1458w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_689/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 689w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_689/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1378w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_667/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 667w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_667/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1334w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_637/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 637w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_637/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1274w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_386/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 386w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_386/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 772w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_369/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 369w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_369/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 738w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_308/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 308w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_308/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 616w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_214/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 214w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_214/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 428w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_100/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 100w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_100/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 200w
  " sizes="(min-width: 1200px) 40vw, 100vw"/>
  <source media="(min-width: 1200px)" type="image/jpeg" srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_860/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 860w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_860/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1720w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_856/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 856w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_856/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1712w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_857/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 857w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_857/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1714w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_831/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 831w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_831/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1662w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_800/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 800w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_800/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1600w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_769/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 769w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_769/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1538w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_729/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 729w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_729/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1458w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_689/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 689w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_689/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1378w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_667/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 667w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_667/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1334w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_637/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 637w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_637/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1274w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_386/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 386w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_386/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 772w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_369/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 369w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_369/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 738w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_308/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 308w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_308/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 616w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_214/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 214w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_214/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 428w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_100/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 100w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_scale,w_100/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 200w
  " sizes="(min-width: 1200px) 40vw, 100vw"/>
  <source media="(min-width: 992px) and (max-width: 1199px)" type="image/jxl" srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1290/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1290w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1290/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 2580w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1284/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1284w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1284/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 2568w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1286/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1286w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1286/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 2572w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1247/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1247w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1247/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 2494w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1201/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1201w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1201/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 2402w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1153/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1153w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1153/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 2306w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1094/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1094w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1094/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 2188w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1034/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1034w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1034/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 2068w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1000/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1000w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1000/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 2000w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_955/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 955w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_955/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1910w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_579/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 579w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_579/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1158w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_553/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 553w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_553/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1106w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_462/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 462w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_462/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 924w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_321/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 321w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_321/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 642w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_150/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 150w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_150/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 300w
  " sizes="(min-width: 1200px) 60vw, 100vw"/>
  <source media="(min-width: 992px) and (max-width: 1199px)" type="image/avif" srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1290/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1290w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1290/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 2580w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1284/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1284w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1284/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 2568w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1286/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1286w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1286/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 2572w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1247/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1247w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1247/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 2494w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1201/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1201w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1201/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 2402w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1153/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1153w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1153/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 2306w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1094/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1094w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1094/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 2188w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1034/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1034w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1034/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 2068w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1000/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1000w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1000/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 2000w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_955/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 955w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_955/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1910w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_579/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 579w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_579/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1158w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_553/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 553w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_553/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1106w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_462/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 462w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_462/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 924w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_321/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 321w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_321/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 642w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_150/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 150w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_150/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 300w
  " sizes="(min-width: 1200px) 60vw, 100vw"/>
  <source media="(min-width: 992px) and (max-width: 1199px)" type="image/jpeg" srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1290/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1290w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1290/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 2580w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1284/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1284w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1284/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 2568w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1286/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1286w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1286/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 2572w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1247/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1247w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1247/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 2494w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1201/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1201w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1201/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 2402w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1153/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1153w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1153/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 2306w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1094/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1094w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1094/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 2188w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1034/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1034w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1034/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 2068w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1000/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1000w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_1000/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 2000w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_955/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 955w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_955/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1910w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_579/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 579w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_579/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1158w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_553/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 553w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_553/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1106w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_462/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 462w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_462/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 924w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_321/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 321w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_321/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 642w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_150/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 150w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_16:9/c_scale,w_150/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 300w
  " sizes="(min-width: 1200px) 60vw, 100vw"/>
  <source media="(min-width: 768px) and (max-width: 991px)" type="image/jxl" srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1505/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1505w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1505/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 3010w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1498/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1498w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1498/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 2996w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1500/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1500w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1500/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 3000w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1455/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1455w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1455/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 2910w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1401/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1401w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1401/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 2802w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1346/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1346w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1346/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 2692w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1276/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1276w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1276/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 2552w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1206/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1206w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1206/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 2412w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1167/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1167w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1167/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 2334w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1115/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1115w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1115/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 2230w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_675/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 675w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_675/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1350w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_646/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 646w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_646/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1292w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_539/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 539w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_539/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1078w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_374/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 374w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_374/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 748w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_175/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 175w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_175/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 350w
  " sizes="(min-width: 1200px) 70vw, 100vw"/>
  <source media="(min-width: 768px) and (max-width: 991px)" type="image/avif" srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1505/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1505w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1505/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 3010w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1498/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1498w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1498/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 2996w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1500/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1500w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1500/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 3000w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1455/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1455w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1455/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 2910w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1401/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1401w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1401/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 2802w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1346/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1346w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1346/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 2692w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1276/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1276w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1276/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 2552w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1206/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1206w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1206/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 2412w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1167/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1167w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1167/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 2334w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1115/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1115w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1115/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 2230w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_675/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 675w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_675/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1350w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_646/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 646w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_646/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1292w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_539/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 539w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_539/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1078w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_374/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 374w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_374/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 748w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_175/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 175w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_175/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 350w
  " sizes="(min-width: 1200px) 70vw, 100vw"/>
  <source media="(min-width: 768px) and (max-width: 991px)" type="image/jpeg" srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1505/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1505w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1505/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 3010w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1498/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1498w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1498/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 2996w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1500/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1500w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1500/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 3000w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1455/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1455w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1455/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 2910w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1401/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1401w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1401/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 2802w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1346/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1346w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1346/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 2692w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1276/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1276w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1276/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 2552w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1206/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1206w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1206/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 2412w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1167/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1167w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1167/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 2334w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1115/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1115w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_1115/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 2230w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_675/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 675w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_675/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1350w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_646/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 646w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_646/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1292w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_539/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 539w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_539/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1078w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_374/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 374w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_374/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 748w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_175/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 175w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_4:3/c_scale,w_175/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 350w
  " sizes="(min-width: 1200px) 70vw, 100vw"/>
  <source media="(max-width: 767px)" type="image/jxl" srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2150/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 2150w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2150/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 4300w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2140/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 2140w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2140/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 4280w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2144/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 2144w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2144/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 4288w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2079/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 2079w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2079/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 4158w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2002/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 2002w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2002/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 4004w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1923/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1923w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1923/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 3846w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1824/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1824w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1824/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 3648w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1724/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1724w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1724/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 3448w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1668/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1668w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1668/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 3336w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1593/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1593w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1593/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 3186w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_965/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 965w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_965/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1930w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_923/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 923w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_923/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1846w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_770/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 770w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_770/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1540w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_535/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 535w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_535/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 1070w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_250/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 250w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_250/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jxl 500w
  " sizes="(min-width: 1200px) 100vw, 100vw"/>
  <source media="(max-width: 767px)" type="image/avif" srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2150/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 2150w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2150/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 4300w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2140/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 2140w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2140/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 4280w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2144/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 2144w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2144/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 4288w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2079/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 2079w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2079/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 4158w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2002/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 2002w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2002/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 4004w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1923/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1923w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1923/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 3846w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1824/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1824w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1824/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 3648w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1724/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1724w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1724/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 3448w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1668/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1668w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1668/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 3336w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1593/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1593w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1593/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 3186w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_965/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 965w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_965/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1930w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_923/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 923w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_923/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1846w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_770/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 770w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_770/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1540w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_535/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 535w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_535/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 1070w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_250/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 250w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_250/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.avif 500w
  " sizes="(min-width: 1200px) 100vw, 100vw"/>
  <source media="(max-width: 767px)" type="image/jpeg" srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2150/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 2150w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2150/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 4300w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2140/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 2140w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2140/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 4280w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2144/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 2144w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2144/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 4288w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2079/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 2079w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2079/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 4158w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2002/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 2002w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_2002/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 4004w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1923/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1923w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1923/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 3846w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1824/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1824w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1824/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 3648w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1724/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1724w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1724/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 3448w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1668/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1668w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1668/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 3336w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1593/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1593w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_1593/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 3186w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_965/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 965w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_965/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1930w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_923/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 923w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_923/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1846w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_770/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 770w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_770/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1540w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_535/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 535w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_535/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 1070w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_250/e_shadow:75,x_20,y_20/dpr_1.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 250w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_250/e_shadow:75,x_20,y_20/dpr_2.0/v1741986514/hgsjqzapmwghbrs9dlji.jpeg 500w
  " sizes="(min-width: 1200px) 100vw, 100vw"/>
  <img src="https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,ar_1:1/c_scale,w_250/e_shadow:75,x_20,y_20/v1741986514/hgsjqzapmwghbrs9dlji.jxl" alt="Responsive Image" loading="lazy"></img>
</picture>
</div>
<style>
  .credit-container {
    font-size: 10px;
    font-style: italic;
    display: flex;
    align-items: center;
    flex-wrap: wrap;
  }
  .icon {
    width: 1em;
    height: 1em;
    margin-left: 0.25em;
  }
</style>
<p class="credit-container">
  <em>Photo by <a href="https://unsplash.com/photos/a-close-up-of-a-giraffe-with-a-sky-background-mxm0wNN-Sjg?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash">Arno Moller</a> on</em>
  <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
    <path d="M448,230.17V480H0V230.17H141.13V355.09H306.87V230.17ZM306.87,32H141.13V156.91H306.87Z"/>
  </svg>
</p>
