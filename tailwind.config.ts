import type { Config } from 'tailwindcss'

const config: Config = {
  content: ['./src/**/*.{html,js,ts,jsx,tsx,astro,mdx}'],
  theme: {
    extend: {
      fontFamily: {
        wotfard: ['"Wotfard"', 'sans-serif'],
      },
    },
  },
  plugins: [require('@tailwindcss/typography')],
}

export default config
