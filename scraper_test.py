import requests
from bs4 import BeautifulSoup
import time

def test_scraper():
    url = "https://histock.tw/stock/gift.aspx"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    
    try:
        print("Start scraping...")
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        print("Parsing HTML...")
        soup = BeautifulSoup(response.text, "lxml")
        
        # 找到所有的表格
        tables = soup.find_all("table", class_="gvTB")
        
        if not tables:
            print("No tables found")
            return
            
        print(f"找到 {len(tables)} 個表格")
        
        # 處理每個表格
        for table_index, table in enumerate(tables):
            # 找到表格前的標題
            previous_h5 = table.find_previous("h5")
            table_title = previous_h5.text if previous_h5 else f"表格 {table_index+1}"
            
            print("\n" + "="*60)
            print(f"表格: {table_title}")
            print("="*60)
            
            rows = table.find_all("tr")
            print(f"此表格包含 {len(rows)-1} 筆資料")
            
            # 獲取表頭
            header_row = rows[0]
            headers = [th.text.strip() for th in header_row.find_all("th")]
            print(f"表頭: {', '.join(headers)}")
            
            # 只顯示前3筆資料
            for i, row in enumerate(rows[1:4], 1):
                cells = row.find_all("td")
                if len(cells) >= 3:
                    stock_id = cells[0].text.strip()
                    company_name = cells[1].text.strip()
                    gift = cells[2].text.strip()
                    print(f"{i}. 股票代號: {stock_id}, 公司名稱: {company_name}")
                    print(f"   紀念品: {gift}")
                    print("-"*50)
        
        print("\nScraping done")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()
        
if __name__ == "__main__":
    print("Start testing...")
    start_time = time.time()
    test_scraper()
    print(f"Done in {time.time() - start_time:.2f} sec")