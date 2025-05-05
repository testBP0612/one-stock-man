import logging
import os

def setup_logger():
    """設定日誌"""
    # 確保日誌目錄存在
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 設定日誌格式
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[
            logging.FileHandler(os.path.join(log_dir, 'scraper.log')),
            logging.StreamHandler()
        ]
    ) 