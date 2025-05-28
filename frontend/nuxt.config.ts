// https://nuxt.com/docs/api/configuration/nuxt-config
import tailwindcss from '@tailwindcss/vite';

export default defineNuxtConfig({
	compatibilityDate: '2024-11-01',
	devtools: { enabled: true },
	modules: ['@nuxt/eslint', '@nuxtjs/google-fonts', '@pinia/nuxt', 'nuxt-jsonld'],
	css: ['~/assets/css/main.css'],
	vite: {
		plugins: [tailwindcss()],
	},
	nitro: {
		plugins: ['@/server/index'],
	},
	googleFonts: {
		families: {
			Inter: [300, 400, 500, 600, 700],
			Poppins: [500, 600, 700],
		},
		display: 'swap',
	},
	app: {
		head: {
			title: 'OneStockMan 一股超人-台灣公司股票紀念品資訊平台',
			meta: [
				{ charset: 'utf-8' },
				{ name: 'viewport', content: 'width=device-width, initial-scale=1' },
				{
					name: 'description',
					content:
						'探索台灣上市公司的精美股票紀念品，收藏獨特的企業文化記憶。提供最全面的股票紀念品資訊平台。',
				},
				{
					name: 'keywords',
					content: '股票紀念品,台灣上市公司,企業紀念品,收藏品,股東會紀念品',
				},
				{
					name: 'author',
					content: 'OneStockMan',
				},
				{
					name: 'robots',
					content: 'index, follow',
				},
				// Open Graph / Facebook
				{
					property: 'og:type',
					content: 'website',
				},
				{
					property: 'og:title',
					content: 'OneStockMan 一股超人-台灣公司股票紀念品資訊平台',
				},
				{
					property: 'og:description',
					content:
						'探索台灣上市公司的精美股票紀念品，收藏獨特的企業文化記憶。提供最全面的股票紀念品資訊平台。',
				},
				{
					property: 'og:image',
					content: 'https://onestockman.com/og-image.jpg',
				},
				{
					property: 'og:url',
					content: 'https://onestockman.com',
				},
				// Twitter
				{
					name: 'twitter:card',
					content: 'summary_large_image',
				},
				{
					name: 'twitter:title',
					content: 'OneStockMan 一股超人-台灣公司股票紀念品資訊平台',
				},
				{
					name: 'twitter:description',
					content:
						'探索台灣上市公司的精美股票紀念品，收藏獨特的企業文化記憶。提供最全面的股票紀念品資訊平台。',
				},
				{
					name: 'twitter:image',
					content: 'https://onestockman.com/og-image.jpg',
				},
			],
			link: [
				{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
				{ rel: 'canonical', href: 'https://onestockman.com' },
			],
		},
	},
	runtimeConfig: {
		mongodbUri: process.env.MONGO_CONNECTION_STRING,
	},
	build: {
		transpile: ['luxon'],
	},
});
