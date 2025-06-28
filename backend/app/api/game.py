# -*- coding: utf-8 -*-
from fastapi import APIRouter, HTTPException
from typing import Dict
from ..models.game import (
    GameStartResponse, GameStatusResponse, AskQuestionRequest, 
    AskQuestionResponse
)
from ..services.game_manager import game_manager

router = APIRouter(prefix="/api/game", tags=["game"])


@router.post("/start", response_model=GameStartResponse)
async def start_game() -> GameStartResponse:
    """开始新游戏"""
    try:
        session = game_manager.start_new_game()
        return GameStartResponse(
            session_id=session.session_id,
            message="游戏开始！我已经想好了一个知名人物，请开始提问来猜测这个人物是谁。"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"创建游戏失败: {str(e)}")


@router.get("/{session_id}", response_model=GameStatusResponse)
async def get_game_status(session_id: str) -> GameStatusResponse:
    """获取游戏状态"""
    session = game_manager.get_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="游戏会话不存在")
    
    return GameStatusResponse(
        session_id=session.session_id,
        status=session.status,
        questions_count=len(session.questions_asked),
        created_at=session.created_at
    )


@router.post("/{session_id}/ask", response_model=AskQuestionResponse)
async def ask_question(session_id: str, request: AskQuestionRequest) -> AskQuestionResponse:
    """提问"""
    session = game_manager.get_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="游戏会话不存在")
    
    if session.status != "active":
        raise HTTPException(status_code=400, detail="游戏已结束")
    
    answer = game_manager.ask_question(session_id, request.question)
    if answer is None:
        raise HTTPException(status_code=500, detail="处理问题失败")
    
    return AskQuestionResponse(
        question=request.question,
        answer=answer,
        questions_count=len(session.questions_asked)
    )




@router.delete("/{session_id}")
async def end_game(session_id: str) -> Dict[str, str]:
    """结束游戏"""
    success = game_manager.delete_session(session_id)
    if not success:
        raise HTTPException(status_code=404, detail="游戏会话不存在")
    
    return {"message": "游戏已结束"}


@router.get("/stats/overview")
async def get_stats() -> Dict[str, int]:
    """获取游戏统计信息"""
    from ..utils.wikipedia import wikipedia_service
    stats = game_manager.get_session_stats()
    stats["total_people"] = wikipedia_service.get_people_count()
    return stats