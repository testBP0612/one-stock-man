<template>
	<div
		v-if="souvenir"
		class="bg-gray-50 py-12"
	>
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="overflow-hidden rounded-xl bg-white shadow-sm">
				<div class="flex flex-col md:flex-row">
					<!-- Image Gallery (simplified) -->
					<div class="md:w-1/2">
						<div class="aspect-w-4 aspect-h-3 relative bg-gray-100">
							<img
								:src="souvenir.imageUrl"
								alt=""
								class="h-full w-full object-cover"
							/>
							<div
								v-if="souvenir.status"
								class="absolute top-0 right-0 m-4 rounded bg-white px-2 py-1 text-xs font-medium"
								:class="statusClass"
							>
								{{ souvenir.status }}
							</div>
						</div>
						<div class="grid grid-cols-4 gap-2 p-4">
							<div
								class="aspect-w-1 aspect-h-1 cursor-pointer overflow-hidden rounded-md bg-gray-100"
							>
								<img
									:src="souvenir.imageUrl"
									alt=""
									class="h-full w-full object-cover"
								/>
							</div>
							<!-- Placeholder thumbnails for demo -->
							<div class="aspect-w-1 aspect-h-1 cursor-pointer rounded-md bg-gray-200"></div>
							<div class="aspect-w-1 aspect-h-1 cursor-pointer rounded-md bg-gray-200"></div>
							<div class="aspect-w-1 aspect-h-1 cursor-pointer rounded-md bg-gray-200"></div>
						</div>
					</div>

					<!-- Product Info -->
					<div class="p-6 md:w-1/2">
						<div class="flex justify-between">
							<div>
								<h1 class="text-2xl font-bold text-gray-900">{{ souvenir.name }}</h1>
								<NuxtLink
									:to="`/companies/${souvenir.companyId}`"
									class="text-primary-600 hover:text-primary-700"
								>
									{{ souvenir.companyName }}
								</NuxtLink>
							</div>
							<div
								class="bg-primary-50 text-primary-700 h-fit rounded px-2 py-1 text-xs font-medium"
							>
								{{ souvenir.category }}
							</div>
						</div>

						<div class="mt-4 flex items-center">
							<div class="flex items-center">
								<template
									v-for="i in 5"
									:key="i"
								>
									<svg
										class="h-5 w-5"
										:class="i <= souvenir.rating ? 'text-accent-500' : 'text-gray-300'"
										xmlns="http://www.w3.org/2000/svg"
										viewBox="0 0 20 20"
										fill="currentColor"
									>
										<path
											d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
										/>
									</svg>
								</template>
								<span class="ml-2 text-sm text-gray-600">{{ souvenir.reviewCount }} 評價</span>
							</div>
						</div>

						<div class="mt-6">
							<h3 class="text-sm font-medium text-gray-900">紀念品介紹</h3>
							<div class="mt-2 space-y-4 text-base text-gray-700">
								<p>{{ souvenir.description }}</p>
							</div>
						</div>

						<div class="mt-6">
							<div class="flex items-center justify-between">
								<h3 class="text-sm font-medium text-gray-900">紀念品資訊</h3>
							</div>
							<div class="mt-2 border-t border-gray-200">
								<dl class="divide-y divide-gray-200">
									<div class="flex justify-between py-3">
										<dt class="text-sm font-medium text-gray-500">發行年份</dt>
										<dd class="text-sm text-gray-900">{{ souvenir.releaseYear }}</dd>
									</div>
									<div class="flex justify-between py-3">
										<dt class="text-sm font-medium text-gray-500">發行公司</dt>
										<dd class="text-sm text-gray-900">{{ souvenir.companyName }}</dd>
									</div>
									<div class="flex justify-between py-3">
										<dt class="text-sm font-medium text-gray-500">紀念品分類</dt>
										<dd class="text-sm text-gray-900">{{ souvenir.category }}</dd>
									</div>
									<div class="flex justify-between py-3">
										<dt class="text-sm font-medium text-gray-500">限量發行</dt>
										<dd class="text-sm text-gray-900">{{ souvenir.isLimited ? '是' : '否' }}</dd>
									</div>
								</dl>
							</div>
						</div>

						<div class="mt-8 flex space-x-4">
							<button class="btn-primary flex-1">
								<svg
									class="mr-2 h-5 w-5"
									xmlns="http://www.w3.org/2000/svg"
									fill="none"
									viewBox="0 0 24 24"
									stroke="currentColor"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"
									/>
								</svg>
								購買紀念品
							</button>
							<button
								class="btn-outline flex items-center justify-center"
								:class="{ 'text-error-500 border-error-500 hover:bg-error-50': isWishlisted }"
								@click="toggleWishlist"
							>
								<svg
									class="h-5 w-5"
									xmlns="http://www.w3.org/2000/svg"
									:fill="isWishlisted ? 'currentColor' : 'none'"
									viewBox="0 0 24 24"
									stroke="currentColor"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
									/>
								</svg>
							</button>
							<button class="btn-outline flex items-center justify-center">
								<svg
									class="h-5 w-5"
									xmlns="http://www.w3.org/2000/svg"
									fill="none"
									viewBox="0 0 24 24"
									stroke="currentColor"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z"
									/>
								</svg>
							</button>
						</div>
					</div>
				</div>
			</div>

			<!-- Reviews Section (Simplified) -->
			<div class="mt-12">
				<h2 class="mb-6 text-2xl font-bold text-gray-900">收藏家評價</h2>

				<div class="rounded-lg bg-white p-6 shadow-sm">
					<div class="mb-6 flex items-center justify-between">
						<div>
							<h3 class="text-lg font-medium text-gray-900">評價 ({{ souvenir.reviewCount }})</h3>
							<div class="mt-1 flex items-center">
								<div class="flex items-center">
									<template
										v-for="i in 5"
										:key="i"
									>
										<svg
											class="h-5 w-5"
											:class="i <= souvenir.rating ? 'text-accent-500' : 'text-gray-300'"
											xmlns="http://www.w3.org/2000/svg"
											viewBox="0 0 20 20"
											fill="currentColor"
										>
											<path
												d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
											/>
										</svg>
									</template>
									<span class="ml-2 text-sm text-gray-600">{{ souvenir.rating }} / 5</span>
								</div>
							</div>
						</div>
						<button class="btn-primary">撰寫評價</button>
					</div>

					<!-- Sample Reviews - In a real app, these would come from an API -->
					<div class="space-y-8">
						<div class="flex">
							<div class="mr-4 flex-shrink-0">
								<img
									class="h-12 w-12 rounded-full"
									src="https://images.pexels.com/photos/614810/pexels-photo-614810.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
									alt=""
								/>
							</div>
							<div>
								<h4 class="text-md font-bold">陳小明</h4>
								<div class="mt-1 flex items-center">
									<template
										v-for="i in 5"
										:key="i"
									>
										<svg
											class="h-4 w-4"
											:class="i <= 5 ? 'text-accent-500' : 'text-gray-300'"
											xmlns="http://www.w3.org/2000/svg"
											viewBox="0 0 20 20"
											fill="currentColor"
										>
											<path
												d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
											/>
										</svg>
									</template>
									<span class="ml-2 text-xs text-gray-500">2023年12月10日</span>
								</div>
								<div class="mt-2 text-sm text-gray-600">
									<p>品質非常好，做工精細，值得收藏！紀念價值高，是很棒的企業紀念品。</p>
								</div>
							</div>
						</div>

						<div class="flex">
							<div class="mr-4 flex-shrink-0">
								<img
									class="h-12 w-12 rounded-full"
									src="https://images.pexels.com/photos/774909/pexels-photo-774909.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
									alt=""
								/>
							</div>
							<div>
								<h4 class="text-md font-bold">王小華</h4>
								<div class="mt-1 flex items-center">
									<template
										v-for="i in 5"
										:key="i"
									>
										<svg
											class="h-4 w-4"
											:class="i <= 4 ? 'text-accent-500' : 'text-gray-300'"
											xmlns="http://www.w3.org/2000/svg"
											viewBox="0 0 20 20"
											fill="currentColor"
										>
											<path
												d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
											/>
										</svg>
									</template>
									<span class="ml-2 text-xs text-gray-500">2024年2月5日</span>
								</div>
								<div class="mt-2 text-sm text-gray-600">
									<p>
										設計非常有創意，展現了企業精神。收到後比照片上看起來還要漂亮，朋友們都很羨慕這個收藏品。
									</p>
								</div>
							</div>
						</div>
					</div>

					<div class="mt-8 text-center">
						<button class="btn-outline">查看更多評價</button>
					</div>
				</div>
			</div>

			<!-- Related Souvenirs -->
			<div class="mt-16">
				<h2 class="mb-6 text-2xl font-bold text-gray-900">相關紀念品</h2>

				<div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
					<SouvenirCard
						v-for="related in relatedSouvenirs"
						:key="related.id"
						:souvenir="related"
					/>
				</div>
			</div>
		</div>
	</div>
	<div
		v-else
		class="flex h-64 items-center justify-center"
	>
		<div class="border-primary-500 h-12 w-12 animate-spin rounded-full border-b-2"></div>
	</div>
