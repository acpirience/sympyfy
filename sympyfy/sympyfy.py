"""

main sympyfy class

"""
import base64
import json
import os
import sys

from dotenv import dotenv_values
from requests import Response, get, post

from sympyfy.api.api_urls import (
    HTTP_GET_APP_TOKEN,
    HTTP_GET_ARTIST,
    HTTP_GET_RELATED_ARTISTS,
    HTTP_GET_SEVERAL_ARTISTS,
)
from sympyfy.api.artists import Artist, make_artist, make_artists_list
from sympyfy.tokens.access_token import Access_token


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
        # get access token used when user identification is not needed
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
        print(f"Access Token received, valid until {self._access_token.expiry}")

    def _get_api_response_with_access_token(self, url: str) -> Response:
        # Generic function that returns the json response
        # of an API call using access token
        headers = {"Authorization": "Bearer " + self._access_token.token}
        response = get(url, headers=headers)
        return response

    def get_artist(self, id: str) -> Artist | None:
        """returns an Artist Object specified by its id
        https://developer.spotify.com/documentation/web-api/reference/get-an-artist

        :param id: Spotify id of the artist
        :type id: str
        :returns:  Artist object or None if id does not match an artist
        """
        url = HTTP_GET_ARTIST.replace("{id}", id)
        response = self._get_api_response_with_access_token(url)
        if response.status_code == 200:
            return make_artist(response.content)
        return None

    def get_several_artists(self, ids: list[str]) -> list[Artist]:
        """returns a list of Artist Objects specified by a list of their ids
        https://developer.spotify.com/documentation/web-api/reference/get-multiple-artists

        :param ids: list of artists ids
        :type ids: list[str]
        :returns:  list of Artist objects
        """
        url = HTTP_GET_SEVERAL_ARTISTS.replace("{ids}", "%2C".join(ids))
        response = self._get_api_response_with_access_token(url)
        return make_artists_list(response.content)

    def get_artist_related_artists(self, id: str) -> list[Artist] | None:
        """returns a list of Artist Objects related to the artist specified by its id
        https://developer.spotify.com/documentation/web-api/reference/get-an-artists-related-artists

        :param id: Spotify id of the artist
        :type id: str
        :returns:  list of Artist objects
        """
        url = HTTP_GET_RELATED_ARTISTS.replace("{id}", id)
        response = self._get_api_response_with_access_token(url)
        if response.status_code == 200:
            return make_artists_list(response.content)
        return None
