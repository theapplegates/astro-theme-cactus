---
title: "Markdown Admonitions"
description: "This post showcases using the markdown admonition feature in Astro Cactus"
publishDate: "25 Aug 2024"
updatedDate: "4 July 2025"
tags: ["markdown", "admonitions"]
---
<picture>
  <source type="image/jxl" srcset="
    https://res.cloudinary.com/paulapplegate.com/image/upload/c_scale,w_1000/v1756090345/aaron-yuan-painting_n57zoa.jxl 1000w,
    https://res.cloudinary.com/paulapplegate.com/image/upload/c_scale,w_838/v1756090345/aaron-yuan-painting_n57zoa.jxl 838w,
    https://res.cloudinary.com/paulapplegate.com/image/upload/c_scale,w_50/v1756090345/aaron-yuan-painting_n57zoa.jxl 50w
  " sizes="(max-width: 7974px) 100vw, 7974px">
  <source type="image/avif" srcset="
    https://res.cloudinary.com/paulapplegate.com/image/upload/c_scale,w_1000/v1756090345/aaron-yuan-painting_n57zoa.avif 1000w,
    https://res.cloudinary.com/paulapplegate.com/image/upload/c_scale,w_50/v1756090345/aaron-yuan-painting_n57zoa.avif 50w
  " sizes="(max-width: 7974px) 100vw, 7974px">
  <img
    src="https://res.cloudinary.com/paulapplegate.com/image/upload/c_scale,w_1000/v1756090345/aaron-yuan-painting_n57zoa.jpg"
    srcset="
    https://res.cloudinary.com/paulapplegate.com/image/upload/c_scale,w_1000/v1756090345/aaron-yuan-painting_n57zoa.jpg 1000w,
    https://res.cloudinary.com/paulapplegate.com/image/upload/c_scale,w_945/v1756090345/aaron-yuan-painting_n57zoa.jpg 945w,
    https://res.cloudinary.com/paulapplegate.com/image/upload/c_scale,w_665/v1756090345/aaron-yuan-painting_n57zoa.jpg 665w,
    https://res.cloudinary.com/paulapplegate.com/image/upload/c_scale,w_50/v1756090345/aaron-yuan-painting_n57zoa.jpg 50w
  "
    sizes="(max-width: 7974px) 100vw, 7974px"
    width="7974"
    height="5518"
    alt="Responsive aaron-yuan-painting_n57zoa"
    loading="lazy"
    decoding="async">
</picture>


## What are admonitions

Admonitions (also known as “asides”) are useful for providing supportive and/or supplementary information related to your content.

## How to use them

To use admonitions in Astro Cactus, wrap your Markdown content in a pair of triple colons `:::`. The first pair should also include the type of admonition you want to use.

For example, with the following Markdown:

```md
:::note
Highlights information that users should take into account, even when skimming.
:::
```

Outputs:

:::note
Highlights information that users should take into account, even when skimming.
:::

## Admonition Types

The following admonitions are currently supported:

- `note`
- `tip`
- `important`
- `warning`
- `caution`

### Note

```md
:::note
Highlights information that users should take into account, even when skimming.
:::
```

:::note
Highlights information that users should take into account, even when skimming.
:::

### Tip

```md
:::tip
Optional information to help a user be more successful.
:::
```

:::tip
Optional information to help a user be more successful.
:::

### Important

```md
:::important
Crucial information necessary for users to succeed.
:::
```

:::important
Crucial information necessary for users to succeed.
:::

### Caution

```md
:::caution
Negative potential consequences of an action.
:::
```

:::caution
Negative potential consequences of an action.
:::

### Warning

```md
:::warning
Critical content demanding immediate user attention due to potential risks.
:::
```

:::warning
Critical content demanding immediate user attention due to potential risks.
:::

## Customising the admonition title

You can customise the admonition title using the following markup:

```md
:::note[My custom title]
This is a note with a custom title.
:::
```

Outputs:

:::note[My custom title]
This is a note with a custom title.
:::

## GitHub Repository Cards
You can add dynamic cards that link to GitHub repositories, on page load, the repository information is pulled from the GitHub API.

::github{repo="chrismwilliams/astro-theme-cactus"}

You can also link a Github user:

::github{user="withastro"}

To use this feature you just use the "Github" directive:

```markdown title="Linking a repo"
::github{repo="chrismwilliams/astro-theme-cactus"}
```

```markdown title="Linking a user"
::github{user="withastro"}
```
