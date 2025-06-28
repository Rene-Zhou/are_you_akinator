# -*- coding: utf-8 -*-
from openai import OpenAI
from typing import List
from ..config.settings import settings
from ..models.person import PersonInfo


class AIService:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.openai_api_key, 
            base_url=settings.openai_base_url
        )
        self.model = settings.model_name
        
        # AI回答的允许选项
        self.allowed_answers = ["是", "否", "不知道", "或许是", "或许不是", "你猜对了"]
    
    def get_system_prompt(self, person_info: PersonInfo) -> str:
        """生成系统提示词"""
        return f"""你是一个反向Akinator游戏的AI。你已经选择了一个网络知名人物：{person_info.name}

关于这个人物的信息：
姓名：{person_info.name}
简介：{person_info.summary}
出生日期：{person_info.birth_date or "未知"}
国籍：{person_info.nationality or "未知"}
职业：{", ".join(person_info.occupation) if person_info.occupation else "未知"}
著名事迹：{", ".join(person_info.known_for) if person_info.known_for else "未知"}
类别：{", ".join(person_info.categories[:5]) if person_info.categories else "未知"}

游戏规则：
1. 用户会问你关于这个人物的问题
2. 你只能回答以下6种答案之一：
   - "是" - 确定答案为是
   - "否" - 确定答案为否  
   - "不知道" - 不确定或信息不足
   - "或许是" - 可能是，但不确定
   - "或许不是" - 可能不是，但不确定
   - "你猜对了" - 用户猜中了人物

3. 基于提供的人物信息准确回答
4. 如果用户直接猜测人物姓名且正确，回答"你猜对了"
5. 严格按照以上6种回答格式，不要添加任何额外解释或信息
6. 即使用户询问游戏规则或要求提示，也只能用这6种回答之一回应"""
    
    def answer_question(self, question: str, person_info: PersonInfo, conversation_history: List[dict] = None) -> str:
        """回答用户问题"""
        try:
            messages = [
                {"role": "system", "content": self.get_system_prompt(person_info)}
            ]
            
            # 添加对话历史
            if conversation_history:
                messages.extend(conversation_history)
            
            # 添加当前问题
            messages.append({"role": "user", "content": question})
            
            print(f"🤖 调用AI服务，问题: {question}")
            print(f"🤖 使用模型: {self.model}")
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=10,  # 限制回答长度
                temperature=0.3,  # 降低随机性
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            
            answer = response.choices[0].message.content.strip()
            print(f"🤖 AI原始回答: {answer}")
            
            # 确保回答在允许范围内
            if answer not in self.allowed_answers:
                # 如果回答不在允许范围内，尝试映射到最相近的答案
                mapped_answer = self._map_to_allowed_answer(answer)
                print(f"🤖 映射后回答: {mapped_answer}")
                answer = mapped_answer
            
            return answer
            
        except Exception as e:
            print(f"❌ AI服务错误: {e}")
            print(f"❌ 错误类型: {type(e)}")
            import traceback
            traceback.print_exc()
            return "不知道"
    
    def check_guess(self, guess: str, person_info: PersonInfo) -> bool:
        """检查用户猜测是否正确"""
        guess_lower = guess.lower().strip()
        person_name_lower = person_info.name.lower().strip()
        
        # 完全匹配
        if guess_lower == person_name_lower:
            return True
        
        # 部分匹配（处理姓名的不同表达方式）
        if guess_lower in person_name_lower or person_name_lower in guess_lower:
            # 使用AI判断是否为正确猜测
            try:
                prompt = f"用户猜测：'{guess}'\n正确答案：'{person_info.name}'\n这个猜测是否正确？只回答'是'或'否'"
                
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=5,
                    temperature=0.1
                )
                
                ai_judgment = response.choices[0].message.content.strip()
                return ai_judgment == "是"
                
            except Exception:
                # 如果AI判断失败，使用简单的字符串匹配
                return len(set(guess_lower.split()) & set(person_name_lower.split())) > 0
        
        return False
    
    def _map_to_allowed_answer(self, answer: str) -> str:
        """将AI回答映射到允许的答案格式"""
        answer_lower = answer.lower()
        
        # 映射规则
        if any(word in answer_lower for word in ["yes", "correct", "right", "对", "正确"]):
            return "是"
        elif any(word in answer_lower for word in ["no", "wrong", "incorrect", "不对", "错误"]):
            return "否"
        elif any(word in answer_lower for word in ["maybe", "perhaps", "possibly", "可能是", "或许是"]):
            return "或许是"
        elif any(word in answer_lower for word in ["maybe not", "probably not", "可能不是", "或许不是"]):
            return "或许不是"
        elif any(word in answer_lower for word in ["don't know", "unknown", "unsure", "不确定", "不清楚"]):
            return "不知道"
        elif any(word in answer_lower for word in ["guessed", "correct guess", "you got it", "猜对了", "答对了"]):
            return "你猜对了"
        else:
            return "不知道"  # 默认回答


# 全局实例
ai_service = AIService()