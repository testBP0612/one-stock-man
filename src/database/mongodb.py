import os
import logging
from typing import List, Dict
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ServerSelectionTimeoutError, OperationFailure

from ..config.settings import (
    MONGODB_URI,
    MONGODB_DB_NAME,
    MONGODB_COLLECTION_PREFIX,
    CURRENT_YEAR
)

class MongoDBManager:
    def __init__(self):
        self.client = None
        self.db = None
        self.collection = None
        self.collection_name = f"{MONGODB_COLLECTION_PREFIX}_{CURRENT_YEAR}"
        
    async def connect(self) -> bool:
        """連線到 MongoDB"""
        try:
            if not MONGODB_URI:
                logging.error("未設定 MongoDB 連線字串")
                return False
                
            self.client = AsyncIOMotorClient(MONGODB_URI)
            self.db = self.client[MONGODB_DB_NAME]
            self.collection = self.db[self.collection_name]
            
            # 測試連線
            await self.client.admin.command('ping')
            logging.info(f"成功連線到 MongoDB，資料庫: {MONGODB_DB_NAME}，集合: {self.collection_name}")
            return True
            
        except (ServerSelectionTimeoutError, OperationFailure) as e:
            logging.error(f"MongoDB 連線失敗: {e}")
            return False
            
    async def save_data(self, data: List[Dict]) -> int:
        """儲存資料到 MongoDB"""
        try:
            if not self.collection:
                if not await self.connect():
                    logging.error("MongoDB 未連線")
                    return 0
                
            # 刪除舊資料
            await self.collection.delete_many({})
            
            # 插入新資料
            if data:
                result = await self.collection.insert_many(data)
                saved_count = len(result.inserted_ids)
                logging.info(f"成功儲存 {saved_count} 筆資料")
                return saved_count
            else:
                logging.warning("沒有資料需要儲存")
                return 0
            
        except Exception as e:
            logging.error(f"儲存資料時發生錯誤: {e}")
            return 0
            
    async def close(self):
        """關閉 MongoDB 連線"""
        if self.client:
            self.client.close()
            logging.info("已關閉 MongoDB 連線") 