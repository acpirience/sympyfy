"""

Access_token: used for api call not needing oauth

"""

import base64
import json
import os
import sys
from datetime import datetime, timedelta
from enum import Enum

from dotenv import dotenv_values
from requests import post
from rich.console import Console

from sympyfy.api_urls import HTTP_GET_APP_TOKEN
from sympyfy.consts import STYLE

console = Console()

ACCESS_TOKEN_FILE = ".access_token"


class Auth_type(Enum):
    """
    Authentication type:<br>
        - APP: authentication via client_id / client_secret with access only to app APIs. See [https://developer.spotify.com/documentation/web-api/concepts/access-token](https://developer.spotify.com/documentation/web-api/concepts/access-token)<br>
        - USER: authentication via Oauth2 Authorization code flow. See [https://developer.spotify.com/documentation/web-api/tutorials/code-flow](https://developer.spotify.com/documentation/web-api/tutorials/code-flow)
    """

    APP = "APP"
    USER = "USER"


SCOPES = {
    "ugc-image-upload",
    "user-read-playback-state",
    "user-modify-playback-state",
    "user-read-currently-playing",
    "app-remote-control",
    "streaming",
    "playlist-read-private",
    "playlist-read-collaborative",
    "playlist-modify-private",
    "playlist-modify-public",
    "user-follow-modify",
    "user-follow-read",
    "user-read-playback-position",
    "user-top-read",
    "user-read-recently-played",
    "user-library-modify",
    "user-library-read",
    "user-read-email",
    "user-read-private",
    "user-soa-link",
    "user-soa-unlink",
    "user-manage-entitlements",
    "user-manage-partner",
    "user-create-partner",
}


class Access_token:
    def __init__(self, client_id: str = "", client_secret: str = "") -> None:
        #     # Token: token content passed to the API
        #     # expiry: datetime when the token becomes invalid
        self._client_id: str = client_id
        self._client_secret: str = client_secret
        self._token: str = ""
        self._token_type: Auth_type = Auth_type.APP
        self._scope: list[str] = []
        self._expiry: datetime = datetime.today()
        self._refresh_token: str = ""

    def load_spotify_credentials(self) -> None:
        if self._client_id != "" and self._client_secret != "":
            console.print("Spotify credentials loaded from method parameters", style=STYLE["INFO"])
            return

        if "client_id" in os.environ and "client_secret" in os.environ:
            console.print(
                "Spotify credentials loaded from environment variables", style=STYLE["INFO"]
            )
            self._client_id = os.environ["client_id"]
            self._client_secret = os.environ["client_secret"]
            return

        if not os.path.isfile(".env"):
            console.print(
                "Error: can't find client_id / client_secret environment variables or an .env file",
                style=STYLE["CRITICAL"],
            )
            sys.exit(1)
        env_config = dotenv_values(".env")
        if "client_id" not in env_config:
            console.print(
                "Error: Missing client_id variable from .env file", style=STYLE["CRITICAL"]
            )
            sys.exit(1)
        if "client_secret" not in env_config:
            console.print(
                "Error: Missing client_secret variable from .env file", style=STYLE["CRITICAL"]
            )
            sys.exit(1)
        console.print("Spotify credentials loaded from .env file", style=STYLE["INFO"])
        self._client_id = env_config["client_id"]
        self._client_secret = env_config["client_secret"]

    def load_access_token(self, auth_type: Auth_type=Auth_type.APP, scope: list[str] | None = None) -> None:
        # check for previously saved token on filesystem
        if os.path.isfile(ACCESS_TOKEN_FILE):
            self.make_access_token(self.load_token_from_file(), auth_type, scope)
            if self.is_valid():
                return
            console.print("Cache is expired", style=STYLE["NOTICE"])

        self.make_access_token(self.load_token_from_api(auth_type, scope), auth_type, scope)

    def load_token_from_file(self) -> bytes:
        console.print("Loading Access Token from cache", style=STYLE["INFO"])
        with open(ACCESS_TOKEN_FILE, "rb") as token_file:
            token_json = token_file.read()
        return token_json

    def load_token_from_api(self, auth_type: Auth_type, scope: list[str] | None) -> bytes:
        if auth_type == Auth_type.USER and not scope:
            console.print(
                "Error: Scope is mandatory for a USER authentication",
                style=STYLE["CRITICAL"],
            )
            sys.exit(1)

        self._token_type = auth_type
        self._scope = scope if scope else []
        console.print(
            f"Loading Access Token from Spotify {auth_type.value} API", style=STYLE["INFO"]
        )
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
                f"Error: can't get access token ([{response.status_code}] {response.reason}",
                style=STYLE["CRITICAL"],
            )
            sys.exit(1)

    def make_access_token(self, json_content: bytes, auth_type: Auth_type, scope: list[str] | None = None) -> None:
        save_json = self.json_token_decode(json_content, auth_type, scope)
        with open(ACCESS_TOKEN_FILE, "wb") as token_file:
            token_file.write(save_json.encode("utf-8"))

    def json_token_decode(self, json_content: bytes, auth_type: Auth_type, scope: list[str] | None = None) -> str:
        response_dict = json.loads(json_content)
        self._scope = scope
        self._token = response_dict["access_token"]

        if "refresh_token" in response_dict:
            self._refresh_token = response_dict["refresh_token"]

        if "token_type" in response_dict:
            if response_dict["token_type"] == "Bearer":
                self._token_type = auth_type
            else:
                match response_dict["token_type"]:
                    case "APP":
                        self._token_type = auth_type.APP
                    case "USER":
                        self._token_type = auth_type.USER
                if "scope" in response_dict:
                    self._scope = response_dict["scope"].split(",")

        if "expire_date" in response_dict: # From File
            self._expiry = datetime.fromisoformat(response_dict["expire_date"])
        else:
            self._expiry = datetime.today() + timedelta(seconds=response_dict["expires_in"])
        console.print(
            f"Access Token loaded, valid until {self.expiry}",
            style=STYLE["INFO"],
        )

        save_dict = {"access_token": self._token, "expire_date": self._expiry.isoformat(), "token_type": self._token_type.name, "scope": ",".join(self._scope) if self._scope else "", "refresh_token": self._refresh_token}
        return json.dumps(save_dict)


    @property
    def token(self) -> str:
        return self._token

    @property
    def expiry(self) -> datetime:
        return self._expiry

    @property
    def headers(self) -> dict[str, str]:
        if not self.is_valid():
            console.print("Access token has expired", style=STYLE["NOTICE"])
            self.load_token_from_api(self._token_type, self._scope)
        return {"Authorization": "Bearer " + self.token}

    def is_valid(self) -> bool:
        # token is invalid if current date + 30 seconds> expiry
        return datetime.today() + timedelta(seconds=30) < self.expiry

    def __repr__(self) -> str:
        return f"(Token:'{self.token}', Expiry:'{self.expiry}')"

