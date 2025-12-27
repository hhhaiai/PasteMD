import { defineConfig } from 'vitepress'

const zhConfig = {
  lang: 'zh-CN',
  description: '智能 Markdown 转换工具，让 AI 对话内容完美粘贴到 Word/WPS',

  themeConfig: {
    nav: [
      { text: '指南', link: '/zh/guide/what-is-pastemd' },
      { text: 'macOS', link: '/zh/macos/' },
      { text: '配置', link: '/zh/config/' },
      { text: 'API', link: '/zh/api/' },
      {
        text: 'v0.1.6',
        items: [
          { text: '更新日志', link: 'https://github.com/RichQAQ/PasteMD/releases' },
          { text: '贡献指南', link: '/zh/contributing' }
        ]
      }
    ],

    sidebar: {
      '/zh/guide/': [
        {
          text: '开始',
          items: [
            { text: '什么是 PasteMD？', link: '/zh/guide/what-is-pastemd' },
            { text: '快速开始', link: '/zh/guide/getting-started' },
            { text: '安装', link: '/zh/guide/installation' }
          ]
        },
        {
          text: '核心功能',
          items: [
            { text: 'Markdown 转换', link: '/zh/guide/markdown-conversion' },
            { text: 'HTML 富文本', link: '/zh/guide/html-richtext' },
            { text: 'Excel 表格', link: '/zh/guide/excel-tables' },
            { text: '数学公式', link: '/zh/guide/math-formulas' }
          ]
        },
        {
          text: '高级',
          items: [
            { text: '自定义过滤器', link: '/zh/guide/custom-filters' },
            { text: '热键配置', link: '/zh/guide/hotkeys' },
            { text: '兜底模式', link: '/zh/guide/fallback-mode' }
          ]
        }
      ],
      '/zh/macos/': [
        {
          text: 'macOS 指南',
          items: [
            { text: '简介', link: '/zh/macos/' },
            { text: '权限设置', link: '/zh/macos/permissions' },
            { text: '故障排查', link: '/zh/macos/troubleshooting' },
            { text: 'WPS 公式支持', link: '/zh/macos/wpslatex' }
          ]
        }
      ],
      '/zh/config/': [
        {
          text: '配置选项',
          items: [
            { text: '配置概览', link: '/zh/config/' },
            { text: '基础配置', link: '/zh/config/basic' },
            { text: 'Pandoc 配置', link: '/zh/config/pandoc' },
            { text: '格式化选项', link: '/zh/config/formatting' }
          ]
        }
      ],
      '/zh/api/': [
        {
          text: 'API 参考',
          items: [
            { text: 'API 概览', link: '/zh/api/' },
            { text: '工作流', link: '/zh/api/workflows' },
            { text: '服务', link: '/zh/api/services' },
            { text: '工具', link: '/zh/api/utils' }
          ]
        }
      ]
    },

    editLink: {
      pattern: 'https://github.com/RichQAQ/PasteMD/edit/main/docs/:path',
      text: '在 GitHub 上编辑此页'
    },

    footer: {
      message: '基于 MIT 许可发布',
      copyright: 'Copyright © 2024-present RichQAQ'
    },

    docFooter: {
      prev: '上一页',
      next: '下一页'
    },

    outline: {
      label: '页面导航'
    },

    lastUpdated: {
      text: '最后更新于',
      formatOptions: {
        dateStyle: 'short',
        timeStyle: 'medium'
      }
    },

    langMenuLabel: '多语言',
    returnToTopLabel: '回到顶部',
    sidebarMenuLabel: '菜单',
    darkModeSwitchLabel: '主题',
    lightModeSwitchTitle: '切换到浅色模式',
    darkModeSwitchTitle: '切换到深色模式'
  }
}

