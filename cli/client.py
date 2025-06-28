# -*- coding: utf-8 -*-
import httpx
from typing import Optional, Dict, Any
from .config import cli_settings


class APIClient:
    def __init__(self):
        self.base_url = cli_settings.api_base_url
        self.timeout = cli_settings.timeout
        self.session_id: Optional[str] = None
    
    async def start_game(self) -> Dict[str, Any]:
        """开始新游戏"""
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.post(f"{self.base_url}/api/game/start")
            response.raise_for_status()
            data = response.json()
            self.session_id = data.get("session_id")
            return data
    
    async def ask_question(self, question: str) -> Dict[str, Any]:
        """提问"""
        if not self.session_id:
            raise ValueError("游戏未开始，请先开始游戏")
        
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.post(
                f"{self.base_url}/api/game/{self.session_id}/ask",
                json={"question": question}
            )
            response.raise_for_status()
            return response.json()
    
    
    async def get_game_status(self) -> Dict[str, Any]:
        """获取游戏状态"""
        if not self.session_id:
            raise ValueError("游戏未开始，请先开始游戏")
        
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.get(f"{self.base_url}/api/game/{self.session_id}")
            response.raise_for_status()
            return response.json()
    
    async def end_game(self) -> Dict[str, Any]:
        """结束游戏"""
        if not self.session_id:
            raise ValueError("游戏未开始，请先开始游戏")
        
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.delete(f"{self.base_url}/api/game/{self.session_id}")
            response.raise_for_status()
            data = response.json()
            self.session_id = None
            return data
    
    async def check_health(self) -> bool:
        """检查服务器健康状态"""
        try:
            async with httpx.AsyncClient(timeout=5) as client:
                response = await client.get(f"{self.base_url}/health")
                return response.status_code == 200
        except:
            return False