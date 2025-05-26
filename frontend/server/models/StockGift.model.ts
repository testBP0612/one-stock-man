import { Schema, model } from 'mongoose';
import type { StockGiftDocument } from '~/types/database/models';

const schema: Schema = new Schema<StockGiftDocument>(
	{
		stock_id: { type: String, required: true },
		company_name: { type: String, required: true },
		gift: {
			name: { type: String, required: true },
			category: [{ type: String, required: true }],
			final_buy_date: { type: String, required: false },
			shareholders_meeting_date: { type: String, required: false },
		},
	},
	{
		collection: 'gifts_2025',
		timestamps: true, // 自動添加 createdAt 和 updatedAt
	},
);

// 建立索引
schema.index({ stock_id: 1 }, { unique: true });
schema.index({ company_name: 1 });
schema.index({ 'gift.category': 1 });
schema.index({ 'gift.name': 1 });
schema.index({ final_buy_date: 1 });
schema.index({ shareholders_meeting_date: 1 });

// 創建模型
export const StockGift = model<StockGiftDocument>('StockGift', schema);
