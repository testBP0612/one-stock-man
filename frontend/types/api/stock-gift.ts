import type { StockGiftResponse } from '../database/models';

export interface StockGift {
	_id?: string;
	stock_id: string;
	company_name: string;
	gift: {
		name: string;
		category: string[];
		final_buy_date: string;
		shareholders_meeting_date: string;
	};
}

export interface PaginationInfo {
	page: number;
	limit: number;
	totalItems: number;
	totalPages: number;
}

export interface ApiResponse {
	success: boolean;
	data?: StockGiftResponse[];
	pagination?: PaginationInfo;
	error?: string;
	message?: string;
}

// 用於 API 請求的查詢參數
export interface StockGiftQueryParams {
	page?: number;
	limit?: number;
	search?: string;
	category?: string;
	canBuy?: boolean;
	sortBy?: 'name' | 'newest' | 'oldest';
}
