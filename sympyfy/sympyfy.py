"""

main sympyfy class

"""
import os
import sys

from dotenv import dotenv_values


class Sympyfy:
    # main sympyfy class
    def __init__(self) -> None:
        if not os.path.isfile(".env"):
            print("Error: can't find the .env file")
            sys.exit(1)

        _config = dotenv_values(".env")
        if "client_id" not in _config:
            print("Missing client_id variable from .env file")
            sys.exit(1)
        if "client_secret" not in _config:
            print("Missing client_secret variable from .env file")
            sys.exit(1)

        self._spotify_credentials = _config.copy()
        print("Spotify credentials loaded from .env file")
