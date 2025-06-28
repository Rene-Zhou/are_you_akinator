# -*- coding: utf-8 -*-
from fastapi import APIRouter
from typing import Dict

router = APIRouter()


@router.get("/health")
async def health_check() -> Dict[str, str]:
    """健康检查端点"""
    return {"status": "healthy", "service": "are-you-akinator"}


@router.get("/")
async def root() -> Dict[str, str]:
    """根端点"""
    return {"message": "欢迎使用反向天才游戏 API", "version": "0.1.0"}