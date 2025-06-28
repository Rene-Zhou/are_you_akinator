# -*- coding: utf-8 -*-
from prompt_toolkit import prompt, print_formatted_text
from prompt_toolkit.shortcuts import confirm
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.styles import Style
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from typing import List, Dict, Any
import asyncio


class GameUI:
    def __init__(self):
        self.console = Console()
        self.questions_history: List[Dict[str, str]] = []
        
        # 定义样式（用于prompt_toolkit）
        self.style = Style.from_dict({
            'prompt': '#00aa00 bold',
        })
    
    def show_welcome(self):
        """显示欢迎界面"""
        welcome_text = """
🎭 欢迎来到反向天才游戏！

游戏规则：
• AI已经想好了一个知名人物
• 你需要通过提问来猜测这个人物是谁
• AI只能回答：是、否、不知道、或许是、或许不是、你猜对了
• 尽量用最少的问题猜出答案！

游戏方式：
• 直接输入问题进行提问（例如：这个人是男性吗？）
• 想猜测时直接问（例如：是爱因斯坦吗？）
• 输入 'help' 查看帮助，'quit' 退出游戏
• 输入 'history' 查看问答历史
"""
        
        panel = Panel(
            welcome_text.strip(),
            title="🎮 反向天才",
            border_style="blue",
            expand=False
        )
        self.console.print(panel)
    
    def show_game_start(self, message: str):
        """显示游戏开始信息"""
        self.console.print(f"\n✨ {message}\n", style="green bold")
    
    def show_question_answer(self, question: str, answer: str, count: int):
        """显示问答"""
        # 添加到历史记录
        self.questions_history.append({"question": question, "answer": answer})
        
        self.console.print(f"❓ [bold]问题 #{count}:[/bold] {question}")
        self.console.print(f"🤖 [bold blue]AI回答:[/bold blue] {answer}\n")
    
    def show_win_result(self, winning_question: str, session_status: dict = None):
        """显示游戏胜利结果"""
        self.console.print(f"\n🎉 [bold green]恭喜！你猜对了！[/bold green]")
        self.console.print(f"💡 你的猜测：[bold]{winning_question}[/bold]")
        
        if session_status:
            # 从session_status中获取人物信息
            questions_count = session_status.get("questions_count", 0)
            self.console.print(f"📊 总共用了 [bold]{questions_count}[/bold] 个问题")
        
        self.console.print(f"🎯 [bold cyan]游戏结束，感谢游玩！[/bold cyan]\n")
    
    def show_history(self):
        """显示问答历史"""
        if not self.questions_history:
            self.console.print("📝 还没有问答记录", style="blue")
            return
        
        self.console.print("\n📝 问答历史:", style="blue")
        for i, qa in enumerate(self.questions_history, 1):
            self.console.print(f"  {i}. {qa['question']} → {qa['answer']}")
        self.console.print()
    
    def show_help(self):
        """显示帮助信息"""
        help_text = """
🆘 游戏帮助

可用命令：
• 直接输入问题（例如：这个人是男性吗？）
• 直接猜测人物（例如：是爱因斯坦吗？）
• history        - 查看问答历史
• help           - 显示此帮助信息
• quit           - 退出游戏

提问技巧：
• 从大范围开始：性别、年龄、职业、国籍等
• 逐步缩小范围：具体领域、时代、成就等
• 直接猜测：当你觉得知道答案时，直接问"是XXX吗？"
• 注意AI的回答："或许是"/"或许不是"表示不确定
• AI回答"你猜对了"时游戏自动结束
"""
        
        panel = Panel(
            help_text.strip(),
            title="❓ 帮助",
            border_style="yellow",
            expand=False
        )
        self.console.print(panel)
    
    def show_error(self, message: str):
        """显示错误信息"""
        self.console.print(f"❌ 错误：{message}", style="red bold")
    
    def show_warning(self, message: str):
        """显示警告信息"""
        self.console.print(f"⚠️  {message}", style="yellow bold")
    
    def show_info(self, message: str):
        """显示信息"""
        self.console.print(f"ℹ️  {message}", style="blue")
    
    async def get_user_input(self) -> str:
        """获取用户输入"""
        try:
            return await asyncio.get_event_loop().run_in_executor(
                None, 
                lambda: prompt(
                    "🎯 你的问题或命令: "
                )
            )
        except (KeyboardInterrupt, EOFError):
            return "quit"
    
    async def confirm_quit(self) -> bool:
        """确认退出"""
        try:
            return await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: confirm("确定要退出游戏吗？")
            )
        except (KeyboardInterrupt, EOFError):
            return True
    
    def clear_screen(self):
        """清屏"""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_stats(self, questions_count: int):
        """显示游戏统计"""
        self.console.print(f"\n📊 本局游戏统计：共问了 {questions_count} 个问题")
    
    def show_connection_error(self):
        """显示连接错误"""
        error_text = """
🔌 连接服务器失败！

请确保：
1. 后端服务器正在运行
2. 服务器地址配置正确
3. 网络连接正常

启动后端服务器：
cd backend && python -m app.main
"""
        
        panel = Panel(
            error_text.strip(),
            title="❌ 连接错误",
            border_style="red",
            expand=False
        )
        self.console.print(panel)