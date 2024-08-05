// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  ssr: true,
  sourcemap: true,
  devtools: { enabled: true },
  modules: ['@element-plus/nuxt', '@nuxt/test-utils/module'],
  elementPlus: {
    /** Options */
  },
  css: [
    'ag-grid-community/styles/ag-grid.css',
    'ag-grid-community/styles/ag-theme-quartz.css'
  ]
});
