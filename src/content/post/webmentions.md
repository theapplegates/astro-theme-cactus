---
title: "Adding Webmentions to Astro Cactus"
description: "This post describes the process of adding webmentions to your own site"
publishDate: "11 Oct 2023"
tags: ["webmentions", "astro", "social"]
updatedDate: 6 December 2024
---

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


## TLDR

1. Add a link on your homepage to either your GitHub profile and/or email address as per [IndieLogin's](https://indielogin.com/setup) instructions. You _could_ do this via `src/components/SocialList.astro`, just be sure to include `isWebmention` to the relevant link if doing so.
2. Create an account @ [Webmention.io](https://webmention.io/) by entering your website's address.
3. Add the link feed and api key to a `.env` file with the key `WEBMENTION_URL` and `WEBMENTION_API_KEY` respectively, you could rename `.env.example` found in this template. You can also add the optional `WEBMENTION_PINGBACK` link here too.
4. Go to [brid.gy](https://brid.gy/) and sign-in to each social account[s] you wish to link.
5. Publish and build your website, remember to add the api key, and it should now be ready to receive webmentions!

## What are webmentions

Put simply, it's a way to show users who like, comment, repost and more, on various pages on your website via social media.

This theme displays the number of likes, mentions and replies each blog post receives. There are a couple of more webmentions that I haven't included, like reposts, which are currently filtered out, but shouldn't be too difficult to include.

## Steps to add it to your own site

Your going to have to create a couple of accounts to get things up-and-running. But, the first thing you need to ensure is that your social links are correct.

### Add link(s) to your profile(s)

Firstly, you need to add a link on your site to prove ownership. If you have a look at [IndieLogin's](https://indielogin.com/setup) instructions, it gives you 2 options, either an email address and/or GitHub account. I've created the component `src/components/SocialList.astro` where you can add your details into the `socialLinks` array, just include the `isWebmention` property to the relevant link which will add the `rel="me authn"` attribute. Whichever way you do it, make sure you have a link in your markup as per IndieLogin's [instructions](https://indielogin.com/setup)

```html
<a href="https://github.com/your-username" rel="me">GitHub</a>
```

### Sign up to Webmention.io

Next, head over to [Webmention.io](https://webmention.io/) and create an account by signing in with your domain name, e.g. `https://astro-cactus.chriswilliams.dev/`. Please note that .app TLDs don't function correctly. Once in, it will give you a couple of links for your domain to accept webmentions. Make a note of these and create a `.env` file (this template include an example `.env.example` which you could rename). Add the link feed and api key with the key/values of `WEBMENTION_URL` and `WEBMENTION_API_KEY` respectively, and the optional `WEBMENTION_PINGBACK` url if required. Please try not to publish this to a repository!

:::note
You don't have to include the pingback link. Maybe coincidentally, but after adding it I started to receive a higher frequency of spam in my mailbox, informing me that my website could be better. TBH they're not wrong. I've now removed it, but it's up to you.
:::

### Sign up to Brid.gy

You're now going to have to use [brid.gy](https://brid.gy/). As the name suggests, it links your website to your social media accounts. For every account you want to set up (e.g. Mastodon), click on the relevant button and connect each account you want brid.gy to search. Just to note again, brid.gy currently has an issue with .app TLDs.

## Testing everything works

With everything set, it's now time to build and publish your website. **REMEMBER** to set your environment variables `WEBMENTION_API_KEY` & `WEBMENTION_URL` with your host.

You can check to see if everything is working by sending a test webmention via [webmentions.rocks](https://webmention.rocks/receive/1). Log in with your domain, enter the auth code, and then the url of the page you want to test. For example, to test this page I would add `https://astro-cactus.chriswilliams.dev/posts/webmentions/`. To view it on your website, rebuild or (re)start dev mode locally, and you should see the result at the bottom of your page.

You can also view any test mentions in the browser via their [api](https://github.com/aaronpk/webmention.io#api).

## Things to add, things to consider

- At the moment, fresh webmentions are only fetched on a rebuild or restarting dev mode, which obviously means if you don't update your site very often you wont get a lot of new content. It should be quite trivial to add a cron job to run the `getAndCacheWebmentions()` function in `src/utils/webmentions.ts` and populate your blog with new content. This is probably what I'll add next as a github action.

- I have seen some mentions have duplicates. Unfortunately, they're quite difficult to filter out as they have different id's.

- I'm not a huge fan of the little external link icon for linking to comments/replies. It's not particularly great on mobile due to its size, and will likely change it in the future.

## Acknowledgements

Many thanks to [Kieran McGuire](https://github.com/chrismwilliams/astro-theme-cactus/issues/107#issue-1863931105) for sharing this with me, and the helpful posts. I'd never heard of webmentions before, and now with this update hopefully others will be able to make use of them. Additionally, articles and examples from [kld](https://kld.dev/adding-webmentions/) and [ryanmulligan.dev](https://ryanmulligan.dev/blog/) really helped in getting this set up and integrated, both a great resource if you're looking for more information!
