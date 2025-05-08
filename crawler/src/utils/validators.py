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
        
    # 檢查日期格式（如果有的話）
    gift = data["gift"]
    if "final_buy_date" in gift and gift["final_buy_date"]:
        if not isinstance(gift["final_buy_date"], str):
            return False
    if "shareholders_meeting_date" in gift and gift["shareholders_meeting_date"]:
        if not isinstance(gift["shareholders_meeting_date"], str):
            return False
    
    return True

def clean_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """清理資料"""
    cleaned_gift = {
        "name": data["gift"]["name"].strip(),
        "final_buy_date": data["gift"].get("final_buy_date", "").strip() or None,
        "shareholders_meeting_date": data["gift"].get("shareholders_meeting_date", "").strip() or None
    }
    
    return {
        "stock_id": data["stock_id"].strip(),
        "company_name": data["company_name"].strip(),
        "gift": cleaned_gift
    } 