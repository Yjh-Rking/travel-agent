
from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent  # 项目根目录

class Settings(BaseSettings):
    app_name: str = "Travel-Agent智能旅行助手"
    app_version: str = "1.0.0"
    log_level: str = "INFO"

    # 服务器配置
    host: str = "0.0.0.0"
    port: int = 8000

    # CORS配置 - 使用字符串,在代码中分割
    cors_origins: str = "http://localhost:5173,http://127.0.0.1:5173"

    # 高德地图API配置
    amap_api_key: str = ""

    # Unsplash API配置
    unsplash_access_key: str = ""
    unsplash_secret_key: str = ""

    # LLM配置 (从环境变量读取,由HelloAgents管理)
    LLM_MODEL_ID: str = ""
    LLM_BASE_URL: str = ""
    LLM_API_KEY: str = ""

    class Config:
        env_file = str(BASE_DIR / ".env")
        case_sensitive = False
        extra = "ignore"  # 忽略额外的环境变量

    def get_cors_origins_list(self):
        """获取CORS origins列表"""
        return [origin.strip() for origin in self.cors_origins.split(',')]

    # 打印配置信息(用于调试)
    def print_config(self):
        print("Config Info: \n")
        print(f"应用名称: {self.app_name}")
        print(f"版本: {self.app_version}")
        print(f"服务器: {self.host}:{self.port}")
        print(f"高德地图API Key: {'已配置' if self.amap_api_key else '未配置'}")
        print(f"LLM API Key: {'已配置' if self.LLM_API_KEY else '未配置'}")
        print(f"LLM Base URL: {self.LLM_BASE_URL}")
        print(f"LLM Model: { self.LLM_MODEL_ID}")
        print(f"日志级别: {self.log_level}")

    # 验证必要的配置
    def validate_config(self):
        """验证必填配置，返回错误和警告"""
        errors = []
        warnings = []

        # 高德地图
        if not self.amap_api_key:
            errors.append("AMAP_API_KEY未配置")

        # Unsplash
        if not self.unsplash_access_key or not self.unsplash_secret_key:
            warnings.append("Unsplash API Key未配置,图片相关功能可能受限")

        # LLM
        if not self.LLM_API_KEY:
            errors.append("LLM_API_KEY未配置")
        if not self.LLM_BASE_URL:
            errors.append("LLM_BASE_URL未配置")
        if not self.LLM_MODEL_ID:
            errors.append("LLM_MODEL_ID未配置")

        return errors, warnings

# 全局配置实例
settings = Settings()
def get_settings() -> Settings:
    """获取配置实例"""
    return settings
