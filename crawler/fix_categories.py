import asyncio
import logging
from src.database.mongodb import MongoDBManager

async def fix_categories():
    # 初始化 MongoDB 連接
    db_manager = MongoDBManager()
    
    try:
        # 連線到資料庫
        if not await db_manager.connect():
            logging.error("無法連線到 MongoDB")
            return
            
        # 取得所有資料
        collection = db_manager.collection
        cursor = collection.find()
        gifts = await cursor.to_list(length=None)  # 轉換為列表
        
        # 計數器
        total_count = 0
        fixed_count = 0
        
        # 處理每一筆資料
        for gift in gifts:
            total_count += 1
            categories = gift["gift"]["category"]
            
            # 檢查是否需要修正
            if len(categories) == 1 and "," in categories[0]:
                # 分割分類並清理
                fixed_categories = [cat.strip() for cat in categories[0].split(",")]
                fixed_categories = list(set(filter(None, fixed_categories)))
                
                # 更新資料庫
                await collection.update_one(
                    {"_id": gift["_id"]},
                    {"$set": {"gift.category": fixed_categories}}
                )
                fixed_count += 1
                
                # 顯示修正結果
                logging.info(f"已修正: {gift['stock_id']} - {gift['gift']['name']}")
                logging.info(f"  原始分類: {categories}")
                logging.info(f"  修正後分類: {fixed_categories}")
                logging.info("-"*50)
        
        # 顯示統計資訊
        logging.info(f"\n總共處理 {total_count} 筆資料")
        logging.info(f"修正了 {fixed_count} 筆資料的分類格式")
        
    except Exception as e:
        logging.error(f"修正資料時發生錯誤: {e}")
        import traceback
        logging.error(traceback.format_exc())
    finally:
        # 關閉 MongoDB 連接
        await db_manager.close()

if __name__ == "__main__":
    asyncio.run(fix_categories()) 