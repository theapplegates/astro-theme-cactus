---
title: "Example OG Social Image"
publishDate: "27 January 2023"
description: "An example post for Astro Cactus, detailing how to add a custom social image card in the frontmatter"
tags: ["example", "blog", "image"]
ogImage: "/social-card.png"
---

## Adding your own social image to a post

<picture>
  <source type="image/jxl"
      srcset="https://res.cloudinary.com/paulapplegate-com/image/upload/w_1000,f_jxl/v1751379823/rm8wyl2v6reu8lzdodxa.jxl 1000w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/w_800,f_jxl/v1751379823/rm8wyl2v6reu8lzdodxa.jxl 800w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/w_640,f_jxl/v1751379823/rm8wyl2v6reu8lzdodxa.jxl 640w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/w_512,f_jxl/v1751379823/rm8wyl2v6reu8lzdodxa.jxl 512w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/w_410,f_jxl/v1751379823/rm8wyl2v6reu8lzdodxa.jxl 410w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/w_328,f_jxl/v1751379823/rm8wyl2v6reu8lzdodxa.jxl 328w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/w_262,f_jxl/v1751379823/rm8wyl2v6reu8lzdodxa.jxl 262w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/w_210,f_jxl/v1751379823/rm8wyl2v6reu8lzdodxa.jxl 210w"
      sizes="(max-width: 1000px) 1000px, (max-width: 800px) 800px, (max-width: 640px) 640px, (max-width: 512px) 512px, (max-width: 410px) 410px, (max-width: 328px) 328px, (max-width: 262px) 262px, 210px">
  <source type="image/avif"
      srcset="https://res.cloudinary.com/paulapplegate-com/image/upload/w_1000,f_avif/v1751379823/rm8wyl2v6reu8lzdodxa.avif 1000w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/w_800,f_avif/v1751379823/rm8wyl2v6reu8lzdodxa.avif 800w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/w_640,f_avif/v1751379823/rm8wyl2v6reu8lzdodxa.avif 640w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/w_512,f_avif/v1751379823/rm8wyl2v6reu8lzdodxa.avif 512w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/w_410,f_avif/v1751379823/rm8wyl2v6reu8lzdodxa.avif 410w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/w_328,f_avif/v1751379823/rm8wyl2v6reu8lzdodxa.avif 328w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/w_262,f_avif/v1751379823/rm8wyl2v6reu8lzdodxa.avif 262w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/w_210,f_avif/v1751379823/rm8wyl2v6reu8lzdodxa.avif 210w"
      sizes="(max-width: 1000px) 1000px, (max-width: 800px) 800px, (max-width: 640px) 640px, (max-width: 512px) 512px, (max-width: 410px) 410px, (max-width: 328px) 328px, (max-width: 262px) 262px, 210px">
  <source srcset="https://res.cloudinary.com/paulapplegate-com/image/upload/w_1000,f_jpg/v1751379823/rm8wyl2v6reu8lzdodxa.jpg 1000w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/w_800,f_jpg/v1751379823/rm8wyl2v6reu8lzdodxa.jpg 800w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/w_640,f_jpg/v1751379823/rm8wyl2v6reu8lzdodxa.jpg 640w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/w_512,f_jpg/v1751379823/rm8wyl2v6reu8lzdodxa.jpg 512w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/w_410,f_jpg/v1751379823/rm8wyl2v6reu8lzdodxa.jpg 410w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/w_328,f_jpg/v1751379823/rm8wyl2v6reu8lzdodxa.jpg 328w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/w_262,f_jpg/v1751379823/rm8wyl2v6reu8lzdodxa.jpg 262w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/w_210,f_jpg/v1751379823/rm8wyl2v6reu8lzdodxa.jpg 210w"
      sizes="(max-width: 1000px) 1000px, (max-width: 800px) 800px, (max-width: 640px) 640px, (max-width: 512px) 512px, (max-width: 410px) 410px, (max-width: 328px) 328px, (max-width: 262px) 262px, 210px">
  <img src="https://res.cloudinary.com/paulapplegate-com/image/upload/w_1000,f_jpg/v1751379823/rm8wyl2v6reu8lzdodxa.jpg"
     alt="Responsive image"
     loading="lazy">
</picture>

This post is an example of how to add a custom [open graph](https://ogp.me/) social image, also known as an OG image, to a blog post.
By adding the optional ogImage property to the frontmatter of a post, you opt out of [satori](https://github.com/vercel/satori) automatically generating an image for this page.

If you open this markdown file `src/content/post/social-image.md` you'll see the ogImage property set to an image which lives in the public folder[^1].

```yaml
ogImage: "/social-card.png"
```

You can view the one set for this template page [here](https://astro-cactus.chriswilliams.dev/social-card.png).

[^1]: The image itself can be located anywhere you like.
