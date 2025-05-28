<template>
	<section class="bg-white py-16">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="text-center">
				<h2 class="text-primary-600 text-base font-semibold tracking-wide uppercase">分類瀏覽</h2>
				<p class="mt-1 text-3xl font-extrabold text-gray-900 sm:text-4xl sm:tracking-tight">
					紀念品分類
				</p>
				<p class="mx-auto mt-5 max-w-xl text-lg text-gray-500">
					依照不同類型瀏覽台灣企業的股票紀念品，找到您最感興趣的收藏品。
				</p>
			</div>

			<div class="mt-10">
				<div class="grid grid-cols-1 gap-6 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
					<div
						v-for="category in categories"
						:key="category.name"
						class="group relative overflow-hidden rounded-lg bg-white shadow-sm transition-shadow duration-300 hover:shadow-lg"
					>
						<div class="relative h-64 w-full overflow-hidden">
							<img
								:src="category.imageUrl"
								alt=""
								class="h-full w-full transform object-cover transition-transform duration-500 group-hover:scale-105"
							/>
							<div
								class="absolute inset-0 bg-gradient-to-t from-gray-900 to-transparent opacity-60"
							></div>
							<div class="absolute right-0 bottom-0 left-0 p-6">
								<h3 class="text-xl font-bold text-white">{{ category.name }}</h3>
								<p class="mt-1 text-sm text-white opacity-90">
									{{ getCategoryCount(category.name) }}+ 項
								</p>
							</div>
						</div>
						<NuxtLink
							:to="`/companies?category=${encodeURIComponent(category.name)}`"
							class="absolute inset-0 focus:outline-none"
						>
							<span class="sr-only">瀏覽 {{ category.name }}</span>
						</NuxtLink>
					</div>
				</div>
			</div>
		</div>
	</section>
</template>

<script setup lang="ts">
	import { useCategoryCounts } from '~/composables/useCategoryCounts';
	import GIFT_CATEGORY_MAP from '~/config/category';

	const { state, fetchCounts } = useCategoryCounts();

	// 在組件掛載時獲取分類計數
	onMounted(() => {
		fetchCounts();
	});

	const categories = [
		{
			name: '禮品卡',
			slug: GIFT_CATEGORY_MAP['禮品卡'],
			imageUrl:
				'https://images.pexels.com/photos/5650026/pexels-photo-5650026.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
		},
		{
			name: '生活日用品',
			slug: GIFT_CATEGORY_MAP['生活日用品'],
			imageUrl:
				'https://images.pexels.com/photos/4210782/pexels-photo-4210782.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
		},
		{
			name: '食品與飲品',
			slug: GIFT_CATEGORY_MAP['食品與飲品'],
			imageUrl:
				'https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
		},
		{
			name: '廚房用品',
			slug: GIFT_CATEGORY_MAP['廚房用品'],
			imageUrl:
				'https://images.pexels.com/photos/4686822/pexels-photo-4686822.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
		},
		{
			name: '電子產品與配件',
			slug: GIFT_CATEGORY_MAP['電子產品與配件'],
			imageUrl:
				'https://images.pexels.com/photos/3184292/pexels-photo-3184292.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
		},
		{
			name: '居家用品',
			slug: GIFT_CATEGORY_MAP['居家用品'],
			imageUrl:
				'https://images.pexels.com/photos/1571460/pexels-photo-1571460.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
		},
		{
			name: '特殊用途商品',
			slug: GIFT_CATEGORY_MAP['特殊用途商品'],
			imageUrl:
				'https://images.pexels.com/photos/6120214/pexels-photo-6120214.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
		},
		{
			name: '其他',
			slug: GIFT_CATEGORY_MAP['其他'],
			imageUrl:
				'https://images.pexels.com/photos/3621104/pexels-photo-3621104.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
		},
	];

	// 計算每個分類的數量
	const getCategoryCount = (categoryName: string) => {
		if (!state.value.counts) return 0;
		return state.value.counts[categoryName] || 0;
	};
</script>
