from dotenv import dotenv_values
from loguru import logger


def main() -> None:
    config = dotenv_values(".env")
    logger.info(config)


if __name__ == "__main__":
    main()
