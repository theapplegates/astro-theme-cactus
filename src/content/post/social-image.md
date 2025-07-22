---
title: "Example OG Social Image"
publishDate: "27 January 2023"
description: "An example post for Astro Cactus, detailing how to add a custom social image card in the frontmatter"
tags: ["example", "blog", "image"]
ogImage: "/social-card.png"
---

## Adding your own social image to a post

<picture>
  <source type="image/avif" srcset="
        https://res.cloudinary.com/paulapplegate-com/image/upload/f_avif,w_50/evokujxkfmhnyjeowv15.avif 50w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_avif,w_312/evokujxkfmhnyjeowv15.avif 312w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_avif,w_679/evokujxkfmhnyjeowv15.avif 679w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_avif,w_712/evokujxkfmhnyjeowv15.avif 712w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_avif,w_818/evokujxkfmhnyjeowv15.avif 818w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_avif,w_910/evokujxkfmhnyjeowv15.avif 910w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_avif,w_982/evokujxkfmhnyjeowv15.avif 982w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_avif,w_993/evokujxkfmhnyjeowv15.avif 993w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_avif,w_995/evokujxkfmhnyjeowv15.avif 995w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_avif,w_1000/evokujxkfmhnyjeowv15.avif 1000w
  " sizes="100vw">
  <source type="image/jxl" srcset="
        https://res.cloudinary.com/paulapplegate-com/image/upload/f_jxl,w_50/evokujxkfmhnyjeowv15.jxl 50w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_jxl,w_312/evokujxkfmhnyjeowv15.jxl 312w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_jxl,w_679/evokujxkfmhnyjeowv15.jxl 679w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_jxl,w_712/evokujxkfmhnyjeowv15.jxl 712w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_jxl,w_818/evokujxkfmhnyjeowv15.jxl 818w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_jxl,w_910/evokujxkfmhnyjeowv15.jxl 910w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_jxl,w_982/evokujxkfmhnyjeowv15.jxl 982w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_jxl,w_993/evokujxkfmhnyjeowv15.jxl 993w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_jxl,w_995/evokujxkfmhnyjeowv15.jxl 995w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_jxl,w_1000/evokujxkfmhnyjeowv15.jxl 1000w
  " sizes="100vw">
  <img
        src="https://res.cloudinary.com/paulapplegate-com/image/upload/f_jpg,w_50/evokujxkfmhnyjeowv15.jpg"
        srcset="
        https://res.cloudinary.com/paulapplegate-com/image/upload/f_jpg,w_50/evokujxkfmhnyjeowv15.jpg 50w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_jpg,w_312/evokujxkfmhnyjeowv15.jpg 312w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_jpg,w_679/evokujxkfmhnyjeowv15.jpg 679w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_jpg,w_712/evokujxkfmhnyjeowv15.jpg 712w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_jpg,w_818/evokujxkfmhnyjeowv15.jpg 818w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_jpg,w_910/evokujxkfmhnyjeowv15.jpg 910w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_jpg,w_982/evokujxkfmhnyjeowv15.jpg 982w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_jpg,w_993/evokujxkfmhnyjeowv15.jpg 993w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_jpg,w_995/evokujxkfmhnyjeowv15.jpg 995w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/f_jpg,w_1000/evokujxkfmhnyjeowv15.jpg 1000w
  "
        sizes="100vw"
        alt="Responsive evokujxkfmhnyjeowv15"
        loading="lazy"
        decoding="async">
</picture>

This post is an example of how to add a custom [open graph](https://ogp.me/) social image, also known as an OG image, to a blog post.
By adding the optional ogImage property to the frontmatter of a post, you opt out of [satori](https://github.com/vercel/satori) automatically generating an image for this page.

If you open this markdown file `src/content/post/social-image.md` you'll see the ogImage property set to an image which lives in the public folder[^1].

```yaml
ogImage: "/social-card.png"
```

You can view the one set for this template page [here](https://astro-cactus.chriswilliams.dev/social-card.png).

[^1]: The image itself can be located anywhere you like.
