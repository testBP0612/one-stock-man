from typing import List, Dict, Optional
from datetime import datetime
import pytz

from ..config.settings import TAIPEI_TZ

class StockGift:
    def __init__(
        self,
        stock_id: str,
        company_name: str,
        gift_name: str,
        categories: Optional[List[str]] = None,
        final_buy_date: Optional[str] = None,
        shareholders_meeting_date: Optional[str] = None,
        year: Optional[int] = None,
        updated_at: Optional[datetime] = None
    ):
        self.stock_id = stock_id
        self.company_name = company_name
        self.gift = {
            "name": gift_name,
            "category": categories or [],
            "final_buy_date": final_buy_date,
            "shareholders_meeting_date": shareholders_meeting_date
        }
        self.year = year or datetime.now(TAIPEI_TZ).year
        self.updated_at = updated_at or datetime.now(TAIPEI_TZ)

    def to_dict(self) -> Dict:
        """轉換為字典格式"""
        return {
            "stock_id": self.stock_id,
            "company_name": self.company_name,
            "gift": self.gift,
            "year": self.year,
            "updated_at": self.updated_at
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'StockGift':
        """從字典建立物件"""
        gift_data = data["gift"]
        return cls(
            stock_id=data["stock_id"],
            company_name=data["company_name"],
            gift_name=gift_data["name"],
            categories=gift_data.get("category", []),
            final_buy_date=gift_data.get("final_buy_date"),
            shareholders_meeting_date=gift_data.get("shareholders_meeting_date"),
            year=data.get("year"),
            updated_at=data.get("updated_at")
        ) 