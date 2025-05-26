<template>
	<div class="bg-gray-50 py-20">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="mb-12 text-center">
				<h1 class="text-3xl font-extrabold text-gray-900 sm:text-4xl">台灣上市公司列表</h1>
				<p class="mx-auto mt-3 max-w-2xl text-lg text-gray-500 sm:mt-4">
					瀏覽所有有發行股票紀念品的台灣上市公司，探索他們的特色收藏品。
				</p>
			</div>

			<div class="flex flex-col lg:flex-row">
				<div class="mb-6 w-full flex-shrink-0 lg:mr-8 lg:mb-0 lg:w-64">
					<SearchFilter
						:initial-values="state.filterParams"
						@filter="applyFilters"
					/>
				</div>

				<div class="flex-1">
					<div
						v-if="state.pending"
						class="flex justify-center py-12"
					>
						<div class="border-primary-500 h-12 w-12 animate-spin rounded-full border-b-2"></div>
					</div>
					<div
						v-else-if="state.error"
						class="py-12 text-center text-red-500"
					>
						<h3 class="text-lg font-medium text-gray-900">載入失敗</h3>
						<p class="mt-1 text-sm">
							{{ state.error.message || '無法取得公司資料，請稍後再試。' }}
						</p>
					</div>
					<div v-else>
						<div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
							<CompanyCard
								v-for="company in companies"
								:key="company.stock_id"
								:company="company"
							/>
						</div>

						<div
							v-if="!state.pending && companies.length === 0"
							class="py-12 text-center"
						>
							<h3 class="text-lg font-medium text-gray-900">沒有找到符合篩選條件的公司</h3>
							<p class="mt-1 text-sm text-gray-500">請嘗試調整您的搜尋或篩選條件。</p>
						</div>

						<div
							v-if="state.pagination && state.pagination.totalPages > 1"
							class="mt-12 flex justify-center"
						>
							<nav class="flex items-center justify-between">
								<div class="flex flex-1 justify-between sm:hidden">
									<button
										:disabled="currentPage === 1"
										class="cursor-pointer rounded-md border border-gray-300 px-3 py-1 shadow-sm"
										@click="changePage(currentPage - 1)"
									>
										上一頁
									</button>
									<button
										:disabled="currentPage === state.pagination.totalPages"
										class="ml-3 cursor-pointer rounded-md border border-gray-300 px-3 py-1 shadow-sm"
										@click="changePage(currentPage + 1)"
									>
										下一頁
									</button>
								</div>
								<div class="hidden sm:flex sm:flex-1 sm:items-center sm:justify-center">
									<div>
										<span class="relative z-0 inline-flex rounded-md shadow-sm">
											<button
												:disabled="currentPage === 1"
												class="relative inline-flex cursor-pointer items-center rounded-l-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 disabled:opacity-50"
												@click="changePage(currentPage - 1)"
											>
												上一頁
											</button>
											<span
												v-for="pageNumber in pageRange"
												:key="pageNumber"
												:class="[
													'relative inline-flex cursor-pointer items-center border border-gray-300 px-4 py-2 text-sm font-medium hover:bg-gray-50',
													pageNumber === currentPage
														? 'bg-primary-50 text-primary-600 z-10'
														: 'bg-white text-gray-700',
												]"
												@click="changePage(pageNumber)"
											>
												{{ pageNumber }}
											</span>
											<button
												:disabled="currentPage === state.pagination.totalPages"
												class="relative inline-flex cursor-pointer items-center rounded-r-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 disabled:opacity-50"
												@click="changePage(currentPage + 1)"
											>
												下一頁
											</button>
										</span>
										<p class="mt-2 text-center text-sm text-gray-700">
											第 {{ state.pagination.page }} 頁 / 共 {{ state.pagination.totalPages }} 頁
											(總計 {{ state.pagination.totalItems }} 筆資料)
										</p>
									</div>
								</div>
							</nav>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">
	import { computed, onMounted, ref, watch } from 'vue';
	import { useRoute, useRouter } from 'vue-router';
	import CompanyCard from '~/components/CompanyCard.vue';
	import SearchFilter from '~/components/SearchFilter.vue';
	import { useStockGifts } from '~/composables/useStockGifts';

	const { state, companies, fetchData, updateFilters } = useStockGifts();
	const currentPage = ref(1);
	const itemsPerPage = ref(18);

	// SEO 設定
	useHead({
		title: '台灣上市公司列表 - 股票紀念品資訊平台',
		meta: [
			{
				name: 'description',
				content:
					'瀏覽所有有發行股票紀念品的台灣上市公司，探索他們的特色收藏品。提供最完整的上市公司紀念品資訊。',
			},
		],
	});

	// 從 URL 讀取查詢參數
	const route = useRoute();
	const router = useRouter();

	// 初始化時從 URL 讀取參數
	onMounted(() => {
		const { page, search, category, canBuy } = route.query;

		if (page) {
			currentPage.value = parseInt(page as string);
		}

		// 套用 URL 中的篩選條件
		updateFilters({
			search: (search as string) || '',
			category: (category as string) || '',
			canBuy: canBuy === 'true',
		});

		fetchData(currentPage.value, itemsPerPage.value);
	});

	// 更新 URL 查詢參數
	const updateQueryParams = (params: Record<string, string | number | boolean>) => {
		const query = { ...route.query };

		Object.entries(params).forEach(([key, value]) => {
			if (value !== undefined && value !== null && value !== '') {
				query[key] = encodeURIComponent(String(value));
			} else {
				// 使用 delete 操作符刪除屬性
				Reflect.deleteProperty(query, key);
			}
		});

		router.push({ query });
	};

	// 從 SearchFilter 元件套用篩選的函數
	const applyFilters = async (newFilterParams: {
		search: string;
		category: string;
		canBuy: boolean;
	}) => {
		await updateFilters(newFilterParams);

		// 更新 URL 查詢參數
		updateQueryParams({
			...newFilterParams,
			page: 1, // 重置到第一頁
		});
	};

	// 切換頁面的函數
	const changePage = (newPage: number) => {
		if (state.value.pagination && newPage >= 1 && newPage <= state.value.pagination.totalPages) {
			currentPage.value = newPage;

			// 更新 URL 查詢參數
			updateQueryParams({
				...state.value.filterParams,
				page: newPage,
			});
		}
	};

	// 監聽頁碼變化以重新獲取資料
	watch(
		[currentPage, itemsPerPage],
		([newPage, newLimit]) => {
			fetchData(newPage, newLimit);
		},
		{ immediate: false },
	);

	// 分頁顯示邏輯
	const pageRange = computed(() => {
		if (!state.value.pagination) return [];
		const { page, totalPages } = state.value.pagination;
		const range = [];
		const maxPagesToShow = 5;

		let startPage = Math.max(1, page - Math.floor(maxPagesToShow / 2));
		const endPage = Math.min(totalPages, startPage + maxPagesToShow - 1);

		if (endPage - startPage + 1 < maxPagesToShow && startPage > 1) {
			startPage = Math.max(1, endPage - maxPagesToShow + 1);
		}

		for (let i = startPage; i <= endPage; i++) {
			range.push(i);
		}
		return range;
	});
</script>
