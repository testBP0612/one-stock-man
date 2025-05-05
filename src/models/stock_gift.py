from typing import Dict, Optional
from datetime import datetime
from pydantic import BaseModel, Field, validator

class StockGift(BaseModel):
    """股票紀念品資料模型"""
    stock_id: str = Field(..., description="股票代號")
    company_name: str = Field(..., description="公司名稱")
    gift: str = Field(..., description="紀念品")
    year: Optional[int] = Field(None, description="年度")
    created_at: Optional[datetime] = Field(None, description="建立時間")

    @validator('stock_id')
    def validate_stock_id(cls, v):
        """驗證股票代號"""
        if not v.isdigit():
            raise ValueError("股票代號必須是數字")
        return v

    @classmethod
    def from_dict(cls, data: Dict) -> 'StockGift':
        """從字典建立 StockGift 實例"""
        return cls(**data)

    def to_dict(self) -> Dict:
        """轉換為字典格式"""
        return self.model_dump() 