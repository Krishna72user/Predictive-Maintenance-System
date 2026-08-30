from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application
    app_name: str = "Predictive Maintenance API"
    environment: str = "production"

    dagshub_uri:str
    version:str = "latest"
    model_name:str

    model_path:str
    # Database
    database_url: str

    secret:str

    algorithm: str
    # Redis
    # redis_url: str


    # API
    api_v1_prefix: str = "/api/v1"

    model_config = SettingsConfigDict( # Special Atrribute model_config dont rename it(Pydantic cant recognise)
        env_file=".env",
        extra="ignore"
    )


settings = Settings()