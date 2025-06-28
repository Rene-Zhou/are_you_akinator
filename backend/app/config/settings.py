# -*- coding: utf-8 -*-
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # LLM配置
    llm_provider: str = "openai"
    openai_api_key: str
    openai_base_url: str = "https://api.openai.com/v1"
    model_name: str = "gpt-4o-mini"
    
    # 应用配置
    debug: bool = True
    log_level: str = "INFO"
    port: int = 8000
    
    # Wikipedia配置
    wikipedia_language: str = "en"
    cache_duration: int = 3600
    
    model_config = {
        "env_file": ".env",
        "case_sensitive": False,
        "extra": "ignore"  # 忽略额外的字段
    }


settings = Settings()