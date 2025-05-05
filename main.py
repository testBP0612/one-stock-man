import asyncio
import time
import logging

from src.utils.logger import setup_logger
from src.services.scraper import StockGiftScraper
from src.database.mongodb import MongoDBManager

async def main():
    # 設定日誌
    setup_logger()
    
    start_time = time.time()
    scraper = StockGiftScraper()
    db_manager = MongoDBManager()
    
    try:
        # 爬取資料
        results = await scraper.scrape()
        
        # 儲存到資料庫
        if results:
            saved_count = await db_manager.save_data(results)
            logging.info(f"成功儲存 {saved_count} 筆資料到資料庫")
        
        # 顯示結果
        logging.info("\n爬取結果:")
        for i, result in enumerate(results[:3], 1):  # 只顯示前三筆
            logging.info(f"{i}. 股票代號: {result['stock_id']}, 公司名稱: {result['company_name']}")
            logging.info(f"   紀念品: {result['gift']}")
            logging.info("-"*50)
        
        logging.info(f"\n總共爬取 {len(results)} 筆資料")
        logging.info(f"執行時間: {time.time() - start_time:.2f} 秒")
    except Exception as e:
        logging.error(f"程式執行時發生錯誤: {e}")
        import traceback
        logging.error(traceback.format_exc())
    finally:
        await db_manager.close()

if __name__ == "__main__":
    asyncio.run(main()) 