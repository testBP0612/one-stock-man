import type { ApiResponse, PaginationInfo, StockGift } from '~/types/api/stock-gift';

interface StockGiftsState {
	companies: StockGift[];
	pagination: PaginationInfo | null;
	error: Error | null;
	pending: boolean;
	filterParams: {
		search: string;
		category: string;
		canBuy: boolean;
	};
}

export const useStockGifts = () => {
	const state = useState<StockGiftsState>('stockGifts', () => ({
		companies: [],
		pagination: null,
		error: null,
		pending: false,
		filterParams: {
			search: '',
			category: '',
			canBuy: false,
		},
	}));

	const fetchData = async (page: number, limit: number) => {
		state.value.pending = true;
		state.value.error = null;
		let retryCount = 0;
		const maxRetries = 3;
		const retryDelay = 1000;

		const attemptFetch = async (): Promise<void> => {
			try {
				const response = await $fetch<ApiResponse>('/api/stock-gifts', {
					query: {
						page,
						limit,
						search: state.value.filterParams.search || undefined,
						category: state.value.filterParams.category || undefined,
						canBuy: state.value.filterParams.canBuy || undefined,
					},
				});

				if (response.success && response.data) {
					state.value.companies = response.data;
					state.value.pagination = response.pagination || null;
				} else {
					throw new Error(response.error || 'API 回傳不成功的回應');
				}
			} catch (err) {
				if (retryCount < maxRetries) {
					retryCount++;
					console.log(`重試第 ${retryCount} 次...`);
					await new Promise((resolve) => setTimeout(resolve, retryDelay));
					return attemptFetch();
				}
				throw err;
			}
		};

		try {
			await attemptFetch();
		} catch (err) {
			state.value.error = err instanceof Error ? err : new Error('發生未知錯誤');
			state.value.companies = [];
			state.value.pagination = null;
		} finally {
			state.value.pending = false;
		}
	};

	const updateFilters = async (newFilters: Partial<typeof state.value.filterParams>) => {
		state.value.filterParams = {
			...state.value.filterParams,
			...newFilters,
		};
		// 重置到第一頁並重新獲取資料
		await fetchData(1, state.value.pagination?.limit || 10);
	};

	const resetState = () => {
		state.value = {
			companies: [],
			pagination: null,
			error: null,
			pending: false,
			filterParams: {
				search: '',
				category: '',
				canBuy: false,
			},
		};
	};

	return {
		state: readonly(state),
		companies: computed(() => state.value.companies),
		fetchData,
		updateFilters,
		resetState,
	};
};
