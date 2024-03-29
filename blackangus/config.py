import pathlib
import sys
from typing import List, Dict

import toml
from pydantic import BaseModel, Field


class DiscordConfig(BaseModel):
    client_id: str
    client_secret: str
    public_key: str
    token: str


class BotConfig(BaseModel):
    app_list: List[str] = Field(default_factory=list)
    prefix: str = Field(default='!')
    emoticon_prefix: str = Field(default='~')
    log_when_ready: bool = Field(default=False)
    log_channel: str


class PapagoConfig(BaseModel):
    client_id: str
    client_secret: str


class GoogleConfig(BaseModel):
    api_key: str


class WeatherConfig(BaseModel):
    api_key: str


class DatabaseConfig(BaseModel):
    url: str
    database_name: str


class EmoticonConfig(BaseModel):
    s3_bucket: str
    s3_access_key: str
    s3_secret_key: str
    s3_region: str
    api_endpoint: Dict[str, str]


class Config(BaseModel):
    discord: DiscordConfig
    bot: BotConfig
    mongodb: DatabaseConfig
    papago: PapagoConfig
    google: GoogleConfig
    weather: WeatherConfig
    emoticon: EmoticonConfig


def panic(message: str, *args):
    print(message.format(*args), file=sys.stderr)
    raise SystemExit(1)


def load(path: pathlib.Path) -> Config:
    """지정한 Path에서 toml 파일을 serialize합니다."""
    if not path.exists() or not path.is_file() or not path.match('*.toml'):
        panic('지정한 경로에 파일이 없거나, 파일이 아니거나, toml 파일이 아닙니다.')

    try:
        return Config.parse_obj(toml.loads(path.read_text()))
    except TypeError as e:
        panic(str(e))
        raise
