---
title: "Example OG Social Image"
publishDate: "27 January 2023"
description: "An example post for Astro Cactus, detailing how to add a custom social image card in the frontmatter"
tags: ["example", "blog", "image"]
ogImage: "/social-card.png"
---

## Adding your own social image to a post

This post is an example of how to add a custom [open graph](https://ogp.me/) social image, also known as an OG image, to a blog post.
By adding the optional ogImage property to the frontmatter of a post, you opt out of [satori](https://github.com/vercel/satori) automatically generating an image for this page.

If you open this markdown file `src/content/post/social-image.md` you'll see the ogImage property set to an image which lives in the public folder[^1].

```yaml
ogImage: "/social-card.png"
```

You can view the one set for this template page [here](https://astro-cactus.chriswilliams.dev/social-card.png).

<div class="shadow-wrapper">
  <picture class="responsive-picture">
    <source type="image/jxl" srcset="
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_2150/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.jxl 2150w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_2145/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.jxl 2145w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_2139/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.jxl 2139w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1989/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.jxl 1989w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1838/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.jxl 1838w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1521/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.jxl 1521w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1427/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.jxl 1427w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1480/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.jxl 1480w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_935/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.jxl 935w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_868/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.jxl 868w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_747/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.jxl 747w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_614/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.jxl 614w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_457/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.jxl 457w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_250/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.jxl 250w
    " sizes="(min-width: 1200px) 1200px, 100vw"/>
    <source type="image/avif" srcset="
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_2150/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.avif 2150w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_2145/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.avif 2145w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_2139/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.avif 2139w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1989/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.avif 1989w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1838/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.avif 1838w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1521/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.avif 1521w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1427/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.avif 1427w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1480/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.avif 1480w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_935/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.avif 935w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_868/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.avif 868w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_747/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.avif 747w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_614/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.avif 614w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_457/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.avif 457w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_250/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.avif 250w
    " sizes="(min-width: 1200px) 1200px, 100vw"/>
    <source type="image/jpeg" srcset="
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_2150/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.jpeg 2150w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_2145/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.jpeg 2145w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_2139/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.jpeg 2139w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1989/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.jpeg 1989w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1838/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.jpeg 1838w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1521/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.jpeg 1521w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1427/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.jpeg 1427w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1480/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.jpeg 1480w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_935/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.jpeg 935w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_868/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.jpeg 868w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_747/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.jpeg 747w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_614/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.jpeg 614w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_457/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.jpeg 457w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_250/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.jpeg 250w
    " sizes="(min-width: 1200px) 1200px, 100vw"/>
    <img src="https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_250/e_shadow:75,x_20,y_20/v1739411864/jgql9ljyx1ipak40dxzl.jxl" alt="Responsive Image" loading="lazy"/>
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
  <em>Photo by <a href="https://unsplash.com/photos/a-person-in-a-red-coat-looking-at-a-christmas-tree-VjxDMq6pt8M?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash">Maksym Mazur</a> on</em>
  <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
    <path d="M448,230.17V480H0V230.17H141.13V355.09H306.87V230.17ZM306.87,32H141.13V156.91H306.87Z"/>
  </svg>
</p>

[^1]: The image itself can be located anywhere you like.
