from pydantic.v1 import BaseSettings

class Settings(BaseSettings):
    """
    Settings for the application, loaded from environment variables or a .env file.
    """
    
    # AI Model Provider URLs
    openai_api_url: str
    openrouter_api_url: str
    ollama_api_url: str
    
    # AI Model Provider Keys
    openai_api_key: str
    openrouter_api_key: str
    genai_api_key: str
    hf_token: str
    
    # LLM settings
    provider: str
    model_name: str
    temperature: float
    top_p: float
    max_tokens: int
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# 在程式一開始就讀取所有設定
setting = Settings()