import { defineCachedEventHandler } from '#imports';
import { getQuery } from 'h3';
import { StockGift } from '~/server/models/StockGift.model';
import type { StockGiftQueryParams } from '~/types/api/stock-gift';

export default defineCachedEventHandler(
	async (event) => {
		try {
			const query = getQuery(event) as Record<string, string>;
			const page = Number(query.page) || 1;
			const limit = Number(query.limit) || 10;
			const skip = (page - 1) * limit;

			// 建立查詢條件
			const filter: Record<string, any> = {};
			if (query.search) {
				filter.$or = [
					{ company_name: { $regex: query.search, $options: 'i' } },
					{ stock_id: { $regex: query.search, $options: 'i' } },
					{ 'gift.name': { $regex: query.search, $options: 'i' } },
				];
			}
			if (query.category) {
				const categories = Array.isArray(query.category) ? query.category : [query.category];
				filter['gift.category'] = { $in: categories };
			}
			if (query.canBuy === 'true') {
				const today = new Date();
				const currentMonth = today.getMonth() + 1;
				const currentDay = today.getDate();
				filter['gift.final_buy_date'] = {
					$regex: new RegExp(
						`^${currentMonth.toString().padStart(2, '0')}/${currentDay.toString().padStart(2, '0')}`,
					),
				};
			}

			// 使用 Mongoose 模型查詢
			const [stockGifts, totalDocuments] = await Promise.all([
				StockGift.find(filter).skip(skip).limit(limit).lean(),
				StockGift.countDocuments(filter),
			]);

			return {
				success: true,
				data: stockGifts,
				pagination: {
					page,
					limit,
					totalItems: totalDocuments,
					totalPages: Math.ceil(totalDocuments / limit),
				},
			};
		} catch (error) {
			console.error('Error fetching stock gifts:', error);
			throw createError({
				statusCode: 500,
				statusMessage: 'Internal Server Error',
			});
		}
	},
	{
		name: 'stock-gifts-api',
		getKey: (event) => {
			const query = getQuery(event) as StockGiftQueryParams;

			const page = query.page || '1';
			const limit = query.limit || '18';
			const search = query.search || '';
			const category = Array.isArray(query.category)
				? query.category.join('-')
				: query.category || '';
			const canBuy = query.canBuy ? 'true' : 'false';

			return `stock_gifts_page_${page}_limit_${limit}_search_${encodeURIComponent(search)}_category_${encodeURIComponent(category)}_canBuy_${canBuy}`;
		},
		maxAge: 60 * 10, // 10 minutes
	},
);
