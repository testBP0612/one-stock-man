<template>
	<div class="sticky top-20 rounded-lg bg-white p-4 shadow-sm">
		<div class="mb-4">
			<label
				for="search"
				class="block text-sm font-medium text-gray-700"
			>
				搜尋
			</label>
			<div class="relative mt-1 rounded-md shadow-sm">
				<div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
					<svg
						class="h-5 w-5 text-gray-400"
						xmlns="http://www.w3.org/2000/svg"
						viewBox="0 0 20 20"
						fill="currentColor"
						aria-hidden="true"
					>
						<path
							fill-rule="evenodd"
							d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
							clip-rule="evenodd"
						/>
					</svg>
				</div>
				<input
					id="search"
					v-model="searchQuery"
					type="text"
					name="search"
					class="focus:border-primary-500 focus:ring-primary-500 block w-full rounded-md border border-gray-300 bg-white py-2 pr-3 pl-10 text-sm placeholder-gray-400 focus:ring-1 focus:outline-none"
					placeholder="搜尋公司或紀念品"
				/>
			</div>
		</div>

		<div class="mb-4">
			<label
				for="category"
				class="block text-sm font-medium text-gray-700"
			>
				分類
			</label>
			<div class="relative mt-1">
				<select
					id="category"
					v-model="selectedCategory"
					class="input focus:border-primary-500 focus:ring-primary-500 block w-full appearance-none rounded-md border border-gray-300 bg-white py-2 pr-10 pl-3 text-base focus:outline-none sm:text-sm"
				>
					<option value="">全部分類</option>
					<option
						v-for="category in categories"
						:key="category"
						:value="category"
					>
						{{ category }}
					</option>
				</select>
				<div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2">
					<svg
						class="h-5 w-5 text-gray-400"
						xmlns="http://www.w3.org/2000/svg"
						viewBox="0 0 20 20"
						fill="currentColor"
						aria-hidden="true"
					>
						<path
							fill-rule="evenodd"
							d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
							clip-rule="evenodd"
						/>
					</svg>
				</div>
			</div>
		</div>

		<div class="space-y-2">
			<label class="group relative flex cursor-pointer items-center">
				<input
					v-model="filters.canBuy"
					type="checkbox"
					class="peer sr-only"
				/>
				<div
					class="peer-checked:border-primary-500 peer-checked:bg-primary-500 peer-focus:ring-primary-500 h-5 w-5 rounded border border-gray-300 bg-white transition-colors peer-focus:ring-2 peer-focus:ring-offset-2"
				>
					<svg
						class="h-4 w-4 text-white opacity-0 transition-opacity peer-checked:opacity-100"
						xmlns="http://www.w3.org/2000/svg"
						viewBox="0 0 20 20"
						fill="currentColor"
					>
						<path
							fill-rule="evenodd"
							d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
							clip-rule="evenodd"
						/>
					</svg>
				</div>
				<span class="ml-2 text-sm text-gray-700 group-hover:text-gray-900">最後買進日未過期</span>
			</label>
		</div>

		<div class="mt-4 flex space-x-2">
			<button
				class="btn-primary flex-1 rounded-md border border-gray-300 px-4 py-2 shadow-sm"
				@click="applyFilters"
			>
				套用篩選
			</button>
			<button
				class="btn-outline flex-1 rounded-md border border-gray-300 px-4 py-2 shadow-sm"
				@click="resetFilters"
			>
				重設
			</button>
		</div>
	</div>
</template>

<script setup lang="ts">
	import { useRoute } from 'vue-router';
	import { useStockGifts } from '~/composables/useStockGifts';
	import GIFT_CATEGORY_MAP from '~/config/category';

	const emit = defineEmits(['filter']);
	const { updateFilters, state } = useStockGifts();
	const route = useRoute();
	const searchQuery = ref('');
	const selectedCategory = ref('');
	const filters = reactive({
		canBuy: false,
	});

	const categories = Object.keys(GIFT_CATEGORY_MAP);

	// 從 URL 初始化篩選條件
	onMounted(() => {
		const { search, category, canBuy } = route.query;

		if (search) {
			try {
				searchQuery.value = decodeURIComponent(search as string);
			} catch (e) {
				searchQuery.value = search as string;
			}
		}

		if (category) {
			try {
				selectedCategory.value = decodeURIComponent(category as string);
			} catch (e) {
				selectedCategory.value = category as string;
			}
		}

		if (canBuy === 'true') {
			filters.canBuy = true;
		}
	});

	const applyFilters = () => {
		const filterParams = {
			search: searchQuery.value,
			category: selectedCategory.value,
			...filters,
		};
		updateFilters(filterParams);
		emit('filter', filterParams);
	};

	const resetFilters = () => {
		searchQuery.value = '';
		selectedCategory.value = '';
		filters.canBuy = false;

		applyFilters();
	};
</script>
