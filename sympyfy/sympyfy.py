"""

main sympyfy class

"""
import os
import sys

from dotenv import dotenv_values


class Sympyfy:
    # main sympyfy class
    def __init__(self) -> None:
        self._spotify_credentials: dict[str, str]
        self._get_spotify_credentials()

    def _get_spotify_credentials(self) -> None:
        if "client_id" in os.environ and "client_secret" in os.environ:
            self._spotify_credentials = {
                "client_id": os.environ["client_id"],
                "client_secret": os.environ["client_secret"],
            }
            print("Spotify credentials loaded from environment variableS")
            return

        if not os.path.isfile(".env"):
            print(
                "Error: can't find client_id / client_secret environment variableS or an .env file"
            )
            sys.exit(1)
        env_config = dotenv_values(".env")
        if "client_id" not in env_config:
            print("Missing client_id variable from .env file")
            sys.exit(1)
        if "client_secret" not in env_config:
            print("Missing client_secret variable from .env file")
            sys.exit(1)
        self._spotify_credentials = env_config.copy()
        print("Spotify credentials loaded from .env file")
