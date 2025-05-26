// https://nuxt.com/docs/api/configuration/nuxt-config
import tailwindcss from '@tailwindcss/vite';

export default defineNuxtConfig({
	compatibilityDate: '2024-11-01',
	devtools: { enabled: true },
	modules: ['@nuxt/eslint', '@nuxtjs/google-fonts', '@pinia/nuxt'],
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
			title: '台灣公司股票紀念品資訊平台',
			meta: [
				{ charset: 'utf-8' },
				{ name: 'viewport', content: 'width=device-width, initial-scale=1' },
				{
					name: 'description',
					content: '探索台灣上市公司的精美股票紀念品',
				},
			],
			link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
		},
	},
	runtimeConfig: {
		mongodbUri: process.env.MONGO_CONNECTION_STRING,
	},
	build: {
		transpile: ['luxon'],
	},
});
