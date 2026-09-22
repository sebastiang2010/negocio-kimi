import asyncio
import os
import sys

import yaml


def load_config(path):
    with open(path, "r", encoding="utf-8") as fh:
        config = yaml.safe_load(fh)
    env_token = os.environ.get("BOT_TOKEN")
    if env_token:
        config["bot_token"] = env_token
    return config


async def main():
    config_path = os.environ.get("BOT_CONFIG", "config.yaml")
    config = load_config(config_path)
    from src.bot import BotApp

    await BotApp(config).run_polling()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    finally:
        sys.exit(0)