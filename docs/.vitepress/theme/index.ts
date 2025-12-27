// https://vitepress.dev/guide/custom-theme
import { defineComponent, h, onMounted, ref } from 'vue'
import type { Theme } from 'vitepress'
import DefaultTheme from 'vitepress/theme'
import './custom.css'

const GitHubStarBadge = defineComponent({
  name: 'GitHubStarBadge',
  setup() {
    const stars = ref<number | null>(null)

    const formatStars = (value: number) => {
      if (value >= 1000) {
        return `${(value / 1000).toFixed(1).replace(/\.0$/, '')}k`
      }
      return value.toString()
    }

    onMounted(async () => {
      try {
        const response = await fetch('https://api.github.com/repos/RichQAQ/PasteMD')
        if (!response.ok) {
          return
        }
        const data = await response.json()
        if (typeof data?.stargazers_count === 'number') {
          stars.value = data.stargazers_count
        }
      } catch {
        // Keep the fallback display when the request fails.
      }
    })

    return () =>
      h(
        'a',
        {
          class: 'nav-bar-github-stars',
          href: 'https://github.com/RichQAQ/PasteMD',
          target: '_blank',
          rel: 'noreferrer',
          'aria-label': 'GitHub Stars'
        },
        [
          h('span', { class: 'nav-bar-github-stars-label', 'aria-hidden': 'true' }, 'Star'),
          h(
            'span',
            { class: 'nav-bar-github-stars-count' },
            stars.value === null ? '—' : formatStars(stars.value)
          )
        ]
      )
  }
})

export default {
  extends: DefaultTheme,
  Layout: () => {
    return h(DefaultTheme.Layout, null, {
      // https://vitepress.dev/guide/extending-default-theme#layout-slots
      'nav-bar-content-after': () => h(GitHubStarBadge)
    })
  },
  enhanceApp({ app, router, siteData }) {
    // ...
  }
} satisfies Theme
