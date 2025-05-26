<template>
	<div class="flex min-h-screen flex-col">
		<AppHeader />
		<main class="flex-grow">
			<slot />
		</main>
		<AppFooter />
	</div>
</template>
