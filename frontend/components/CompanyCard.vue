<template>
	<div
		class="card group overflow-hidden transition-all duration-300 hover:scale-[1.01] hover:transform"
		@mouseenter="isHovered = true"
		@mouseleave="isHovered = false"
	>
		<div class="p-5">
			<div class="flex items-center justify-between">
				<h3
					class="group-hover:text-primary-600 text-lg font-bold text-gray-900 transition-colors duration-200"
				>
					{{ company.company_name }}
				</h3>
				<p class="text-sm text-gray-500">{{ company.stock_id }}</p>
			</div>

			<div class="mt-4 flex flex-wrap justify-between gap-x-4 gap-y-2">
				<div class="flex w-full flex-col">
					<span class="text-sm text-gray-500">紀念品</span>
					<span class="text-sm font-semibold">{{ company.gift.name }}</span>
				</div>

				<div class="flex flex-col">
					<span class="text-sm text-gray-500">最後買進日</span>
					<span
						class="text-sm font-semibold"
						:class="{ 'text-error-500': isFinalBuyDateExpired }"
					>
						{{ company.gift.final_buy_date }}
					</span>
				</div>

				<div class="flex flex-col">
					<span class="text-sm text-gray-500">股東會日期</span>
					<span class="text-sm font-semibold">{{ company.gift.shareholders_meeting_date }}</span>
				</div>
			</div>

			<div class="mt-3 flex flex-wrap gap-2">
				<span
					v-for="category in company.gift.category"
					:key="category"
					:class="`tag tag-${giftCategoryMap[category as keyof typeof giftCategoryMap]}`"
				>
					{{ category }}
				</span>
			</div>
		</div>
	</div>
</template>

<script lang="ts" setup>
	import { DateTime } from 'luxon';
	import GIFT_CATEGORY_MAP from '~/config/category';
	import type { StockGift } from '~/types/api/stock-gift';

	interface Props {
		company: StockGift;
	}

	const props = defineProps<Props>();

	const isHovered = ref(false);
	const isWishlisted = ref(false);
	const giftCategoryMap = ref(GIFT_CATEGORY_MAP);

	const isFinalBuyDateExpired = computed(() => {
		if (!props.company.gift.final_buy_date) return false;

		const finalBuyDate = DateTime.fromFormat(props.company.gift.final_buy_date, 'MM/dd');
		const today = DateTime.now().startOf('day');

		if (!finalBuyDate.isValid) {
			console.error('日期格式錯誤:', props.company.gift.final_buy_date);
			return false;
		}

		return finalBuyDate < today;
	});
</script>
