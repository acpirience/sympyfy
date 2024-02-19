"""

main sympyfy class

"""
import base64
import json
import os
import sys

from dotenv import dotenv_values
from requests import post

from .sympyfy_urls import HTTP_GET_APP_TOKEN
from .tokens.access_token import Access_token


class Sympyfy:
    # main sympyfy class
    def __init__(self) -> None:
        self._spotify_credentials: dict[str, str]
        self._access_token: Access_token

    def load_credentials(self) -> None:
        self._load_spotify_credentials()
        self._load_access_token()

    def _load_spotify_credentials(self) -> None:
        if "client_id" in os.environ and "client_secret" in os.environ:
            print("Spotify credentials loaded from environment variableS")
            self._spotify_credentials = {
                "client_id": os.environ["client_id"],
                "client_secret": os.environ["client_secret"],
            }
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
        print("Spotify credentials loaded from .env file")
        self._spotify_credentials = {
            "client_id": env_config["client_id"],
            "client_secret": env_config["client_secret"],
        }

    def _load_access_token(self) -> None:
        auth_str = (
            self._spotify_credentials["client_id"]
            + ":"
            + self._spotify_credentials["client_secret"]
        )
        auth_bytes = auth_str.encode("utf-8")
        base64_bytes = base64.b64encode(auth_bytes)
        base64_str = base64_bytes.decode("utf-8")

        headers = {
            "Authorization": "Basic " + base64_str,
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {"grant_type": "client_credentials"}

        response = post(HTTP_GET_APP_TOKEN, headers=headers, data=data)
        response_json = json.loads(response.content)

        self._access_token = Access_token(
            response_json["access_token"], response_json["expires_in"]
        )
