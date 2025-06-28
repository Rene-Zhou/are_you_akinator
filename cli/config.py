# -*- coding: utf-8 -*-
from pydantic_settings import BaseSettings
from typing import Optional


class CLISettings(BaseSettings):
    # API配置
    api_base_url: str = "http://localhost:8000"
    timeout: int = 30
    
    # 显示配置
    show_debug: bool = False
    max_history_display: int = 10
    
    model_config = {
        "env_file": ".env",
        "case_sensitive": False,
        "env_prefix": "CLI_",
        "extra": "ignore"  # 忽略额外的字段
    }


cli_settings = CLISettings()