<template>
	<header class="sticky top-0 z-50 bg-white shadow-sm">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="flex h-16 justify-between">
				<div class="flex items-center">
					<NuxtLink
						to="/"
						class="flex flex-shrink-0 items-center"
					>
						<img
							src="/images/logo.png"
							alt="OneStockMan"
							class="h-10 w-10"
						/>
						<span class="font-heading text-primary-600 text-xl font-bold">OneStockMan</span>
					</NuxtLink>
					<nav class="hidden md:ml-8 md:flex md:space-x-8">
						<NuxtLink
							v-for="item in navItems"
							:key="item.name"
							:to="item.href"
							class="hover:text-primary-600 hover:border-primary-500 inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-700 transition-colors duration-200 hover:border-b-2"
							active-class="text-primary-600 border-b-2 border-primary-500"
						>
							{{ item.name }}
						</NuxtLink>
					</nav>
				</div>
				<div class="flex items-center md:hidden">
					<button
						type="button"
						class="focus:ring-primary-500 rounded-md p-2 text-gray-500 hover:bg-gray-100 hover:text-gray-700 focus:ring-2 focus:outline-none focus:ring-inset"
						@click="isOpen = !isOpen"
					>
						<span class="sr-only">打開選單</span>
						<svg
							class="h-6 w-6"
							xmlns="http://www.w3.org/2000/svg"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path
								v-if="!isOpen"
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M4 6h16M4 12h16M4 18h16"
							/>
							<path
								v-else
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M6 18L18 6M6 6l12 12"
							/>
						</svg>
					</button>
				</div>
			</div>
		</div>

		<!-- Mobile menu -->
		<div
			v-if="isOpen"
			class="md:hidden"
		>
			<div class="space-y-1 pt-2 pb-3">
				<NuxtLink
					v-for="item in navItems"
					:key="item.name"
					:to="item.href"
					class="hover:text-primary-600 block py-2 pr-4 pl-3 text-base font-medium text-gray-700 hover:bg-gray-50"
					active-class="bg-secondary-50 text-primary-600"
				>
					{{ item.name }}
				</NuxtLink>
			</div>
		</div>
	</header>
</template>

<script setup>
	const route = useRoute();
	const isOpen = ref(false);

	const navItems = [
		{ name: '首頁', href: '/' },
		{ name: '公司列表', href: '/companies' },
	];

	watch(
		() => route.path,
		() => {
			isOpen.value = false;
		},
	);
</script>
