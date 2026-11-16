from pydantic import Field, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Automatically looks for an ENV variable named 'APP_ENV'
    app_env: str = "development"  # Default value if not found
    
    # Advanced type validation worked seamlessly
    api_timeout: int = 30

    port: int = 5000
    redis_port: int = 6379
    debug: bool = True

    jwt_token: str
    jwt_seconds: int = 86400 # preserve token for one day

    
    # Use SettingsConfigDict to define global settings behaviors
    model_config = SettingsConfigDict(
        env_file=".env",              # Read from a local .env file
        env_file_encoding="utf-8",    # Encoding for the file
        env_prefix="APP_",            # Forces fields to match APP_APP_ENV, APP_DATABASE_URL etc.
        case_sensitive=False,         # Case insensitivity configuration
        extra="ignore"
    )

# Instantiate settings
settings = Settings()
