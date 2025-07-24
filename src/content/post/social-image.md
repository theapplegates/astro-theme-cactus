---
title: "Example OG Social Image"
publishDate: "27 January 2023"
description: "An example post for Astro Cactus, detailing how to add a custom social image card in the frontmatter"
tags: ["example", "blog", "image"]
ogImage: "/social-card.png"
---

## Adding your own social image to a post

<picture>
  <source type="image/jxl" srcset="
        https://res.cloudinary.com/paulapplegate-com/image/upload/f_jxl,w_2000/nbynep79t6pfkpkgflm9.jxl 2000w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_jxl,w_1866/nbynep79t6pfkpkgflm9.jxl 1866w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_jxl,w_1235/nbynep79t6pfkpkgflm9.jxl 1235w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_jxl,w_200/nbynep79t6pfkpkgflm9.jxl 200w
  " sizes="100vw">
  <source type="image/avif" srcset="
        https://res.cloudinary.com/paulapplegate-com/image/upload/f_avif,w_2000/nbynep79t6pfkpkgflm9.avif 2000w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_avif,w_1866/nbynep79t6pfkpkgflm9.avif 1866w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_avif,w_1235/nbynep79t6pfkpkgflm9.avif 1235w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_avif,w_200/nbynep79t6pfkpkgflm9.avif 200w
  " sizes="100vw">
  <source type="image/jpeg" srcset="
          https://res.cloudinary.com/paulapplegate-com/image/upload/f_jpeg,w_2000/nbynep79t6pfkpkgflm9.jpeg 2000w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_jpeg,w_1866/nbynep79t6pfkpkgflm9.jpeg 1866w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_jpeg,w_1235/nbynep79t6pfkpkgflm9.jpeg 1235w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_jpeg,w_200/nbynep79t6pfkpkgflm9.jpeg 200w
        " sizes="100vw">
  <img
        src="https://res.cloudinary.com/paulapplegate-com/image/upload/f_jpg,w_2000/nbynep79t6pfkpkgflm9.jpg"
        srcset="
        https://res.cloudinary.com/paulapplegate-com/image/upload/f_jpg,w_2000/nbynep79t6pfkpkgflm9.jpg 2000w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_jpg,w_1866/nbynep79t6pfkpkgflm9.jpg 1866w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_jpg,w_1235/nbynep79t6pfkpkgflm9.jpg 1235w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_jpg,w_200/nbynep79t6pfkpkgflm9.jpg 200w
  "
        sizes="100vw"
        alt="Responsive nbynep79t6pfkpkgflm9"
        loading="lazy"
        decoding="async">
</picture>
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
  <em>Photo by <a href="https://unsplash.com/photos/a-woman-running-down-a-dirt-road-next-to-the-ocean-uOtxvT_LuGg?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash">Daniel J. Schwarz</a> on</em>
  <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
    <path d="M448,230.17V480H0V230.17H141.13V355.09H306.87V230.17ZM306.87,32H141.13V156.91H306.87Z"/>
  </svg>
</p>

This post is an example of how to add a custom [open graph](https://ogp.me/) social image, also known as an OG image, to a blog post.
By adding the optional ogImage property to the frontmatter of a post, you opt out of [satori](https://github.com/vercel/satori) automatically generating an image for this page.

If you open this markdown file `src/content/post/social-image.md` you'll see the ogImage property set to an image which lives in the public folder[^1].

```yaml
ogImage: "/social-card.png"
```

You can view the one set for this template page [here](https://astro-cactus.chriswilliams.dev/social-card.png).

[^1]: The image itself can be located anywhere you like.
