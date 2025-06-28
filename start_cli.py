# -*- coding: utf-8 -*-
"""启动CLI客户端的脚本"""
import sys
import os
import asyncio

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    from cli.main import main as cli_main
    
    try:
        asyncio.run(cli_main())
    except KeyboardInterrupt:
        print("\n👋 再见！")
        sys.exit(0)