# -*- coding: utf-8 -*-
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import health, game
from .config.settings import settings
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用生命周期事件"""
    # 启动事件
    print("🚀 反向天才游戏服务器启动中...")
    print(f"📖 API文档: http://localhost:{settings.port}/docs")
    print(f"🔧 调试模式: {'开启' if settings.debug else '关闭'}")
    
    yield
    
    # 关闭事件
    print("🛑 反向天才游戏服务器关闭")


app = FastAPI(
    title="反向天才 (Reverse Akinator)",
    description="AI预设知名人物，人类猜测的反向Akinator游戏",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# CORS配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中应该设置具体的域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(health.router)
app.include_router(game.router)


if __name__ == "__main__":
    uvicorn.run(
        "backend.app.main:app",
        host="0.0.0.0",
        port=settings.port,
        reload=settings.debug,
        log_level=settings.log_level.lower()
    )