# -*- coding: utf-8 -*-
import asyncio
import sys
from cli.main import main as cli_main


def show_menu():
    """显示主菜单"""
    print("🎭 反向天才 (Reverse Akinator)")
    print("=" * 40)
    print("1. 启动游戏 (CLI)")
    print("2. 启动后端服务器")
    print("3. 退出")
    print("=" * 40)


async def main():
    """主函数"""
    while True:
        show_menu()
        choice = input("请选择 (1-3): ").strip()
        
        if choice == "1":
            print("\n🎮 启动CLI游戏...")
            await cli_main()
        elif choice == "2":
            print("\n🚀 启动后端服务器...")
            import subprocess
            subprocess.run([sys.executable, "run_backend.py"])
        elif choice == "3":
            print("\n👋 再见！")
            break
        else:
            print("\n❌ 无效选择，请重试")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 再见！")
        sys.exit(0)