interface CategoryCounts {
	[key: string]: number;
}

interface CategoryCountsResponse {
	success: boolean;
	data: CategoryCounts;
	error?: string;
}

export const useCategoryCounts = () => {
	const state = useState<{
		counts: CategoryCounts | null;
		error: Error | null;
		pending: boolean;
	}>('categoryCounts', () => ({
		counts: null,
		error: null,
		pending: false,
	}));

	const fetchCounts = async () => {
		state.value.pending = true;
		state.value.error = null;

		try {
			const response = await $fetch<CategoryCountsResponse>('/api/categories/count');
			if (response.success && response.data) {
				state.value.counts = response.data;
			} else {
				throw new Error(response.error || '無法取得分類計數');
			}
		} catch (err) {
			state.value.error = err instanceof Error ? err : new Error('發生未知錯誤');
			state.value.counts = null;
		} finally {
			state.value.pending = false;
		}
	};

	return {
		state: readonly(state),
		fetchCounts,
	};
};
