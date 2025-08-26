---
title: "Example OG Social Image"
publishDate: "27 January 2023"
description: "An example post for Astro Cactus, detailing how to add a custom social image card in the frontmatter"
tags: ["example", "blog", "image"]
ogImage: "/social-card.png"
---
<picture>
  <source type="image/jxl" srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1317/v1756208885/pavlo-talpa-chaiir-ocean.jpg 50w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1317/v1756208885/pavlo-talpa-chaiir-ocean.jpg 1014w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1317/v1756208885/pavlo-talpa-chaiir-ocean.jpg 1317w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1317/v1756208885/pavlo-talpa-chaiir-ocean.jpg 1553w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1317/v1756208885/pavlo-talpa-chaiir-ocean.jpg 1600w
  " sizes="(max-width: 1600px) 100vw, 1600px">
  <source type="image/avif" srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1317/v1756208885/pavlo-talpa-chaiir-ocean.jpg 50w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1317/v1756208885/pavlo-talpa-chaiir-ocean.jpg 963w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1317/v1756208885/pavlo-talpa-chaiir-ocean.jpg 1251w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1317/v1756208885/pavlo-talpa-chaiir-ocean.jpg 1475w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1317/v1756208885/pavlo-talpa-chaiir-ocean.jpg 1600w
  " sizes="(max-width: 1600px) 100vw, 1600px">
  <source type="image/jpeg" srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1317/v1756208885/pavlo-talpa-chaiir-ocean.jpg 50w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1317/v1756208885/pavlo-talpa-chaiir-ocean.jpg 1065w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1317/v1756208885/pavlo-talpa-chaiir-ocean.jpg 825w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1317/v1756208885/pavlo-talpa-chaiir-ocean.jpg 1383w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1317/v1756208885/pavlo-talpa-chaiir-ocean.jpg 1600w
  " sizes="(max-width: 1600px) 100vw, 1600px">
  <img
    src="https://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1600/v1756208885/pavlo-talpa-chaiir-ocean.jpg"
    srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1317/v1756208885/pavlo-talpa-chaiir-ocean.jpg 50w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1317/v1756208885/pavlo-talpa-chaiir-ocean.jpg 1014w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1317/v1756208885/pavlo-talpa-chaiir-ocean.jpg 1317w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1317/v1756208885/pavlo-talpa-chaiir-ocean.jpg 1553w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/q_auto/c_scale,w_1317/v1756208885/pavlo-talpa-chaiir-ocean.jpg 1600w
  "
    sizes="(max-width: 1600px) 100vw, 1600px"
    width="1860"
    height="2792"
    alt="Responsive pavlo-talpa-chaiir-ocean"
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
  <em>Photo by <a href="https://unsplash.com/photos/a-lone-chair-sits-in-a-shallow-body-of-water-ZLms1AcFjMQ?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash">Pavlo Talpa</a> on</em>
  <svg class="icon" xmlns="https://www.w3.org/2000/svg" viewBox="0 0 448 512">
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
