from dataclasses import dataclass

from environs import Env


# @dataclass
# class DbConfig:
#     host: str
#     password: str
#     user: str
#     name: str
#     port: str


@dataclass
class Redis:
    use_redis: bool
    host: str
    port: str
    password: str | None


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


@dataclass
class Miscellaneous:
    other_params: str = None


@dataclass
class Config:
    tg_bot: TgBot
    redis: Redis
    # db: DbConfig
    misc: Miscellaneous


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS"))),
        ),
        redis=Redis(
            host=env.str("REDIS_HOST"),
            port=env.str("REDIS_PORT"),
            password=env.str("REDIS_PASSWORD"),
            use_redis=env.bool("USE_REDIS", 'False')
        ),
        # db=DbConfig(
        #     host=env.str('POSTGRES_HOST'),
        #     password=env.str('POSTGRES_PASSWORD'),
        #     user=env.str('POSTGRES_USER'),
        #     name=env.str('POSTGRES_DB'),
        #     port=env.str('POSTGRES_PORT')
        # ),
        misc=Miscellaneous()
    )
