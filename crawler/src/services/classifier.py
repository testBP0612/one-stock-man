import os
import logging
import asyncio
from typing import List, Dict
from openai import OpenAI
from tenacity import retry, stop_after_attempt, wait_exponential

from ..config.settings import (
    OPENAI_API_KEY,
    MAX_RETRIES,
    MIN_RETRY_DELAY,
    MAX_RETRY_DELAY
)

class GiftClassifier:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.system_prompt = """
        你是一個專業的股票紀念品分類專家。

        請根據以下給定的紀念品名稱，嚴格將其分類到下面指定的類別之一或多個：
        1. 禮品卡（如7-11禮券、全家禮物卡、咖啡提領券）
        2. 生活日用品（如肥皂、洗手乳、洗衣精、口罩、濕巾）
        3. 食品與飲品（如咖啡、調味料、米、拌麵、餅乾、茶飲）
        4. 廚房用品（如餐具、料理剪刀、保溫袋、餐盤、玻璃杯）
        5. 電子產品與配件（如手機支架、充電頭、充電線、自拍棒、手電筒）
        6. 居家用品（如毛巾、襪子、購物袋、保鮮盒、香皂）
        7. 特殊用途商品（如股東會員卡、住宿抵用券、遊戲點數卡）
        8. 其他（無法分類於上述任何類別的物品）
        共這八種 [禮品卡, 生活日用品, 食品與飲品, 廚房用品, 電子產品與配件, 居家用品, 特殊用途商品, 其他]

        ## 回覆規則（必須嚴格遵守）：
        - 僅允許使用上述8個類別名稱回覆，不得增加其他文字、符號或解釋。
        - 若適用多個類別，直接以逗號隔開（如："食品與飲品,居家用品"）。
        - 禁止回覆任何額外符號（例如："-"、"•"），僅回覆分類名稱。
        """
        
    @retry(
        stop=stop_after_attempt(MAX_RETRIES),  # 最多重試3次
        wait=wait_exponential(multiplier=2, min=MIN_RETRY_DELAY, max=MAX_RETRY_DELAY)  # 指數退避，最少等待4秒，最多60秒
    )
    async def classify_gift(self, gift_name: str) -> List[str]:
        """使用 GPT 分類紀念品"""
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": f"請分類以下紀念品：{gift_name}"}
                ],
                temperature=0.3,
                max_tokens=100
            )
            
            # 解析回應
            categories = response.choices[0].message.content.strip()
            # 分割分類結果，移除空白和重複
            categories = [cat.strip() for cat in categories.split(",")]
            categories = list(set(filter(None, categories)))
            
            logging.info(f"紀念品 '{gift_name}' 被分類為: {categories}")
            return categories
            
        except Exception as e:
            error_msg = str(e)
            if "rate_limit" in error_msg.lower() or "quota" in error_msg.lower():
                logging.warning(f"API 配額限制，等待重試: {error_msg}")
                raise  # 讓重試機制處理
            else:
                logging.error(f"分類紀念品時發生錯誤: {error_msg}")
                return ["其他"]  # 其他錯誤返回預設類別

    async def classify_gifts(self, gifts: List[Dict]) -> List[Dict]:
        """批量分類紀念品"""
        classified_gifts = []
        batch_size = 2  # 每批次處理的數量
        delay = 1  # 批次之間的延遲（秒）
        max_retries = 3  # 批次處理的最大重試次數
        
        # 將禮物分成小批次
        for i in range(0, len(gifts), batch_size):
            batch = gifts[i:i + batch_size]
            logging.info(f"處理批次 {i//batch_size + 1}，共 {len(batch)} 筆資料")
            
            retry_count = 0
            while retry_count < max_retries:
                try:
                    for gift in batch:
                        try:
                            # 確保 gift 是字典格式
                            if isinstance(gift, str):
                                gift = {"gift": gift}
                            
                            # 確保 gift 字典中有 name 欄位
                            if "name" not in gift["gift"]:
                                gift["gift"] = {"name": gift["gift"]}
                            
                            categories = await self.classify_gift(gift["gift"]["name"])
                            gift["gift"]["category"] = categories
                            classified_gifts.append(gift)
                        except Exception as e:
                            logging.error(f"處理紀念品時發生錯誤: {e}")
                            continue
                    
                    # 批次處理成功，跳出重試循環
                    break
                    
                except Exception as e:
                    retry_count += 1
                    if retry_count < max_retries:
                        wait_time = delay * (2 ** retry_count)  # 指數退避
                        logging.warning(f"批次處理失敗，第 {retry_count} 次重試，等待 {wait_time} 秒...")
                        await asyncio.sleep(wait_time)
                    else:
                        logging.error(f"批次處理失敗，已達到最大重試次數: {e}")
            
            # 批次之間加入延遲
            if i + batch_size < len(gifts):
                logging.info(f"等待 {delay} 秒後處理下一批次...")
                await asyncio.sleep(delay)
                
        return classified_gifts 