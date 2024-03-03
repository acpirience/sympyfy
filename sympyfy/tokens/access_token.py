"""

Access_token: used for api call not needing oauth

"""

import base64
import json
import os
import sys
from datetime import datetime, timedelta

from dotenv import dotenv_values
from requests import post
from rich.console import Console

from sympyfy.api_urls import HTTP_GET_APP_TOKEN

console = Console()

ACCESS_TOKEN_FILE = ".access_token"


class Access_token:
    def __init__(self, client_id: str = "", client_secret: str = "") -> None:
        #     # Token: token content passed to the API
        #     # expiry: datetime when the token becomes invalid
        self._client_id: str = client_id
        self._client_secret: str = client_secret
        self._token: str = ""
        self._expiry: datetime = datetime.today()

    def load_spotify_credentials(self) -> None:
        if self._client_id != "" and self._client_secret != "":
            console.print(
                "Spotify credentials loaded from method parameters", style="light_slate_blue"
            )
            return

        if "client_id" in os.environ and "client_secret" in os.environ:
            console.print(
                "Spotify credentials loaded from environment variables", style="light_slate_blue"
            )
            self._client_id = os.environ["client_id"]
            self._client_secret = os.environ["client_secret"]
            return

        if not os.path.isfile(".env"):
            console.print(
                "Error: can't find client_id / client_secret environment variableS or an .env file",
                style="red on white",
            )
            sys.exit(1)
        env_config = dotenv_values(".env")
        if "client_id" not in env_config:
            console.print("Error: Missing client_id variable from .env file", style="red on white")
            sys.exit(1)
        if "client_secret" not in env_config:
            console.print(
                "Error: Missing client_secret variable from .env file", style="red one white"
            )
            sys.exit(1)
        console.print("Spotify credentials loaded from .env file", style="light_slate_blue")
        self._client_id = env_config["client_id"]
        self._client_secret = env_config["client_secret"]

    def load_access_token(self) -> None:
        # check for previously saved token on filesystem
        if os.path.isfile(ACCESS_TOKEN_FILE):
            console.print("Loading from cache", style="light_slate_blue")
            self.make_access_token(self.load_token_from_file())
            if self.is_valid():
                return
            console.print("Cache is expired", style="orange1")

        console.print("Loading from Spotify API", style="light_slate_blue")
        self.make_access_token(self.load_token_from_api())

    def load_token_from_file(self) -> bytes:
        with open(ACCESS_TOKEN_FILE, "rb") as token_file:
            token_json = token_file.read()
        return token_json

    def load_token_from_api(self) -> bytes:
        auth_str = self._client_id + ":" + self._client_secret
        auth_bytes = auth_str.encode("utf-8")
        base64_bytes = base64.b64encode(auth_bytes)
        base64_str = base64_bytes.decode("utf-8")

        headers = {
            "Authorization": "Basic " + base64_str,
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {"grant_type": "client_credentials"}

        response = post(HTTP_GET_APP_TOKEN, headers=headers, data=data)
        if response.status_code == 200:
            return response.content
        else:
            console.print(
                f"Error: can't get access token ([{response.status_code}] {response.reason})",
                style="red on white",
            )
            sys.exit(1)

    def make_access_token(self, json_content: bytes):
        response_json = json.loads(json_content)
        self._token = response_json["access_token"]
        if "expires_in" in response_json:
            self._expiry = datetime.today() + timedelta(seconds=response_json["expires_in"])
        else:
            self._expiry = datetime.fromisoformat(response_json["expire_date"])
        console.print(
            f"Access Token loaded, valid until {self.expiry}",
            style="light_slate_blue",
        )

        save_dict = {"access_token": self._token, "expire_date": self._expiry.isoformat()}
        save_json = json.dumps(save_dict)

        with open(ACCESS_TOKEN_FILE, "wb") as token_file:
            token_file.write(save_json.encode("utf-8"))

    @property
    def token(self) -> str:
        return self._token

    @property
    def expiry(self) -> datetime:
        return self._expiry

    @property
    def headers(self) -> dict[str, str]:
        return {"Authorization": "Bearer " + self.token}

    def is_valid(self) -> bool:
        # token is invalid if current date + 30 seconds> expiry
        return datetime.today() + timedelta(seconds=30) < self.expiry

    def __repr__(self) -> str:
        return f"(Token:'{self.token}', Expiry:'{self.expiry}')"
