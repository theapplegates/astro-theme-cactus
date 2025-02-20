---
title: "Example OG Social Image"
publishDate: "27 January 2023"
description: "An example post for Astro Cactus, detailing how to add a custom social image card in the frontmatter"
tags: ["example", "blog", "image"]
ogImage: "/social-card.png"
---
<div class="shadow-wrapper">
<picture class="responsive-picture">
  <source media="(min-width: 1200px)" type="image/jxl" sizes="40vw"
          srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_2150/v1740075122/cq7g154llpa2kuttb6zc.jxl 2150w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_2150/v1740075122/cq7g154llpa2kuttb6zc.jxl 4300w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_2145/v1740075122/cq7g154llpa2kuttb6zc.jxl 2145w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_2145/v1740075122/cq7g154llpa2kuttb6zc.jxl 4290w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_2060/v1740075122/cq7g154llpa2kuttb6zc.jxl 2060w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_2060/v1740075122/cq7g154llpa2kuttb6zc.jxl 4120w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_1987/v1740075122/cq7g154llpa2kuttb6zc.jxl 1987w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_1987/v1740075122/cq7g154llpa2kuttb6zc.jxl 3974w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_1848/v1740075122/cq7g154llpa2kuttb6zc.jxl 1848w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_1848/v1740075122/cq7g154llpa2kuttb6zc.jxl 3696w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_1695/v1740075122/cq7g154llpa2kuttb6zc.jxl 1695w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_1695/v1740075122/cq7g154llpa2kuttb6zc.jxl 3390w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_1521/v1740075122/cq7g154llpa2kuttb6zc.jxl 1521w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_1521/v1740075122/cq7g154llpa2kuttb6zc.jxl 3042w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_1427/v1740075122/cq7g154llpa2kuttb6zc.jxl 1427w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_1427/v1740075122/cq7g154llpa2kuttb6zc.jxl 2854w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_1480/v1740075122/cq7g154llpa2kuttb6zc.jxl 1480w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_1480/v1740075122/cq7g154llpa2kuttb6zc.jxl 2960w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_935/v1740075122/cq7g154llpa2kuttb6zc.jxl 935w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_935/v1740075122/cq7g154llpa2kuttb6zc.jxl 1870w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_868/v1740075122/cq7g154llpa2kuttb6zc.jxl 868w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_868/v1740075122/cq7g154llpa2kuttb6zc.jxl 1736w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_744/v1740075122/cq7g154llpa2kuttb6zc.jxl 744w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_744/v1740075122/cq7g154llpa2kuttb6zc.jxl 1488w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_615/v1740075122/cq7g154llpa2kuttb6zc.jxl 615w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_615/v1740075122/cq7g154llpa2kuttb6zc.jxl 1230w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_457/v1740075122/cq7g154llpa2kuttb6zc.jxl 457w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_457/v1740075122/cq7g154llpa2kuttb6zc.jxl 914w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_250/v1740075122/cq7g154llpa2kuttb6zc.jxl 250w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_250/v1740075122/cq7g154llpa2kuttb6zc.jxl 500w
  "/>
  <source media="(min-width: 1200px)" type="image/avif" sizes="40vw"
          srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_2150/v1740075122/cq7g154llpa2kuttb6zc.avif 2150w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_2150/v1740075122/cq7g154llpa2kuttb6zc.avif 4300w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_2145/v1740075122/cq7g154llpa2kuttb6zc.avif 2145w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_2145/v1740075122/cq7g154llpa2kuttb6zc.avif 4290w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_2060/v1740075122/cq7g154llpa2kuttb6zc.avif 2060w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_2060/v1740075122/cq7g154llpa2kuttb6zc.avif 4120w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_1987/v1740075122/cq7g154llpa2kuttb6zc.avif 1987w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_1987/v1740075122/cq7g154llpa2kuttb6zc.avif 3974w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_1848/v1740075122/cq7g154llpa2kuttb6zc.avif 1848w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_1848/v1740075122/cq7g154llpa2kuttb6zc.avif 3696w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_1695/v1740075122/cq7g154llpa2kuttb6zc.avif 1695w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_1695/v1740075122/cq7g154llpa2kuttb6zc.avif 3390w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_1521/v1740075122/cq7g154llpa2kuttb6zc.avif 1521w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_1521/v1740075122/cq7g154llpa2kuttb6zc.avif 3042w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_1427/v1740075122/cq7g154llpa2kuttb6zc.avif 1427w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_1427/v1740075122/cq7g154llpa2kuttb6zc.avif 2854w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_1480/v1740075122/cq7g154llpa2kuttb6zc.avif 1480w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_1480/v1740075122/cq7g154llpa2kuttb6zc.avif 2960w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_935/v1740075122/cq7g154llpa2kuttb6zc.avif 935w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_935/v1740075122/cq7g154llpa2kuttb6zc.avif 1870w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_868/v1740075122/cq7g154llpa2kuttb6zc.avif 868w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_868/v1740075122/cq7g154llpa2kuttb6zc.avif 1736w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_744/v1740075122/cq7g154llpa2kuttb6zc.avif 744w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_744/v1740075122/cq7g154llpa2kuttb6zc.avif 1488w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_615/v1740075122/cq7g154llpa2kuttb6zc.avif 615w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_615/v1740075122/cq7g154llpa2kuttb6zc.avif 1230w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_457/v1740075122/cq7g154llpa2kuttb6zc.avif 457w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_457/v1740075122/cq7g154llpa2kuttb6zc.avif 914w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_250/v1740075122/cq7g154llpa2kuttb6zc.avif 250w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_250/v1740075122/cq7g154llpa2kuttb6zc.avif 500w
  "/>
  <source media="(min-width: 1200px)" type="image/jpeg" sizes="40vw"
          srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_2150/v1740075122/cq7g154llpa2kuttb6zc.jpeg 2150w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_2150/v1740075122/cq7g154llpa2kuttb6zc.jpeg 4300w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_2145/v1740075122/cq7g154llpa2kuttb6zc.jpeg 2145w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_2145/v1740075122/cq7g154llpa2kuttb6zc.jpeg 4290w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_2060/v1740075122/cq7g154llpa2kuttb6zc.jpeg 2060w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_2060/v1740075122/cq7g154llpa2kuttb6zc.jpeg 4120w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_1987/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1987w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_1987/v1740075122/cq7g154llpa2kuttb6zc.jpeg 3974w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_1848/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1848w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_1848/v1740075122/cq7g154llpa2kuttb6zc.jpeg 3696w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_1695/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1695w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_1695/v1740075122/cq7g154llpa2kuttb6zc.jpeg 3390w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_1521/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1521w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_1521/v1740075122/cq7g154llpa2kuttb6zc.jpeg 3042w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_1427/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1427w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_1427/v1740075122/cq7g154llpa2kuttb6zc.jpeg 2854w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_1480/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1480w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_1480/v1740075122/cq7g154llpa2kuttb6zc.jpeg 2960w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_935/v1740075122/cq7g154llpa2kuttb6zc.jpeg 935w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_935/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1870w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_868/v1740075122/cq7g154llpa2kuttb6zc.jpeg 868w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_868/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1736w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_744/v1740075122/cq7g154llpa2kuttb6zc.jpeg 744w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_744/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1488w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_615/v1740075122/cq7g154llpa2kuttb6zc.jpeg 615w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_615/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1230w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_457/v1740075122/cq7g154llpa2kuttb6zc.jpeg 457w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_457/v1740075122/cq7g154llpa2kuttb6zc.jpeg 914w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_1.0/c_scale,w_250/v1740075122/cq7g154llpa2kuttb6zc.jpeg 250w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/dpr_2.0/c_scale,w_250/v1740075122/cq7g154llpa2kuttb6zc.jpeg 500w
  "/>
  <source media="(min-width: 992px) and (max-width: 1199px)" type="image/jxl" sizes="60vw"
          srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_2150/v1740075122/cq7g154llpa2kuttb6zc.jxl 2150w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_2150/v1740075122/cq7g154llpa2kuttb6zc.jxl 4300w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_2145/v1740075122/cq7g154llpa2kuttb6zc.jxl 2145w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_2145/v1740075122/cq7g154llpa2kuttb6zc.jxl 4290w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_2060/v1740075122/cq7g154llpa2kuttb6zc.jxl 2060w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_2060/v1740075122/cq7g154llpa2kuttb6zc.jxl 4120w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1987/v1740075122/cq7g154llpa2kuttb6zc.jxl 1987w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1987/v1740075122/cq7g154llpa2kuttb6zc.jxl 3974w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1848/v1740075122/cq7g154llpa2kuttb6zc.jxl 1848w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1848/v1740075122/cq7g154llpa2kuttb6zc.jxl 3696w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1695/v1740075122/cq7g154llpa2kuttb6zc.jxl 1695w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1695/v1740075122/cq7g154llpa2kuttb6zc.jxl 3390w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1521/v1740075122/cq7g154llpa2kuttb6zc.jxl 1521w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1521/v1740075122/cq7g154llpa2kuttb6zc.jxl 3042w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1427/v1740075122/cq7g154llpa2kuttb6zc.jxl 1427w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1427/v1740075122/cq7g154llpa2kuttb6zc.jxl 2854w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1480/v1740075122/cq7g154llpa2kuttb6zc.jxl 1480w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1480/v1740075122/cq7g154llpa2kuttb6zc.jxl 2960w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_935/v1740075122/cq7g154llpa2kuttb6zc.jxl 935w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_935/v1740075122/cq7g154llpa2kuttb6zc.jxl 1870w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_868/v1740075122/cq7g154llpa2kuttb6zc.jxl 868w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_868/v1740075122/cq7g154llpa2kuttb6zc.jxl 1736w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_744/v1740075122/cq7g154llpa2kuttb6zc.jxl 744w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_744/v1740075122/cq7g154llpa2kuttb6zc.jxl 1488w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_615/v1740075122/cq7g154llpa2kuttb6zc.jxl 615w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_615/v1740075122/cq7g154llpa2kuttb6zc.jxl 1230w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_457/v1740075122/cq7g154llpa2kuttb6zc.jxl 457w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_457/v1740075122/cq7g154llpa2kuttb6zc.jxl 914w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_250/v1740075122/cq7g154llpa2kuttb6zc.jxl 250w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_250/v1740075122/cq7g154llpa2kuttb6zc.jxl 500w
  "/>
  <source media="(min-width: 992px) and (max-width: 1199px)" type="image/avif" sizes="60vw"
          srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_2150/v1740075122/cq7g154llpa2kuttb6zc.avif 2150w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_2150/v1740075122/cq7g154llpa2kuttb6zc.avif 4300w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_2145/v1740075122/cq7g154llpa2kuttb6zc.avif 2145w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_2145/v1740075122/cq7g154llpa2kuttb6zc.avif 4290w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_2060/v1740075122/cq7g154llpa2kuttb6zc.avif 2060w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_2060/v1740075122/cq7g154llpa2kuttb6zc.avif 4120w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1987/v1740075122/cq7g154llpa2kuttb6zc.avif 1987w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1987/v1740075122/cq7g154llpa2kuttb6zc.avif 3974w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1848/v1740075122/cq7g154llpa2kuttb6zc.avif 1848w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1848/v1740075122/cq7g154llpa2kuttb6zc.avif 3696w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1695/v1740075122/cq7g154llpa2kuttb6zc.avif 1695w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1695/v1740075122/cq7g154llpa2kuttb6zc.avif 3390w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1521/v1740075122/cq7g154llpa2kuttb6zc.avif 1521w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1521/v1740075122/cq7g154llpa2kuttb6zc.avif 3042w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1427/v1740075122/cq7g154llpa2kuttb6zc.avif 1427w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1427/v1740075122/cq7g154llpa2kuttb6zc.avif 2854w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1480/v1740075122/cq7g154llpa2kuttb6zc.avif 1480w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1480/v1740075122/cq7g154llpa2kuttb6zc.avif 2960w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_935/v1740075122/cq7g154llpa2kuttb6zc.avif 935w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_935/v1740075122/cq7g154llpa2kuttb6zc.avif 1870w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_868/v1740075122/cq7g154llpa2kuttb6zc.avif 868w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_868/v1740075122/cq7g154llpa2kuttb6zc.avif 1736w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_744/v1740075122/cq7g154llpa2kuttb6zc.avif 744w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_744/v1740075122/cq7g154llpa2kuttb6zc.avif 1488w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_615/v1740075122/cq7g154llpa2kuttb6zc.avif 615w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_615/v1740075122/cq7g154llpa2kuttb6zc.avif 1230w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_457/v1740075122/cq7g154llpa2kuttb6zc.avif 457w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_457/v1740075122/cq7g154llpa2kuttb6zc.avif 914w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_250/v1740075122/cq7g154llpa2kuttb6zc.avif 250w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_250/v1740075122/cq7g154llpa2kuttb6zc.avif 500w
  "/>
  <source media="(min-width: 992px) and (max-width: 1199px)" type="image/jpeg" sizes="60vw"
          srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_2150/v1740075122/cq7g154llpa2kuttb6zc.jpeg 2150w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_2150/v1740075122/cq7g154llpa2kuttb6zc.jpeg 4300w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_2145/v1740075122/cq7g154llpa2kuttb6zc.jpeg 2145w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_2145/v1740075122/cq7g154llpa2kuttb6zc.jpeg 4290w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_2060/v1740075122/cq7g154llpa2kuttb6zc.jpeg 2060w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_2060/v1740075122/cq7g154llpa2kuttb6zc.jpeg 4120w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1987/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1987w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1987/v1740075122/cq7g154llpa2kuttb6zc.jpeg 3974w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1848/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1848w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1848/v1740075122/cq7g154llpa2kuttb6zc.jpeg 3696w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1695/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1695w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1695/v1740075122/cq7g154llpa2kuttb6zc.jpeg 3390w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1521/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1521w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1521/v1740075122/cq7g154llpa2kuttb6zc.jpeg 3042w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1427/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1427w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1427/v1740075122/cq7g154llpa2kuttb6zc.jpeg 2854w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1480/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1480w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1480/v1740075122/cq7g154llpa2kuttb6zc.jpeg 2960w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_935/v1740075122/cq7g154llpa2kuttb6zc.jpeg 935w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_935/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1870w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_868/v1740075122/cq7g154llpa2kuttb6zc.jpeg 868w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_868/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1736w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_744/v1740075122/cq7g154llpa2kuttb6zc.jpeg 744w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_744/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1488w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_615/v1740075122/cq7g154llpa2kuttb6zc.jpeg 615w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_615/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1230w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_457/v1740075122/cq7g154llpa2kuttb6zc.jpeg 457w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_457/v1740075122/cq7g154llpa2kuttb6zc.jpeg 914w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_250/v1740075122/cq7g154llpa2kuttb6zc.jpeg 250w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_250/v1740075122/cq7g154llpa2kuttb6zc.jpeg 500w
  "/>
  <source media="(min-width: 768px) and (max-width: 991px)" type="image/jxl" sizes="70vw"
          srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_2150/v1740075122/cq7g154llpa2kuttb6zc.jxl 2150w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_2150/v1740075122/cq7g154llpa2kuttb6zc.jxl 4300w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_2145/v1740075122/cq7g154llpa2kuttb6zc.jxl 2145w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_2145/v1740075122/cq7g154llpa2kuttb6zc.jxl 4290w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_2060/v1740075122/cq7g154llpa2kuttb6zc.jxl 2060w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_2060/v1740075122/cq7g154llpa2kuttb6zc.jxl 4120w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1987/v1740075122/cq7g154llpa2kuttb6zc.jxl 1987w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1987/v1740075122/cq7g154llpa2kuttb6zc.jxl 3974w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1848/v1740075122/cq7g154llpa2kuttb6zc.jxl 1848w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1848/v1740075122/cq7g154llpa2kuttb6zc.jxl 3696w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1695/v1740075122/cq7g154llpa2kuttb6zc.jxl 1695w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1695/v1740075122/cq7g154llpa2kuttb6zc.jxl 3390w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1521/v1740075122/cq7g154llpa2kuttb6zc.jxl 1521w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1521/v1740075122/cq7g154llpa2kuttb6zc.jxl 3042w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1427/v1740075122/cq7g154llpa2kuttb6zc.jxl 1427w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1427/v1740075122/cq7g154llpa2kuttb6zc.jxl 2854w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1480/v1740075122/cq7g154llpa2kuttb6zc.jxl 1480w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1480/v1740075122/cq7g154llpa2kuttb6zc.jxl 2960w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_935/v1740075122/cq7g154llpa2kuttb6zc.jxl 935w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_935/v1740075122/cq7g154llpa2kuttb6zc.jxl 1870w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_868/v1740075122/cq7g154llpa2kuttb6zc.jxl 868w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_868/v1740075122/cq7g154llpa2kuttb6zc.jxl 1736w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_744/v1740075122/cq7g154llpa2kuttb6zc.jxl 744w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_744/v1740075122/cq7g154llpa2kuttb6zc.jxl 1488w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_615/v1740075122/cq7g154llpa2kuttb6zc.jxl 615w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_615/v1740075122/cq7g154llpa2kuttb6zc.jxl 1230w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_457/v1740075122/cq7g154llpa2kuttb6zc.jxl 457w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_457/v1740075122/cq7g154llpa2kuttb6zc.jxl 914w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_250/v1740075122/cq7g154llpa2kuttb6zc.jxl 250w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_250/v1740075122/cq7g154llpa2kuttb6zc.jxl 500w
  "/>
  <source media="(min-width: 768px) and (max-width: 991px)" type="image/avif" sizes="70vw"
          srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_2150/v1740075122/cq7g154llpa2kuttb6zc.avif 2150w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_2150/v1740075122/cq7g154llpa2kuttb6zc.avif 4300w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_2145/v1740075122/cq7g154llpa2kuttb6zc.avif 2145w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_2145/v1740075122/cq7g154llpa2kuttb6zc.avif 4290w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_2060/v1740075122/cq7g154llpa2kuttb6zc.avif 2060w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_2060/v1740075122/cq7g154llpa2kuttb6zc.avif 4120w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1987/v1740075122/cq7g154llpa2kuttb6zc.avif 1987w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1987/v1740075122/cq7g154llpa2kuttb6zc.avif 3974w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1848/v1740075122/cq7g154llpa2kuttb6zc.avif 1848w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1848/v1740075122/cq7g154llpa2kuttb6zc.avif 3696w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1695/v1740075122/cq7g154llpa2kuttb6zc.avif 1695w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1695/v1740075122/cq7g154llpa2kuttb6zc.avif 3390w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1521/v1740075122/cq7g154llpa2kuttb6zc.avif 1521w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1521/v1740075122/cq7g154llpa2kuttb6zc.avif 3042w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1427/v1740075122/cq7g154llpa2kuttb6zc.avif 1427w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1427/v1740075122/cq7g154llpa2kuttb6zc.avif 2854w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1480/v1740075122/cq7g154llpa2kuttb6zc.avif 1480w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1480/v1740075122/cq7g154llpa2kuttb6zc.avif 2960w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_935/v1740075122/cq7g154llpa2kuttb6zc.avif 935w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_935/v1740075122/cq7g154llpa2kuttb6zc.avif 1870w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_868/v1740075122/cq7g154llpa2kuttb6zc.avif 868w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_868/v1740075122/cq7g154llpa2kuttb6zc.avif 1736w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_744/v1740075122/cq7g154llpa2kuttb6zc.avif 744w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_744/v1740075122/cq7g154llpa2kuttb6zc.avif 1488w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_615/v1740075122/cq7g154llpa2kuttb6zc.avif 615w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_615/v1740075122/cq7g154llpa2kuttb6zc.avif 1230w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_457/v1740075122/cq7g154llpa2kuttb6zc.avif 457w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_457/v1740075122/cq7g154llpa2kuttb6zc.avif 914w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_250/v1740075122/cq7g154llpa2kuttb6zc.avif 250w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_250/v1740075122/cq7g154llpa2kuttb6zc.avif 500w
  "/>
  <source media="(min-width: 768px) and (max-width: 991px)" type="image/jpeg" sizes="70vw"
          srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_2150/v1740075122/cq7g154llpa2kuttb6zc.jpeg 2150w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_2150/v1740075122/cq7g154llpa2kuttb6zc.jpeg 4300w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_2145/v1740075122/cq7g154llpa2kuttb6zc.jpeg 2145w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_2145/v1740075122/cq7g154llpa2kuttb6zc.jpeg 4290w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_2060/v1740075122/cq7g154llpa2kuttb6zc.jpeg 2060w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_2060/v1740075122/cq7g154llpa2kuttb6zc.jpeg 4120w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1987/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1987w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1987/v1740075122/cq7g154llpa2kuttb6zc.jpeg 3974w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1848/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1848w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1848/v1740075122/cq7g154llpa2kuttb6zc.jpeg 3696w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1695/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1695w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1695/v1740075122/cq7g154llpa2kuttb6zc.jpeg 3390w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1521/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1521w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1521/v1740075122/cq7g154llpa2kuttb6zc.jpeg 3042w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1427/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1427w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1427/v1740075122/cq7g154llpa2kuttb6zc.jpeg 2854w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1480/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1480w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1480/v1740075122/cq7g154llpa2kuttb6zc.jpeg 2960w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_935/v1740075122/cq7g154llpa2kuttb6zc.jpeg 935w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_935/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1870w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_868/v1740075122/cq7g154llpa2kuttb6zc.jpeg 868w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_868/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1736w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_744/v1740075122/cq7g154llpa2kuttb6zc.jpeg 744w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_744/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1488w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_615/v1740075122/cq7g154llpa2kuttb6zc.jpeg 615w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_615/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1230w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_457/v1740075122/cq7g154llpa2kuttb6zc.jpeg 457w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_457/v1740075122/cq7g154llpa2kuttb6zc.jpeg 914w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_250/v1740075122/cq7g154llpa2kuttb6zc.jpeg 250w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_250/v1740075122/cq7g154llpa2kuttb6zc.jpeg 500w
  "/>
  <source media="(max-width: 767px)" type="image/jxl" sizes="100vw"
          srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_2150/v1740075122/cq7g154llpa2kuttb6zc.jxl 2150w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_2150/v1740075122/cq7g154llpa2kuttb6zc.jxl 4300w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_2145/v1740075122/cq7g154llpa2kuttb6zc.jxl 2145w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_2145/v1740075122/cq7g154llpa2kuttb6zc.jxl 4290w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_2060/v1740075122/cq7g154llpa2kuttb6zc.jxl 2060w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_2060/v1740075122/cq7g154llpa2kuttb6zc.jxl 4120w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1987/v1740075122/cq7g154llpa2kuttb6zc.jxl 1987w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1987/v1740075122/cq7g154llpa2kuttb6zc.jxl 3974w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1848/v1740075122/cq7g154llpa2kuttb6zc.jxl 1848w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1848/v1740075122/cq7g154llpa2kuttb6zc.jxl 3696w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1695/v1740075122/cq7g154llpa2kuttb6zc.jxl 1695w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1695/v1740075122/cq7g154llpa2kuttb6zc.jxl 3390w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1521/v1740075122/cq7g154llpa2kuttb6zc.jxl 1521w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1521/v1740075122/cq7g154llpa2kuttb6zc.jxl 3042w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1427/v1740075122/cq7g154llpa2kuttb6zc.jxl 1427w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1427/v1740075122/cq7g154llpa2kuttb6zc.jxl 2854w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1480/v1740075122/cq7g154llpa2kuttb6zc.jxl 1480w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1480/v1740075122/cq7g154llpa2kuttb6zc.jxl 2960w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_935/v1740075122/cq7g154llpa2kuttb6zc.jxl 935w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_935/v1740075122/cq7g154llpa2kuttb6zc.jxl 1870w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_868/v1740075122/cq7g154llpa2kuttb6zc.jxl 868w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_868/v1740075122/cq7g154llpa2kuttb6zc.jxl 1736w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_744/v1740075122/cq7g154llpa2kuttb6zc.jxl 744w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_744/v1740075122/cq7g154llpa2kuttb6zc.jxl 1488w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_615/v1740075122/cq7g154llpa2kuttb6zc.jxl 615w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_615/v1740075122/cq7g154llpa2kuttb6zc.jxl 1230w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_457/v1740075122/cq7g154llpa2kuttb6zc.jxl 457w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_457/v1740075122/cq7g154llpa2kuttb6zc.jxl 914w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_250/v1740075122/cq7g154llpa2kuttb6zc.jxl 250w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_250/v1740075122/cq7g154llpa2kuttb6zc.jxl 500w
  "/>
  <source media="(max-width: 767px)" type="image/avif" sizes="100vw"
          srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_2150/v1740075122/cq7g154llpa2kuttb6zc.avif 2150w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_2150/v1740075122/cq7g154llpa2kuttb6zc.avif 4300w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_2145/v1740075122/cq7g154llpa2kuttb6zc.avif 2145w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_2145/v1740075122/cq7g154llpa2kuttb6zc.avif 4290w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_2060/v1740075122/cq7g154llpa2kuttb6zc.avif 2060w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_2060/v1740075122/cq7g154llpa2kuttb6zc.avif 4120w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1987/v1740075122/cq7g154llpa2kuttb6zc.avif 1987w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1987/v1740075122/cq7g154llpa2kuttb6zc.avif 3974w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1848/v1740075122/cq7g154llpa2kuttb6zc.avif 1848w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1848/v1740075122/cq7g154llpa2kuttb6zc.avif 3696w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1695/v1740075122/cq7g154llpa2kuttb6zc.avif 1695w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1695/v1740075122/cq7g154llpa2kuttb6zc.avif 3390w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1521/v1740075122/cq7g154llpa2kuttb6zc.avif 1521w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1521/v1740075122/cq7g154llpa2kuttb6zc.avif 3042w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1427/v1740075122/cq7g154llpa2kuttb6zc.avif 1427w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1427/v1740075122/cq7g154llpa2kuttb6zc.avif 2854w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1480/v1740075122/cq7g154llpa2kuttb6zc.avif 1480w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1480/v1740075122/cq7g154llpa2kuttb6zc.avif 2960w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_935/v1740075122/cq7g154llpa2kuttb6zc.avif 935w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_935/v1740075122/cq7g154llpa2kuttb6zc.avif 1870w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_868/v1740075122/cq7g154llpa2kuttb6zc.avif 868w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_868/v1740075122/cq7g154llpa2kuttb6zc.avif 1736w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_744/v1740075122/cq7g154llpa2kuttb6zc.avif 744w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_744/v1740075122/cq7g154llpa2kuttb6zc.avif 1488w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_615/v1740075122/cq7g154llpa2kuttb6zc.avif 615w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_615/v1740075122/cq7g154llpa2kuttb6zc.avif 1230w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_457/v1740075122/cq7g154llpa2kuttb6zc.avif 457w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_457/v1740075122/cq7g154llpa2kuttb6zc.avif 914w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_250/v1740075122/cq7g154llpa2kuttb6zc.avif 250w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_250/v1740075122/cq7g154llpa2kuttb6zc.avif 500w
  "/>
  <source media="(max-width: 767px)" type="image/jpeg" sizes="100vw"
          srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_2150/v1740075122/cq7g154llpa2kuttb6zc.jpeg 2150w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_2150/v1740075122/cq7g154llpa2kuttb6zc.jpeg 4300w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_2145/v1740075122/cq7g154llpa2kuttb6zc.jpeg 2145w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_2145/v1740075122/cq7g154llpa2kuttb6zc.jpeg 4290w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_2060/v1740075122/cq7g154llpa2kuttb6zc.jpeg 2060w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_2060/v1740075122/cq7g154llpa2kuttb6zc.jpeg 4120w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1987/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1987w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1987/v1740075122/cq7g154llpa2kuttb6zc.jpeg 3974w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1848/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1848w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1848/v1740075122/cq7g154llpa2kuttb6zc.jpeg 3696w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1695/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1695w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1695/v1740075122/cq7g154llpa2kuttb6zc.jpeg 3390w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1521/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1521w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1521/v1740075122/cq7g154llpa2kuttb6zc.jpeg 3042w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1427/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1427w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1427/v1740075122/cq7g154llpa2kuttb6zc.jpeg 2854w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1480/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1480w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1480/v1740075122/cq7g154llpa2kuttb6zc.jpeg 2960w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_935/v1740075122/cq7g154llpa2kuttb6zc.jpeg 935w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_935/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1870w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_868/v1740075122/cq7g154llpa2kuttb6zc.jpeg 868w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_868/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1736w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_744/v1740075122/cq7g154llpa2kuttb6zc.jpeg 744w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_744/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1488w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_615/v1740075122/cq7g154llpa2kuttb6zc.jpeg 615w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_615/v1740075122/cq7g154llpa2kuttb6zc.jpeg 1230w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_457/v1740075122/cq7g154llpa2kuttb6zc.jpeg 457w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_457/v1740075122/cq7g154llpa2kuttb6zc.jpeg 914w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_250/v1740075122/cq7g154llpa2kuttb6zc.jpeg 250w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_250/v1740075122/cq7g154llpa2kuttb6zc.jpeg 500w
  "/>
  <img src="https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_250/v1740075122/cq7g154llpa2kuttb6zc.jpeg" alt="Responsive Image" loading="lazy">
</picture>
</div>

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
  <em>Photo by <a href="https://unsplash.com/photos/an-island-in-the-middle-of-a-lake-covered-in-snow-1JRZN1K8cGo?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash">Benaja Germann</a> on</em>
  <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
    <path d="M448,230.17V480H0V230.17H141.13V355.09H306.87V230.17ZM306.87,32H141.13V156.91H306.87Z"/>
  </svg>
</p>

[^1]: The image itself can be located anywhere you like.
