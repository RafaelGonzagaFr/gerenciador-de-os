from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )

    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ENV: str = "development"  # Novo campo

    @property
    def token_url(self) -> str:
        if self.ENV == "production":
            return ""
        return "/token/"


settings = Settings()
