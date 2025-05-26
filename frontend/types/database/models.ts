import type { Document } from 'mongoose';

export interface StockGiftDocument extends Document {
	stock_id: string;
	company_name: string;
	gift: {
		name: string;
		category: string[];
	};
}

// 用於 API 回應的型別
export interface StockGiftResponse {
	_id: string;
	stock_id: string;
	company_name: string;
	gift: {
		name: string;
		category: string[];
		final_buy_date: string;
		shareholders_meeting_date: string;
	};
}

// 用於建立新資料的型別
export interface CreateStockGiftInput {
	stock_id: string;
	company_name: string;
	gift: {
		name: string;
		category: string[];
	};
}

// 用於更新資料的型別
export interface UpdateStockGiftInput {
	stock_id?: string;
	company_name?: string;
	gift?: {
		name?: string;
		category?: string[];
	};
}
