from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    google_api_key: str

    # This inner class tells pydantic-settings to read from a .env file
    model_config = SettingsConfigDict(
        env_file=".env",
    )
