from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "GRA Drone Officer"
    max_drones: int = 50

settings = Settings()
