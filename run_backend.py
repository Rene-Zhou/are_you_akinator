# -*- coding: utf-8 -*-
"""简单的后端启动脚本"""

if __name__ == "__main__":
    import uvicorn
    
    print("🚀 启动反向天才游戏后端服务器...")
    print("📖 API文档: http://localhost:8000/docs")
    
    uvicorn.run(
        "backend.app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )