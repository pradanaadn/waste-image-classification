from pathlib import Path
from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class KaggleConfig(BaseSettings):
    username: str | None = Field(
        default=None, description="Kaggle username", alias="KAGGLE_USERNAME"
    )
    key: SecretStr | None = Field(
        default=None, description="Kaggle API key", alias="KAGGLE_KEY"
    )
    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.joinpath(".env"),
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


class RoboflowConfig(BaseSettings):
    key: SecretStr | None = Field(
        default=None, description="Roboflow API key", alias="ROBOFLOW_KEY"
    )
    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.joinpath(".env"),
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


class Config(BaseSettings):
    kaggle: KaggleConfig = Field(default_factory=KaggleConfig)
    roboflow: RoboflowConfig = Field(default_factory=RoboflowConfig)

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.joinpath(".env"),
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


config = Config()
