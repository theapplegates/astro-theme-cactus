import typography from '@tailwindcss/typography'

export default {
  theme: {
    extend: {
      typography: {
        DEFAULT: {
          css: {
            color: 'var(--color-global-text)',

            // Headings
            h1: {
              fontSize: '1.875rem', // 30px (≈ text-3xl)
              fontWeight: '700',
              marginTop: '1.4em',
              marginBottom: '0.6em',
              lineHeight: '1.2',
              color: 'var(--color-accent-2)',
            },
            h2: {
              fontSize: '1.5rem',
              fontWeight: '700',
              marginTop: '1.3em',
              marginBottom: '0.5em',
              lineHeight: '1.3',
              color: 'var(--color-accent-2)',
            },
            h3: {
              fontSize: '1.25rem',
              fontWeight: '600',
              marginTop: '1.2em',
              marginBottom: '0.4em',
              color: 'var(--color-accent-2)',
            },
            h4: {
              fontSize: '1.125rem',
              fontWeight: '600',
              marginTop: '1em',
              marginBottom: '0.4em',
              color: 'var(--color-accent-2)',
            },
            h5: {
              fontSize: '1rem',
              fontWeight: '600',
              marginTop: '0.9em',
              marginBottom: '0.3em',
              color: 'var(--color-accent-2)',
            },
            h6: {
              fontSize: '0.875rem',
              fontWeight: '600',
              marginTop: '0.8em',
              marginBottom: '0.3em',
              color: 'var(--color-accent-2)',
            },

            // Paragraph
            p: {
              marginTop: '1em',
              marginBottom: '1em',
              lineHeight: '1.7',
              color: 'var(--color-global-text)',
            },

            // Links
            a: {
              color: 'var(--color-link)',
              textDecoration: 'underline',
              fontWeight: '500',
              '&:hover': {
                color: 'var(--color-accent)',
              },
            },

            // Inline code
            code: {
              backgroundColor: 'rgba(0,0,0,0.05)',
              padding: '0.15em 0.3em',
              borderRadius: '0.25rem',
              fontWeight: '500',
              fontSize: '0.875em',
              color: 'var(--color-accent-2)',
            },

            // Code blocks
            'pre code': {
              backgroundColor: 'transparent',
              padding: '0',
              borderRadius: '0',
              color: 'inherit',
            },
            pre: {
              backgroundColor: '#111',
              color: '#eee',
              borderRadius: '0.5rem',
              padding: '1em',
              overflowX: 'auto',
            },

            // Blockquote
            blockquote: {
              fontStyle: 'italic',
              color: 'var(--color-quote)',
              borderLeft: '4px solid var(--color-accent)',
              paddingLeft: '1em',
              marginTop: '1.5em',
              marginBottom: '1.5em',
            },

            // Lists
            ul: {
              paddingLeft: '1.2em',
              listStyleType: 'disc',
            },
            ol: {
              paddingLeft: '1.2em',
              listStyleType: 'decimal',
            },
            li: {
              marginTop: '0.3em',
              marginBottom: '0.3em',
            },

            // Tables
            table: {
              width: '100%',
              borderCollapse: 'collapse',
              marginTop: '1.5em',
              marginBottom: '1.5em',
            },
            thead: {
              borderBottom: '1px solid #ccc',
              fontWeight: '600',
            },
            th: {
              padding: '0.5em',
              borderColor: 'var(--tw-prose-th-borders)',
              textAlign: 'left',
            },
            td: {
              padding: '0.5em',
              borderTop: '1px solid #ddd',
              textAlign: 'left',
            },
          },
        },
      },
    },
  },
  plugins: [typography],
}
