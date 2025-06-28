# -*- coding: utf-8 -*-
import wikipedia
import random
from typing import Dict, List, Optional
from ..models.person import PersonInfo
from ..config.settings import settings


class WikipediaService:
    def __init__(self):
        wikipedia.set_lang(settings.wikipedia_language)
        self._cache: Dict[str, PersonInfo] = {}
        self.famous_people = self._load_famous_people()
    
    def _load_famous_people(self) -> List[str]:
        """从文件中加载知名人物列表"""
        import os
        
        # 获取项目根目录
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
        famous_people_file = os.path.join(project_root, "famous_people.txt")
        
        people = []
        try:
            with open(famous_people_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    # 跳过空行和注释行
                    if line and not line.startswith('#'):
                        people.append(line)
            
            print(f"📚 从文件加载了 {len(people)} 个知名人物")
            return people
            
        except FileNotFoundError:
            print(f"⚠️  未找到人物文件 {famous_people_file}，使用默认列表")
            # 备用默认列表
            return [
                "Albert Einstein", "Steve Jobs", "Bill Gates", "Elon Musk",
                "Barack Obama", "Donald Trump", "Leonardo da Vinci", "Pablo Picasso",
                "Michael Jackson", "Elvis Presley", "Taylor Swift", "Tom Hanks",
                "Stephen Hawking", "Marie Curie", "Isaac Newton", "Shakespeare",
                "Michael Jordan", "Lionel Messi", "Cristiano Ronaldo",
                "Warren Buffett", "Jeff Bezos", "Mark Zuckerberg"
            ]
        except Exception as e:
            print(f"❌ 加载人物文件时出错: {e}")
            return ["Albert Einstein", "Steve Jobs", "Bill Gates"]  # 最小备用列表
    
    def get_random_person(self) -> str:
        """随机选择一个知名人物"""
        selected_person = random.choice(self.famous_people)
        print(f"🎯 随机选择了人物: {selected_person}")
        return selected_person
    
    def get_people_count(self) -> int:
        """获取人物列表总数"""
        return len(self.famous_people)
    
    def get_people_list(self) -> List[str]:
        """获取人物列表"""
        return self.famous_people.copy()
    
    def get_person_info(self, person_name: str) -> Optional[PersonInfo]:
        """获取人物信息，支持缓存"""
        if person_name in self._cache:
            return self._cache[person_name]
        
        try:
            # 搜索人物页面
            search_results = wikipedia.search(person_name, results=3)
            if not search_results:
                return None
            
            # 尝试获取最匹配的页面
            page = None
            for result in search_results:
                try:
                    page = wikipedia.page(result)
                    break
                except wikipedia.exceptions.DisambiguationError as e:
                    # 如果有歧义，选择最可能的选项
                    try:
                        page = wikipedia.page(e.options[0])
                        break
                    except:
                        continue
                except:
                    continue
            
            if not page:
                return None
            
            # 提取关键信息
            person_info = self._extract_person_info(page)
            
            # 缓存结果
            self._cache[person_name] = person_info
            
            return person_info
            
        except Exception as e:
            print(f"Error fetching info for {person_name}: {e}")
            return None
    
    def _extract_person_info(self, page) -> PersonInfo:
        """从Wikipedia页面提取人物信息"""
        content = page.content
        summary = page.summary
        
        # 提取基本信息
        categories = page.categories if hasattr(page, 'categories') else []
        
        # 简单的信息提取（可以进一步优化）
        occupation = self._extract_occupation(content, categories)
        nationality = self._extract_nationality(content)
        birth_date = self._extract_birth_date(content)
        known_for = self._extract_known_for(content, categories)
        
        return PersonInfo(
            name=page.title,
            summary=summary[:500] + "..." if len(summary) > 500 else summary,
            birth_date=birth_date,
            nationality=nationality,
            occupation=occupation,
            known_for=known_for,
            categories=[cat for cat in categories[:10]],  # 限制类别数量
            additional_info={}
        )
    
    def _extract_occupation(self, content: str, categories: List[str]) -> List[str]:
        """提取职业信息"""
        occupations = []
        
        # 从类别中提取职业
        occupation_keywords = [
            "actor", "actress", "singer", "musician", "writer", "author",
            "politician", "scientist", "entrepreneur", "director", "producer",
            "artist", "painter", "athlete", "footballer", "basketball",
            "tennis", "business", "CEO", "founder", "inventor", "physicist",
            "mathematician", "philosopher", "composer", "chef"
        ]
        
        content_lower = content.lower()
        for keyword in occupation_keywords:
            if keyword in content_lower:
                occupations.append(keyword.title())
        
        # 从类别中提取
        for category in categories:
            for keyword in occupation_keywords:
                if keyword in category.lower():
                    occupations.append(keyword.title())
        
        return list(set(occupations))[:5]  # 去重并限制数量
    
    def _extract_nationality(self, content: str) -> Optional[str]:
        """提取国籍信息"""
        # 简单的国籍提取
        countries = [
            "American", "British", "Chinese", "Japanese", "German", "French",
            "Italian", "Spanish", "Russian", "Indian", "Brazilian", "Canadian",
            "Australian", "South Korean", "Mexican", "Argentine", "Dutch",
            "Swedish", "Norwegian", "Danish", "Swiss", "Austrian", "Belgian"
        ]
        
        for country in countries:
            if country.lower() in content.lower():
                return country
        
        return None
    
    def _extract_birth_date(self, content: str) -> Optional[str]:
        """提取出生日期（简单实现）"""
        import re
        
        # 寻找出生日期模式
        birth_patterns = [
            r"born (\w+ \d+, \d{4})",
            r"born (\d{4})",
            r"\(born (\w+ \d+, \d{4})\)",
            r"\(born (\d{4})\)"
        ]
        
        for pattern in birth_patterns:
            match = re.search(pattern, content)
            if match:
                return match.group(1)
        
        return None
    
    def _extract_known_for(self, content: str, categories: List[str]) -> List[str]:
        """提取著名事迹"""
        known_for = []
        
        # 从内容中提取关键词
        keywords = [
            "Nobel Prize", "Academy Award", "Grammy", "Emmy", "Tony Award",
            "Olympic", "World Cup", "Super Bowl", "NBA", "FIFA",
            "bestseller", "blockbuster", "hit song", "chart-topping",
            "revolutionary", "groundbreaking", "pioneering", "innovative"
        ]
        
        content_lower = content.lower()
        for keyword in keywords:
            if keyword.lower() in content_lower:
                known_for.append(keyword)
        
        return known_for[:5]  # 限制数量


# 全局实例
wikipedia_service = WikipediaService()