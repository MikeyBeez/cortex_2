"""Cortex configuration"""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Cortex_2"
    version: str = "0.1.0"
    debug: bool = True
    
    # API settings
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    
    # Storage paths
    storage_path: str = "/Users/bard/Code/cortex_2/storage"
    module_path: str = "/Users/bard/Code/cortex_2/modules"
    
    # Memory limits
    memory_limit_tokens: int = 100000
    memory_buffer_tokens: int = 5000
    
    class Config:
        env_prefix = "CORTEX_"

settings = Settings()
