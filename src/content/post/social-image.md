---
title: "Example OG Social Image"
publishDate: "27 January 2023"
description: "An example post for Astro Cactus, detailing how to add a custom social image card in the frontmatter"
tags: ["example", "blog", "image"]
ogImage: "/social-card.png"
---

import { Source } from "@unpic/astro";


<picture class="hero">
  <!-- Large screens get a full-width hero image -->
  <Source
    src="https://images.unsplash.com/photo-1694406805270-f3a93e91f4b6"
    media="(min-width: 601px)"
    layout="fullWidth"
  />
  <!-- Small screens get a constrained square image -->
  <Source
    src="https://images.unsplash.com/photo-1693711942336-f4f9963bd364"
    media="(max-width: 600px)"
    width={600}
    height={600}
  />
  <!-- Always include an Image as the final element -->
  <Image
    src="https://images.unsplash.com/photo-1693711942336-f4f9963bd364"
    width={600}
    height={600}
    alt="Aurora"
    unstyled
  />
</picture>

<style>
  /* Style for all layouts */
  .hero img {
    object-fit: cover;
    width: 100%;
  }

  @media (min-width: 601px) {
    /* Style for full-width layout */
    .hero img {
      height: 600px;
    }
  }
  @media (max-width: 600px) {
    /* Style for constrained layout */
    .hero img {
      max-width: 600px;
      /* Set the image aspect-ratio */
      aspect-ratio: 1/1;
    }
  }
</style>

<div class="shadow-wrapper">
<picture>
  <source type="image/jxl" srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_2150/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jxl 2150w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_2140/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jxl 2140w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_2135/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jxl 2135w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_2037/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jxl 2037w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1927/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jxl 1927w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1836/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jxl 1836w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1700/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jxl 1700w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1629/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jxl 1629w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1454/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jxl 1454w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1371/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jxl 1371w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1239/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jxl 1239w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1064/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jxl 1064w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1052/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jxl 1052w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_635/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jxl 635w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_561/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jxl 561w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_474/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jxl 474w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_472/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jxl 472w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_250/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jxl 250w
  "/>
  <source type="image/avif" srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_2150/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.avif 2150w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_2140/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.avif 2140w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_2135/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.avif 2135w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_2037/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.avif 2037w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1927/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.avif 1927w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1836/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.avif 1836w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1700/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.avif 1700w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1629/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.avif 1629w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1454/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.avif 1454w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1371/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.avif 1371w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1239/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.avif 1239w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1064/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.avif 1064w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1052/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.avif 1052w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_635/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.avif 635w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_561/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.avif 561w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_474/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.avif 474w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_472/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.avif 472w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_250/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.avif 250w
  "/>
  <source type="image/jpeg" srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_2150/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jpeg 2150w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_2140/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jpeg 2140w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_2135/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jpeg 2135w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_2037/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jpeg 2037w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1927/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jpeg 1927w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1836/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jpeg 1836w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1700/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jpeg 1700w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1629/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jpeg 1629w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1454/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jpeg 1454w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1371/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jpeg 1371w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1239/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jpeg 1239w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1064/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jpeg 1064w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1052/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jpeg 1052w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_635/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jpeg 635w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_561/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jpeg 561w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_474/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jpeg 474w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_472/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jpeg 472w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_250/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jpeg 250w
  "/>
  <img src="https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_250/e_shadow:75,x_20,y_20/v1732397292/u7wtobd2hs6ahk8pmidx.jxl" alt="Responsive Image">
</picture>
</div>

<style>
  .credit-container {
    font-size: 12px;
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
  <em>Photo by <a href="https://news.chevrolet.com/newsroom.html">NA</a> on</em>
  <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
    <path d="M448,230.17V480H0V230.17H141.13V355.09H306.87V230.17ZM306.87,32H141.13V156.91H306.87Z"/>
  </svg>
</p>

## Adding your own social image to a post

This post is an example of how to add a custom [open graph](https://ogp.me/) social image, also known as an OG image, to a blog post.
By adding the optional ogImage property to the frontmatter of a post, you opt out of [satori](https://github.com/vercel/satori) automatically generating an image for this page.

If you open this markdown file `src/content/post/social-image.md` you'll see the ogImage property set to an image which lives in the public folder[^1].

```yaml
ogImage: "/social-card.png"
```

You can view the one set for this template page [here](https://astro-cactus.chriswilliams.dev/social-card.png).

[^1]: The image itself can be located anywhere you like.
