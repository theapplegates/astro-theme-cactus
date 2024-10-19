---
title: "image-cloudinary"
publishDate: "27 January 2023"
description: "An example post for Astro Cactus, detailing how to add a custom social image card in the frontmatter"
tags: ["example", "blog", "image"]
ogImage: "/social-card.png"
---

import { CldImage } from 'astro-cloudinary';
 <CldImage
  src="https://res.cloudinary.com/paulapplegate-com/image/upload/v1728609985/cnqkojhoqfo7ehdclxrc.jxl"
  width="800"
  height="600"
  sizes="(max-width: 768px) 100vw,
        (max-width: 1200px) 50vw,
        33vw"
  alt="A cake"
/>