</template>

<script setup>
	import { useSouvenirsStore } from '~/stores/souvenirsStore';

	const route = useRoute();
	const souvenirsStore = useSouvenirsStore();

	const souvenirId = computed(() => parseInt(route.params.id));
	const souvenir = computed(() => souvenirsStore.getSouvenirById(souvenirId.value));
	const isWishlisted = ref(false);

	// SEO 設定
	watch(
		souvenir,
		(newSouvenir) => {
			if (newSouvenir) {
				useHead({
					title: `${newSouvenir.name} - ${newSouvenir.companyName} 股票紀念品`,
					meta: [
						{
							name: 'description',
							content: `${newSouvenir.description}`,
						},
						{
							property: 'og:title',
							content: `${newSouvenir.name} - ${newSouvenir.companyName} 股票紀念品`,
						},
						{
							property: 'og:description',
							content: `${newSouvenir.description}`,
						},
						{
							property: 'og:image',
							content: newSouvenir.imageUrl,
						},
						{
							name: 'twitter:title',
							content: `${newSouvenir.name} - ${newSouvenir.companyName} 股票紀念品`,
						},
						{
							name: 'twitter:description',
							content: `${newSouvenir.description}`,
						},
						{
							name: 'twitter:image',
							content: newSouvenir.imageUrl,
						},
					],
				});
			}
		},
		{ immediate: true },
	);

	const statusClass = computed(() => {
		if (!souvenir.value || !souvenir.value.status) return '';

		switch (souvenir.value.status) {
			case '新上架':
				return 'bg-success-500 text-white';
			case '熱門':
				return 'bg-error-500 text-white';
			case '限量':
				return 'bg-accent-500 text-white';
			case '即將結束':
				return 'bg-warning-500 text-white';
			default:
				return 'bg-white text-gray-700';
		}
	});

	const relatedSouvenirs = computed(() => {
		if (!souvenir.value) return [];

		// Get souvenirs from the same company or same category
		return souvenirsStore.souvenirs
			.filter(
				(s) =>
					s.id !== souvenirId.value &&
					(s.companyId === souvenir.value.companyId || s.category === souvenir.value.category),
			)
			.slice(0, 4); // Limit to 4 souvenirs
	});

	const toggleWishlist = () => {
		isWishlisted.value = !isWishlisted.value;
	};

	onMounted(async () => {
		await souvenirsStore.fetchSouvenirs();
	});
</script>
