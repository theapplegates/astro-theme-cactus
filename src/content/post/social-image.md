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
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_1200/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1200w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_1200/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 2400w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_1199/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1199w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_1199/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 2398w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_1197/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1197w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_1197/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 2394w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_1134/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1134w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_1134/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 2268w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_1095/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1095w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_1095/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 2190w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_955/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 955w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_955/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1910w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_865/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 865w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_865/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1730w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_762/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 762w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_762/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1524w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_751/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 751w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_751/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1502w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_484/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 484w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_484/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 968w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_250/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 250w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_250/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 500w
  "/>
  <source media="(min-width: 1200px)" type="image/avif" sizes="40vw"
          srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_1200/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1200w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_1200/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 2400w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_1199/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1199w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_1199/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 2398w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_1197/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1197w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_1197/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 2394w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_1134/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1134w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_1134/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 2268w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_1095/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1095w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_1095/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 2190w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_955/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 955w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_955/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1910w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_865/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 865w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_865/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1730w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_762/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 762w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_762/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1524w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_751/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 751w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_751/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1502w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_484/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 484w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_484/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 968w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_250/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 250w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_250/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 500w
  "/>
  <source media="(min-width: 1200px)" type="image/jpeg" sizes="40vw"
          srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_1200/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1200w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_1200/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 2400w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_1199/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1199w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_1199/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 2398w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_1197/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1197w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_1197/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 2394w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_1134/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1134w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_1134/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 2268w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_1095/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1095w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_1095/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 2190w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_955/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 955w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_955/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1910w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_865/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 865w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_865/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1730w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_762/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 762w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_762/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1524w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_751/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 751w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_751/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1502w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_484/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 484w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_484/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 968w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_1.0/c_fill,g_auto/c_scale,w_250/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 250w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/dpr_2.0/c_fill,g_auto/c_scale,w_250/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 500w
  "/>
  <source media="(min-width: 992px) and (max-width: 1199px)" type="image/jxl" sizes="60vw"
          srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1200/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1200w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1200/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 2400w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1199/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1199w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1199/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 2398w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1197/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1197w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1197/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 2394w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1134/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1134w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1134/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 2268w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1095/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1095w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1095/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 2190w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_955/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 955w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_955/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1910w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_865/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 865w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_865/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1730w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_762/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 762w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_762/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1524w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_751/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 751w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_751/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1502w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_484/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 484w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_484/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 968w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_250/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 250w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_250/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 500w
  "/>
  <source media="(min-width: 992px) and (max-width: 1199px)" type="image/avif" sizes="60vw"
          srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1200/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1200w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1200/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 2400w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1199/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1199w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1199/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 2398w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1197/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1197w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1197/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 2394w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1134/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1134w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1134/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 2268w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1095/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1095w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1095/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 2190w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_955/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 955w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_955/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1910w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_865/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 865w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_865/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1730w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_762/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 762w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_762/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1524w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_751/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 751w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_751/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1502w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_484/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 484w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_484/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 968w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_250/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 250w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_250/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 500w
  "/>
  <source media="(min-width: 992px) and (max-width: 1199px)" type="image/jpeg" sizes="60vw"
          srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1200/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1200w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1200/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 2400w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1199/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1199w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1199/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 2398w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1197/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1197w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1197/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 2394w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1134/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1134w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1134/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 2268w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1095/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1095w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1095/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 2190w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_955/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 955w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_955/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1910w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_865/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 865w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_865/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1730w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_762/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 762w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_762/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1524w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_751/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 751w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_751/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1502w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_484/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 484w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_484/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 968w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_250/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 250w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_16:9,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_250/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 500w
  "/>
  <source media="(min-width: 768px) and (max-width: 991px)" type="image/jxl" sizes="70vw"
          srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1200/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1200w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1200/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 2400w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1199/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1199w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1199/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 2398w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1197/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1197w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1197/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 2394w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1134/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1134w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1134/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 2268w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1095/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1095w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1095/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 2190w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_955/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 955w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_955/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1910w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_865/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 865w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_865/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1730w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_762/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 762w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_762/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1524w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_751/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 751w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_751/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1502w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_484/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 484w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_484/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 968w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_250/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 250w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_250/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 500w
  "/>
  <source media="(min-width: 768px) and (max-width: 991px)" type="image/avif" sizes="70vw"
          srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1200/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1200w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1200/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 2400w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1199/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1199w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1199/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 2398w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1197/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1197w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1197/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 2394w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1134/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1134w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1134/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 2268w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1095/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1095w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1095/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 2190w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_955/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 955w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_955/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1910w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_865/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 865w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_865/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1730w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_762/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 762w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_762/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1524w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_751/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 751w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_751/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1502w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_484/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 484w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_484/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 968w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_250/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 250w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_250/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 500w
  "/>
  <source media="(min-width: 768px) and (max-width: 991px)" type="image/jpeg" sizes="70vw"
          srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1200/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1200w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1200/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 2400w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1199/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1199w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1199/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 2398w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1197/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1197w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1197/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 2394w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1134/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1134w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1134/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 2268w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1095/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1095w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1095/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 2190w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_955/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 955w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_955/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1910w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_865/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 865w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_865/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1730w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_762/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 762w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_762/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1524w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_751/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 751w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_751/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1502w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_484/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 484w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_484/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 968w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_250/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 250w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_4:3,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_250/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 500w
  "/>
  <source media="(max-width: 767px)" type="image/jxl" sizes="100vw"
          srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1200/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1200w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1200/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 2400w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1199/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1199w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1199/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 2398w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1197/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1197w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1197/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 2394w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1134/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1134w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1134/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 2268w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1095/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1095w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1095/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 2190w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_955/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 955w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_955/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1910w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_865/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 865w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_865/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1730w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_762/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 762w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_762/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1524w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_751/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 751w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_751/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 1502w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_484/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 484w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_484/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 968w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_250/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 250w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_250/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jxl 500w
  "/>
  <source media="(max-width: 767px)" type="image/avif" sizes="100vw"
          srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1200/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1200w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1200/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 2400w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1199/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1199w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1199/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 2398w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1197/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1197w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1197/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 2394w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1134/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1134w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1134/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 2268w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1095/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1095w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1095/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 2190w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_955/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 955w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_955/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1910w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_865/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 865w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_865/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1730w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_762/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 762w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_762/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1524w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_751/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 751w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_751/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 1502w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_484/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 484w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_484/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 968w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_250/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 250w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_250/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.avif 500w
  "/>
  <source media="(max-width: 767px)" type="image/jpeg" sizes="100vw"
          srcset="
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1200/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1200w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1200/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 2400w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1199/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1199w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1199/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 2398w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1197/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1197w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1197/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 2394w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1134/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1134w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1134/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 2268w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_1095/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1095w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_1095/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 2190w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_955/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 955w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_955/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1910w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_865/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 865w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_865/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1730w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_762/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 762w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_762/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1524w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_751/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 751w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_751/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 1502w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_484/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 484w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_484/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 968w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_1.0/c_fill,g_auto/c_scale,w_250/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 250w,
    https://res.cloudinary.com/paulapplegate-com/image/upload/ar_1:1,c_fill,g_auto/dpr_2.0/c_fill,g_auto/c_scale,w_250/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg 500w
  "/>
  <img src="https://res.cloudinary.com/paulapplegate-com/image/upload/c_fill,g_auto/c_scale,w_250/e_shadow:75,x_20,y_20/v1742516436/zyvlwmyynrozkbgdysaf.jpeg" alt="Responsive Image" loading="lazy">
</picture>
</div>

![Pic](/src/assets/marek-piwnicki-mountains.jpg)

## Adding your own social image to a post

This post is an example of how to add a custom [open graph](https://ogp.me/) social image, also known as an OG image, to a blog post.
By adding the optional ogImage property to the frontmatter of a post, you opt out of [satori](https://github.com/vercel/satori) automatically generating an image for this page.

If you open this markdown file `src/content/post/social-image.md` you'll see the ogImage property set to an image which lives in the public folder[^1].

```yaml
ogImage: "/social-card.png"
```

You can view the one set for this template page [here](https://astro-cactus.chriswilliams.dev/social-card.png).

[^1]: The image itself can be located anywhere you like.
