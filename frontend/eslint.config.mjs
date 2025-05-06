import prettierPlugin from 'eslint-plugin-prettier';
import withNuxt from './.nuxt/eslint.config.mjs';

export default withNuxt(
	{
		plugins: {
			prettier: prettierPlugin,
		},
		rules: {
			'prettier/prettier': [
				'error',
				{
					endOfLine: 'auto',
					singleQuote: true,
					semi: true,
					trailingComma: 'all',
					printWidth: 100,
					arrowParens: 'always',
					singleAttributePerLine: true,
				},
			],
		},
	},

	{
		files: ['**/*.ts', '**/*.vue', '**/*.js'],
		ignores: [
			'.nuxt/**/*',
			'dist/**/*',
			'.output/**/*',
			'node_modules/**/*',
			'**/*.d.ts',
			'**/*.config.d.ts',
		],
		rules: {
			'@typescript-eslint/no-explicit-any': 'warn',
			'@typescript-eslint/no-unused-vars': 'off',

			'vue/multi-word-component-names': 'off',
			'vue/html-self-closing': 'off',

			'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
			'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
		},
	},
);
