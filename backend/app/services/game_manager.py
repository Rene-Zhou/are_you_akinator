# -*- coding: utf-8 -*-
import uuid
from datetime import datetime
from typing import Dict, Optional, List
from ..models.game import GameSession, GameStatus, Question
from ..models.person import PersonInfo
from ..utils.wikipedia import wikipedia_service
from ..services.ai_service import ai_service


class GameManager:
    def __init__(self):
        self.sessions: Dict[str, GameSession] = {}
    
    def start_new_game(self) -> GameSession:
        """开始新游戏"""
        # 生成会话ID
        session_id = str(uuid.uuid4())
        
        # 随机选择人物
        person_name = wikipedia_service.get_random_person()
        
        # 获取人物信息
        person_info = wikipedia_service.get_person_info(person_name)
        
        if not person_info:
            # 如果获取失败，使用备用人物
            person_info = PersonInfo(
                name=person_name,
                summary=f"{person_name} is a famous person.",
                birth_date=None,
                nationality=None,
                occupation=["Celebrity"],
                known_for=["Being famous"],
                categories=["Famous people"],
                additional_info={}
            )
        
        # 创建游戏会话
        session = GameSession(
            session_id=session_id,
            person_name=person_info.name,
            person_info=person_info,
            questions_asked=[],
            status=GameStatus.ACTIVE,
            created_at=datetime.now()
        )
        
        # 存储会话
        self.sessions[session_id] = session
        
        return session
    
    def get_session(self, session_id: str) -> Optional[GameSession]:
        """获取游戏会话"""
        return self.sessions.get(session_id)
    
    def ask_question(self, session_id: str, question: str) -> Optional[str]:
        """处理用户问题"""
        session = self.sessions.get(session_id)
        if not session or session.status != GameStatus.ACTIVE:
            return None
        
        # 构建对话历史
        conversation_history = []
        for q in session.questions_asked[-5:]:  # 只保留最近5个问答
            conversation_history.extend([
                {"role": "user", "content": q.question},
                {"role": "assistant", "content": q.answer}
            ])
        
        # 获取AI回答
        answer = ai_service.answer_question(
            question, 
            session.person_info, 
            conversation_history
        )
        
        # 记录问答
        question_record = Question(
            question=question,
            answer=answer,
            timestamp=datetime.now()
        )
        session.questions_asked.append(question_record)
        
        # 如果AI回答"你猜对了"，自动结束游戏
        if answer == "你猜对了":
            session.status = GameStatus.WON
        
        return answer
    
    
    def end_game(self, session_id: str) -> bool:
        """结束游戏"""
        session = self.sessions.get(session_id)
        if not session:
            return False
        
        session.status = GameStatus.ABANDONED
        return True
    
    def delete_session(self, session_id: str) -> bool:
        """删除游戏会话"""
        if session_id in self.sessions:
            del self.sessions[session_id]
            return True
        return False
    
    def get_session_stats(self) -> Dict[str, int]:
        """获取会话统计信息"""
        stats = {
            "total_sessions": len(self.sessions),
            "active_sessions": sum(1 for s in self.sessions.values() if s.status == GameStatus.ACTIVE),
            "won_sessions": sum(1 for s in self.sessions.values() if s.status == GameStatus.WON),
            "abandoned_sessions": sum(1 for s in self.sessions.values() if s.status == GameStatus.ABANDONED)
        }
        return stats
    
    def cleanup_old_sessions(self, max_age_hours: int = 24):
        """清理过期的会话"""
        current_time = datetime.now()
        expired_sessions = []
        
        for session_id, session in self.sessions.items():
            age_hours = (current_time - session.created_at).total_seconds() / 3600
            if age_hours > max_age_hours:
                expired_sessions.append(session_id)
        
        for session_id in expired_sessions:
            del self.sessions[session_id]
        
        return len(expired_sessions)


# 全局实例
game_manager = GameManager()