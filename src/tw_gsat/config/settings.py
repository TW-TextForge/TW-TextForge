from pydantic.v1 import BaseSettings

class Settings(BaseSettings):
    """
    Settings for the application, loaded from environment variables or a .env file.
    """
    
    # AI Model Provider URLs
    openai_api_url: str
    openrouter_api_url: str
    ollama_api_url: str
    ollama_embed_api_url: str
    
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
    
    # Embedding settings
    embedding_model: str
    embedding_provider: str
    
    # Qdrant settings
    qdrant_url: str
    chunk_size: int = 8194
    chunk_overlap: int = 50
    vector_size: int = 1024
    distance: str = "Cosine"
    collection_name: str = "code_collection"
    
    
    # Other URLs
    searxng_url: str
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# 在程式一開始就讀取所有設定
setting = Settings()