# -*- coding: utf-8 -*-
from pydantic import BaseModel
from typing import Dict, List, Optional


class PersonInfo(BaseModel):
    name: str
    summary: str
    birth_date: Optional[str] = None
    nationality: Optional[str] = None
    occupation: List[str] = []
    known_for: List[str] = []
    categories: List[str] = []
    additional_info: Dict[str, str] = {}
    
    class Config:
        json_encoders = {
            # 如果需要特殊编码可以在这里添加
        }