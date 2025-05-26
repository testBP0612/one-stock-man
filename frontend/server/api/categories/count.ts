import { defineCachedEventHandler } from '#imports';
import { StockGift } from '~/server/models/StockGift.model';

export default defineCachedEventHandler(
	async () => {
		try {
			// 使用 MongoDB 的聚合管道來計算每個分類的數量
			const categoryCounts = await StockGift.aggregate([
				// 展開 gift.category 陣列
				{ $unwind: '$gift.category' },
				// 按分類分組並計算數量
				{
					$group: {
						_id: '$gift.category',
						count: { $sum: 1 },
					},
				},
				// 重新格式化輸出
				{
					$project: {
						_id: 0,
						category: '$_id',
						count: 1,
					},
				},
			]);

			// 轉換為更容易使用的格式
			const counts = categoryCounts.reduce((acc, curr) => {
				acc[curr.category] = curr.count;
				return acc;
			}, {});

			return {
				success: true,
				data: counts,
			};
		} catch (error) {
			console.error('Error fetching category counts:', error);
			throw createError({
				statusCode: 500,
				statusMessage: 'Internal Server Error',
			});
		}
	},
	{
		name: 'category-counts-api',
		maxAge: 60 * 60, // 快取 1 小時
	},
);
