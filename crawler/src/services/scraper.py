import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
import logging
from tenacity import retry, stop_after_attempt, wait_exponential

from ..config.settings import (
    SCRAPER_URL,
    SCRAPER_HEADERS,
    MAX_RETRIES,
    MIN_RETRY_DELAY,
    MAX_RETRY_DELAY,
    REQUEST_TIMEOUT
)
from ..utils.validators import validate_stock_gift_data, clean_data
from ..models.stock_gift import StockGift

class StockGiftScraper:
    def __init__(self):
        self.url = SCRAPER_URL
        self.headers = SCRAPER_HEADERS
        logging.info(f"初始化爬蟲，目標網址: {self.url}")

    @retry(
        stop=stop_after_attempt(MAX_RETRIES),
        wait=wait_exponential(multiplier=1, min=MIN_RETRY_DELAY, max=MAX_RETRY_DELAY)
    )
    def fetch_page(self) -> Optional[str]:
        """取得網頁內容，包含重試機制"""
        try:
            response = requests.get(
                self.url, 
                headers=self.headers,
                timeout=REQUEST_TIMEOUT
            )
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logging.error(f"取得網頁內容時發生錯誤: {e}")
            raise

    def parse_table_headers(self, header_row) -> List[str]:
        """解析表格表頭"""
        return [th.text.strip() for th in header_row.find_all("th")]
    
    def find_final_buy_date_column_index(self, headers: List[str]) -> Optional[int]:
        """尋找最後一次買進日欄位的索引"""
        for i, header in enumerate(headers):
            if "最後買進日" in header:
                return i
        return None
    
    def find_shareholders_meeting_date_column_index(self, headers: List[str]) -> Optional[int]:
        """尋找股東會日期欄位的索引"""
        for i, header in enumerate(headers):
            if "股東會日期" in header:
                return i
        return None

    def find_gift_column_index(self, headers: List[str]) -> Optional[int]:
        """尋找紀念品欄位的索引"""
        for i, header in enumerate(headers):
            if "紀念品" in header:
                return i
        return None

    def clean_gift_text(self, text: str) -> str:
        """清理紀念品文字"""
        return text.strip().replace("參考圖", "").strip()

    def process_table(self, table) -> List[Dict]:
        """處理單個表格的資料"""
        results = []
        rows = table.find_all("tr")
        
        if not rows:
            return results

        headers = self.parse_table_headers(rows[0])
        
        gift_index = self.find_gift_column_index(headers)
        final_buy_date_index = self.find_final_buy_date_column_index(headers)
        shareholders_meeting_date_index = self.find_shareholders_meeting_date_column_index(headers)
        
        if gift_index is None:
            return results

        for row in rows[1:]:
            try:
                cells = row.find_all("td")
                if len(cells) > gift_index:
                    result = {
                        "stock_id": cells[0].text.strip(),
                        "company_name": cells[1].text.strip(),
                        "gift": {
                            "name": self.clean_gift_text(cells[gift_index].text),
                            "final_buy_date": cells[final_buy_date_index].text.strip() if final_buy_date_index is not None and len(cells) > final_buy_date_index else None,
                            "shareholders_meeting_date": cells[shareholders_meeting_date_index].text.strip() if shareholders_meeting_date_index is not None and len(cells) > shareholders_meeting_date_index else None
                        }
                    }
                    if validate_stock_gift_data(result):
                        results.append(clean_data(result))
            except Exception as e:
                continue

        return results

    async def scrape(self) -> List[Dict]:
        """主要爬蟲邏輯"""
        all_results = []
        
        try:
            html_content = self.fetch_page()
            
            if not html_content:
                logging.error("無法取得網頁內容")
                return all_results

            soup = BeautifulSoup(html_content, "lxml")
            tables = soup.find_all("table", class_="gvTB")

            if not tables:
                logging.warning("找不到任何表格")
                return all_results

            for table in tables:
                results = self.process_table(table)
                all_results.extend(results)

            logging.info(f"爬取完成，總共取得 {len(all_results)} 筆資料")
            return all_results

        except Exception as e:
            logging.error(f"爬取過程中發生錯誤: {e}")
            return all_results 