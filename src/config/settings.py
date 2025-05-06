import os
from dotenv import load_dotenv
import pytz
from datetime import datetime

# 載入環境變數
load_dotenv()

# 時區設定
TAIPEI_TZ = pytz.timezone('Asia/Taipei')

# MongoDB 設定
MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DB_NAME = "stock_gifts"
MONGODB_COLLECTION_PREFIX = "gifts"

# 集合名稱設定（使用當前年度）
CURRENT_YEAR = datetime.now(TAIPEI_TZ).year

# OpenAI 設定
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 爬蟲設定
SCRAPER_URL = "https://histock.tw/stock/gift.aspx"
SCRAPER_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}

# 重試設定
MAX_RETRIES = 3
MIN_RETRY_DELAY = 4
MAX_RETRY_DELAY = 10

# 請求超時設定
REQUEST_TIMEOUT = 10 