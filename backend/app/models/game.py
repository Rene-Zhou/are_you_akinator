# -*- coding: utf-8 -*-
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from enum import Enum

from .person import PersonInfo


class GameStatus(str, Enum):
    ACTIVE = "active"
    WON = "won"
    ABANDONED = "abandoned"


class Question(BaseModel):
    question: str
    answer: str
    timestamp: datetime


class GameSession(BaseModel):
    session_id: str
    person_name: str
    person_info: PersonInfo
    questions_asked: List[Question] = []
    status: GameStatus = GameStatus.ACTIVE
    created_at: datetime
    
    class Config:
        use_enum_values = True


class GameStartResponse(BaseModel):
    session_id: str
    message: str = "游戏开始！请开始提问来猜测我想的人物。"


class GameStatusResponse(BaseModel):
    session_id: str
    status: GameStatus
    questions_count: int
    created_at: datetime


class AskQuestionRequest(BaseModel):
    question: str


class AskQuestionResponse(BaseModel):
    question: str
    answer: str
    questions_count: int


