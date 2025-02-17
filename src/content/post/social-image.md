---
title: "Example OG Social Image"
publishDate: "27 January 2023"
description: "An example post for Astro Cactus, detailing how to add a custom social image card in the frontmatter"
tags: ["example", "blog", "image"]
ogImage: "/social-card.png"
---
<div class="shadow-wrapper">
  <picture class="responsive-picture">
    <source type="image/jxl" srcset="
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_2150/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jxl 2150w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_2070/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jxl 2070w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1989/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jxl 1989w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1906/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jxl 1906w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1816/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jxl 1816w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1724/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jxl 1724w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1639/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jxl 1639w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1410/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jxl 1410w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1370/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jxl 1370w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1307/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jxl 1307w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_874/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jxl 874w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_827/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jxl 827w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_693/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jxl 693w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_514/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jxl 514w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_250/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jxl 250w
    " sizes="(min-width: 1200px) 1200px, 100vw"/>
    <source type="image/avif" srcset="
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_2150/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.avif 2150w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_2070/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.avif 2070w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1989/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.avif 1989w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1906/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.avif 1906w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1816/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.avif 1816w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1724/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.avif 1724w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1639/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.avif 1639w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1410/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.avif 1410w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1370/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.avif 1370w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1307/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.avif 1307w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_874/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.avif 874w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_827/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.avif 827w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_693/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.avif 693w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_514/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.avif 514w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_250/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.avif 250w
    " sizes="(min-width: 1200px) 1200px, 100vw"/>
    <source type="image/jpeg" srcset="
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_2150/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jpeg 2150w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_2070/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jpeg 2070w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1989/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jpeg 1989w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1906/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jpeg 1906w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1816/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jpeg 1816w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1724/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jpeg 1724w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1639/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jpeg 1639w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1410/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jpeg 1410w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1370/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jpeg 1370w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_1307/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jpeg 1307w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_874/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jpeg 874w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_827/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jpeg 827w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_693/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jpeg 693w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_514/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jpeg 514w,
      https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_250/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jpeg 250w
    " sizes="(min-width: 1200px) 1200px, 100vw"/>
    <img src="https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto,x_20,y_20/c_scale,w_250/x_20,y_20/v1739822772/lju6lldkylsvrj85ipus.jxl" alt="Responsive Image" loading="lazy"/>
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
