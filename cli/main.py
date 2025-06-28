# -*- coding: utf-8 -*-
import asyncio
import sys
from .client import APIClient
from .ui import GameUI


class ReverseAkinatorCLI:
    def __init__(self):
        self.client = APIClient()
        self.ui = GameUI()
        self.game_active = False
    
    async def run(self):
        """运行CLI应用"""
        self.ui.show_welcome()
        
        # 检查服务器连接
        if not await self.client.check_health():
            self.ui.show_connection_error()
            return
        
        # 开始游戏
        try:
            await self.start_game()
            await self.game_loop()
        except KeyboardInterrupt:
            self.ui.show_info("游戏被用户中断")
        except Exception as e:
            self.ui.show_error(f"游戏出现异常: {e}")
        finally:
            if self.game_active:
                await self.end_game()
    
    async def start_game(self):
        """开始游戏"""
        try:
            result = await self.client.start_game()
            self.ui.show_game_start(result.get("message", "游戏开始！"))
            self.game_active = True
        except Exception as e:
            self.ui.show_error(f"无法开始游戏: {e}")
            raise
    
    async def game_loop(self):
        """游戏主循环"""
        question_count = 0
        
        while self.game_active:
            try:
                user_input = await self.ui.get_user_input()
                
                if not user_input.strip():
                    continue
                
                # 处理命令
                if user_input.lower() == "quit":
                    self.ui.show_info("感谢游玩，再见！")
                    break
                
                elif user_input.lower() == "help":
                    self.ui.show_help()
                    continue
                
                elif user_input.lower() == "history":
                    self.ui.show_history()
                    continue
                
                else:
                    # 处理普通问题
                    result = await self.handle_question(user_input)
                    question_count += 1
                    
                    # 检查是否猜对了
                    if result and result.get("answer") == "你猜对了":
                        await self.handle_win(user_input)
                        break
            
            except Exception as e:
                self.ui.show_error(f"处理输入时出错: {e}")
        
        if question_count > 0:
            self.ui.show_stats(question_count)
    
    async def handle_question(self, question: str):
        """处理用户问题"""
        try:
            result = await self.client.ask_question(question)
            self.ui.show_question_answer(
                question,
                result.get("answer", ""),
                result.get("questions_count", 0)
            )
            return result
        except Exception as e:
            self.ui.show_error(f"提问失败: {e}")
            return None
    
    async def handle_win(self, winning_question: str):
        """处理游戏胜利"""
        try:
            # 获取游戏状态以确认胜利和获取答案
            session_status = await self.client.get_game_status()
            self.ui.show_win_result(winning_question, session_status)
            self.game_active = False
        except Exception as e:
            self.ui.show_error(f"获取胜利信息失败: {e}")
            # 即使获取状态失败，也显示基本的胜利信息
            self.ui.show_win_result(winning_question, None)
            self.game_active = False
    
    async def end_game(self):
        """结束游戏"""
        try:
            if self.client.session_id:
                await self.client.end_game()
            self.ui.show_info("感谢游玩！")
        except Exception as e:
            self.ui.show_error(f"结束游戏时出错: {e}")


async def main():
    """主函数"""
    cli = ReverseAkinatorCLI()
    await cli.run()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 再见！")
        sys.exit(0)