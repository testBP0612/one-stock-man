import logging
from typing import Dict, Any

def validate_stock_gift_data(data: Dict[str, Any]) -> bool:
    """驗證股票紀念品資料"""
    required_fields = ["stock_id", "company_name", "gift"]
    
    # 檢查必要欄位
    for field in required_fields:
        if field not in data or not data[field]:
            return False
    
    # 檢查股票代號格式
    if not data["stock_id"].isdigit():
        return False
    
    # 檢查 gift 結構
    if not isinstance(data["gift"], dict) or "name" not in data["gift"]:
        return False
    
    return True

def clean_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """清理資料"""
    return {
        "stock_id": data["stock_id"].strip(),
        "company_name": data["company_name"].strip(),
        "gift": {
            "name": data["gift"]["name"].strip()
        }
    } 