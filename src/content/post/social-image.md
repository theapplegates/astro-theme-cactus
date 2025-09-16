---
title: "Example OG Social Image"
publishDate: "27 January 2023"
description: "An example post for Astro Cactus, detailing how to add a custom social image card in the frontmatter"
tags: ["example", "blog", "image"]
ogImage: "/social-card.png"
---
<picture>
  <source type="image/jxl" srcset="
    http://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1062/v1756088440/mos-design-sfnoj6c3ysw-unsplash.jpg 50w,
    http://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1062/v1756088440/mos-design-sfnoj6c3ysw-unsplash.jpg 710w,
    http://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1062/v1756088440/mos-design-sfnoj6c3ysw-unsplash.jpg 1062w,
    http://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1062/v1756088440/mos-design-sfnoj6c3ysw-unsplash.jpg 1393w,
    http://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1062/v1756088440/mos-design-sfnoj6c3ysw-unsplash.jpg 1600w
  " sizes="(max-width: 1600px) 100vw, 1600px">
  <source type="image/jpeg" srcset="
    http://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1062/v1756088440/mos-design-sfnoj6c3ysw-unsplash.jpg 50w,
    http://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1062/v1756088440/mos-design-sfnoj6c3ysw-unsplash.jpg 746w,
    http://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1062/v1756088440/mos-design-sfnoj6c3ysw-unsplash.jpg 1115w,
    http://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1062/v1756088440/mos-design-sfnoj6c3ysw-unsplash.jpg 1463w,
    http://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1062/v1756088440/mos-design-sfnoj6c3ysw-unsplash.jpg 1600w
  " sizes="(max-width: 1600px) 100vw, 1600px">
  <img
    src="http://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1600/v1756088440/mos-design-sfnoj6c3ysw-unsplash.jpg"
    srcset="
    http://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1062/v1756088440/mos-design-sfnoj6c3ysw-unsplash.jpg 50w,
    http://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1062/v1756088440/mos-design-sfnoj6c3ysw-unsplash.jpg 710w,
    http://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1062/v1756088440/mos-design-sfnoj6c3ysw-unsplash.jpg 1062w,
    http://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1062/v1756088440/mos-design-sfnoj6c3ysw-unsplash.jpg 1393w,
    http://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1062/v1756088440/mos-design-sfnoj6c3ysw-unsplash.jpg 1600w
  "
    sizes="(max-width: 1600px) 100vw, 1600px"
    width="4000"
    height="6000"
    alt="Responsive mos-design-SfnOJ6c3ySw-unsplash"
    loading="lazy"
    decoding="async">
</picture>


## Adding your own social image to a post

This post is an example of how to add a custom [open graph](https://ogp.me/) social image, also known as an OG image, to a blog post.
By adding the optional ogImage property to the frontmatter of a post, you opt out of [satori](https://github.com/vercel/satori) automatically generating an image for this page.

If you open this markdown file `src/content/post/social-image.md` you'll see the ogImage property set to an image which lives in the public folder[^1].

```yaml
ogImage: "/social-card.png"
```

You can view the one set for this template page [here](https://astro-cactus.chriswilliams.dev/social-card.png).

[^1]: The image itself can be located anywhere you like.
