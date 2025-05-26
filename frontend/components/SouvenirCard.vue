<template>
	<div
		class="card group overflow-hidden transition-all duration-300 hover:scale-[1.02] hover:transform"
		@mouseenter="isHovered = true"
		@mouseleave="isHovered = false"
	>
		<div class="relative h-64 bg-gray-100">
			<img
				:src="souvenir.imageUrl"
				alt=""
				class="h-full w-full object-cover transition-transform duration-700"
				:class="{ 'scale-105': isHovered }"
			/>
			<div
				v-if="souvenir.status"
				class="absolute top-0 right-0 m-2 rounded bg-white px-2 py-1 text-xs font-medium"
				:class="statusClass"
			>
				{{ souvenir.status }}
			</div>
		</div>
		<div class="p-5">
			<div class="flex items-center justify-between">
				<div>
					<h3
						class="group-hover:text-primary-600 text-lg font-bold text-gray-900 transition-colors duration-200"
					>
						{{ souvenir.name }}
					</h3>
					<div class="mt-1 flex items-center">
						<NuxtLink
							:to="`/companies/${souvenir.companyId}`"
							class="hover:text-primary-600 text-sm text-gray-500"
						>
							{{ souvenir.companyName }}
						</NuxtLink>
						<span class="mx-2 text-gray-300">•</span>
						<span class="text-sm text-gray-500">{{ souvenir.releaseYear }}</span>
					</div>
				</div>
				<div class="bg-primary-50 text-primary-700 rounded px-2 py-1 text-xs font-medium">
					{{ souvenir.category }}
				</div>
			</div>

			<p class="mt-2 line-clamp-3 text-sm text-gray-600">{{ souvenir.description }}</p>

			<div class="mt-4 flex items-center space-x-4">
				<div class="flex items-center">
					<svg
						class="text-accent-500 h-4 w-4"
						xmlns="http://www.w3.org/2000/svg"
						viewBox="0 0 20 20"
						fill="currentColor"
					>
						<path
							d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
						/>
					</svg>
					<span class="ml-1 text-sm font-semibold">{{ souvenir.rating }}</span>
					<span class="ml-1 text-xs text-gray-500">({{ souvenir.reviewCount }})</span>
				</div>
				<div
					v-if="souvenir.isLimited"
					class="text-warning-500 flex items-center"
				>
					<svg
						class="h-4 w-4"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
						/>
					</svg>
					<span class="ml-1 text-xs font-medium">限量發行</span>
				</div>
			</div>

			<div class="mt-4 flex items-center justify-between">
				<NuxtLink
					:to="`/souvenirs/${souvenir.id}`"
					class="text-primary-600 hover:text-primary-700 text-sm font-medium"
				>
					查看詳情
					<span aria-hidden="true">→</span>
				</NuxtLink>
				<button
					class="rounded-full p-2 transition-colors duration-200 hover:bg-gray-100"
					:class="{ 'text-error-500': isWishlisted, 'text-gray-400': !isWishlisted }"
					@click.prevent="toggleWishlist"
				>
					<svg
						class="h-5 w-5"
						xmlns="http://www.w3.org/2000/svg"
						viewBox="0 0 20 20"
						:fill="isWishlisted ? 'currentColor' : 'none'"
						:stroke="isWishlisted ? 'none' : 'currentColor'"
						stroke-width="1.5"
					>
						<path
							fill-rule="evenodd"
							d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z"
							clip-rule="evenodd"
						/>
					</svg>
				</button>
			</div>
		</div>
	</div>
</template>

<script setup>
	const props = defineProps({
		souvenir: {
			type: Object,
			required: true,
		},
	});

	const isHovered = ref(false);
	const isWishlisted = ref(false);

	const statusClass = computed(() => {
		switch (props.souvenir.status) {
			case '新上架':
				return 'bg-success-500 text-white';
			case '熱門':
				return 'bg-error-500 text-white';
			case '即將結束':
				return 'bg-warning-500 text-white';
			default:
				return 'bg-white text-gray-700';
		}
	});

	const toggleWishlist = () => {
		isWishlisted.value = !isWishlisted.value;
	};
</script>
