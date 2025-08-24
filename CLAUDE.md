# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is **Astro Cactus**, a blog/website theme built with Astro v5, featuring Tailwind v4 and TypeScript. It's designed for creating blogs with posts, notes, and static search functionality using Pagefind.

## Essential Commands

### Development
```bash
# Start development server (localhost:3000)
pnpm dev
# or
pnpm start

# Build for production
pnpm build

# Build search index (run after build)
pnpm postbuild

# Preview production build
pnpm preview

# Type checking
astro check
# or
pnpm check
```

### Code Quality
```bash
# Lint with Biome
pnpm lint

# Format code
pnpm format
# Runs: biome format + prettier + import organization

# Just format code with biome + prettier
pnpm format:code

# Just organize imports
pnpm format:imports
```

## Architecture Overview

### Content Management
- Uses **Astro Content Collections** with schema validation (`src/content.config.ts`)
- Three main collections: `post`, `note`, `tag`
- Content stored in `src/content/[collection]/` directories
- Frontmatter schemas enforce data structure and validation

### Key Configuration Files
- `src/site.config.ts` - Main site configuration (author, title, URL, navigation)
- `astro.config.ts` - Astro build configuration with integrations
- `src/content.config.ts` - Content collection schemas
- `biome.json` - Linting and formatting rules (tabs, 100 char line width)
- `tailwind.config.ts` - Custom Tailwind typography and theme extensions

### Layout Structure
- `src/layouts/Base.astro` - Root layout with theme provider and global structure
- `src/layouts/BlogPost.astro` - Post-specific layout with TOC and webmentions
- Font family set to `font-mono` by default on body element

### Custom Features
- **Admonitions** - Custom markdown directive plugin (`src/plugins/remark-admonitions.ts`)
- **GitHub Cards** - Link preview plugin (`src/plugins/remark-github-card.ts`)
- **Reading Time** - Auto-calculated reading time (`src/plugins/remark-reading-time.ts`)
- **Search** - Pagefind integration for static search (built during postbuild)
- **OG Images** - Auto-generated using Satori (`src/pages/og-image/[slug].png.ts`)
- **Dark/Light Mode** - Theme switching with CSS custom properties

### Content Creation
- **Posts**: Blog entries with tags, descriptions, cover images, draft status
- **Notes**: Shorter content pieces with simpler schema
- **Tags**: Custom tag pages to override auto-generated tag listings
- **Frontmatter Snippets**: VSCode snippets available (`frontmatter-post`, `frontmatter-note`)

### Font Handling
- **Web Fonts**: Wotfard font family in `public/fonts/` (various weights/styles)
- **TTF Fonts**: Roboto Mono in `src/assets/` for build-time processing
- Custom Vite plugin (`rawFonts`) processes font files for build

### TypeScript Structure
- `src/types.ts` - Core type definitions for site config, pagination, webmentions
- Strong typing throughout with Astro's built-in TypeScript support
- Content collections provide automatic type generation

### Package Manager
This project uses **pnpm** - stick to pnpm commands rather than npm/yarn.