const enConfig = {
  lang: 'en-US',
  description: 'Smart Markdown converter for seamless pasting to Word/WPS from AI conversations',

  themeConfig: {
    nav: [
      { text: 'Guide', link: '/en/guide/what-is-pastemd' },
      { text: 'macOS', link: '/en/macos/' },
      { text: 'Config', link: '/en/config/' },
      { text: 'API', link: '/en/api/' },
      {
        text: 'v0.1.6',
        items: [
          { text: 'Changelog', link: 'https://github.com/RichQAQ/PasteMD/releases' },
          { text: 'Contributing', link: '/en/contributing' }
        ]
      }
    ],

    sidebar: {
      '/en/guide/': [
        {
          text: 'Introduction',
          items: [
            { text: 'What is PasteMD?', link: '/en/guide/what-is-pastemd' },
            { text: 'Getting Started', link: '/en/guide/getting-started' },
            { text: 'Installation', link: '/en/guide/installation' }
          ]
        },
        {
          text: 'Core Features',
          items: [
            { text: 'Markdown Conversion', link: '/en/guide/markdown-conversion' },
            { text: 'HTML Rich Text', link: '/en/guide/html-richtext' },
            { text: 'Excel Tables', link: '/en/guide/excel-tables' },
            { text: 'Math Formulas', link: '/en/guide/math-formulas' }
          ]
        },
        {
          text: 'Advanced',
          items: [
            { text: 'Custom Filters', link: '/en/guide/custom-filters' },
            { text: 'Hotkey Configuration', link: '/en/guide/hotkeys' },
            { text: 'Fallback Mode', link: '/en/guide/fallback-mode' }
          ]
        }
      ],
      '/en/macos/': [
        {
          text: 'macOS Guide',
          items: [
            { text: 'Introduction', link: '/en/macos/' }
          ]
        }
      ],
      '/en/config/': [
        {
          text: 'Configuration',
          items: [
            { text: 'Overview', link: '/en/config/' },
            { text: 'Basic Options', link: '/en/config/basic' },
            { text: 'Pandoc Options', link: '/en/config/pandoc' },
            { text: 'Formatting', link: '/en/config/formatting' }
          ]
        }
      ],
      '/en/api/': [
        {
          text: 'API Reference',
          items: [
            { text: 'Overview', link: '/en/api/' },
            { text: 'Workflows', link: '/en/api/workflows' },
            { text: 'Services', link: '/en/api/services' },
            { text: 'Utils', link: '/en/api/utils' }
          ]
        }
      ]
    },

    editLink: {
      pattern: 'https://github.com/RichQAQ/PasteMD/edit/main/docs/:path',
      text: 'Edit this page on GitHub'
    },

    footer: {
      message: 'Released under the MIT License',
      copyright: 'Copyright © 2024-present RichQAQ'
    }
  }
}

export default defineConfig({
  title: 'PasteMD',

  lastUpdated: true,
  cleanUrls: true,
  ignoreDeadLinks: true,

  head: [
    ['meta', { name: 'theme-color', content: '#5f9ea0' }],
    ['link', { rel: 'icon', href: '/logo.png' }],
    ['meta', { name: 'og:type', content: 'website' }],
    ['meta', { name: 'og:locale', content: 'zh-CN' }],
    ['meta', { name: 'og:site_name', content: 'PasteMD' }],
    ['meta', { name: 'og:image', content: '/logo.png' }],
  ],

  locales: {
    root: {
      label: '简体中文',
      link: '/zh/',
      ...zhConfig
    },
    en: {
      label: 'English',
      link: '/en/',
      ...enConfig
    }
  },

  themeConfig: {
    logo: '/logo.png',
    i18nRouting: false,

    socialLinks: [
      { icon: 'github', link: 'https://github.com/RichQAQ/PasteMD' }
    ],

    search: {
      provider: 'local',
      options: {
        locales: {
          zh: {
            translations: {
              button: {
                buttonText: '搜索文档',
                buttonAriaLabel: '搜索文档'
              },
              modal: {
                noResultsText: '无法找到相关结果',
                resetButtonTitle: '清除查询条件',
                footer: {
                  selectText: '选择',
                  navigateText: '切换'
                }
              }
            }
          }
        }
      }
    }
  }
})
