"""

main sympyfy class

"""
import base64
import json
import os
import sys
from dataclasses import dataclass
from typing import Any, Optional

from dotenv import dotenv_values
from requests import Response, get, post

from api_urls import (
    HTTP_GET_ALBUM,
    HTTP_GET_APP_TOKEN,
    HTTP_GET_ARTIST,
    HTTP_GET_RELATED_ARTISTS,
    HTTP_GET_SEVERAL_ARTISTS,
    HTTP_GET_TRACK,
)
from sympyfy.common import Image
from sympyfy.tokens.access_token import Access_token


@dataclass
class Artist:
    id: str
    name: str
    href: str
    uri: str
    popularity: int
    type: str
    followers: int
    genres: list[str]
    external_urls: list[dict[str, str]]
    images: list[Image]


@dataclass
class Track:
    id: str
    name: str
    href: str
    uri: str
    popularity: int
    type: str
    preview_url: str
    disc_number: int
    track_number: int
    duration_ms: int
    explicit: bool
    is_local: bool
    external_ids: list[dict[str, str]]
    external_urls: list[dict[str, str]]
    artists: list[Artist]
    available_markets: list[str]
    album: Optional["Album"]


@dataclass
class Album:
    id: str
    name: str
    href: str
    uri: str
    popularity: int
    type: str
    album_type: str
    release_date: str
    release_date_precision: str
    available_markets: list[str]
    genres: list[str]
    label: str
    external_urls: list[dict[str, str]]
    external_ids: list[dict[str, str]]
    copyrights: list[dict[str, str]]
    images: list[Image]
    artists: list[Artist]
    tracks_total: int
    tracks: list[Track]


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
            return self.make_artist(response.content)
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
        return self.make_artists_list(response.content)

    def get_artist_related_artists(self, id: str) -> list[Artist] | None:
        """returns a list of Artist Objects related to the artist specified by its id
        https://developer.spotify.com/documentation/web-api/reference/get-an-artists-related-artists

        :param id: Spotify id of the artist
        :type id: str
        :returns:  list of Artist objects  or None if id does not match an artist
        """
        url = HTTP_GET_RELATED_ARTISTS.replace("{id}", id)
        response = self._get_api_response_with_access_token(url)
        if response.status_code == 200:
            return self.make_artists_list(response.content)
        return None

    def get_track(self, id: str) -> Track | None:
        """returns the details of a track specified by its id
        https://developer.spotify.com/documentation/web-api/reference/get-track

        :param id: Spotify id of the track
        :type id: str
        :returns:  Track object or None if id does not match a track
        """
        url = HTTP_GET_TRACK.replace("{id}", id)
        response = self._get_api_response_with_access_token(url)
        if response.status_code == 200:
            return self.make_track(response.content)
        return None

    def get_album(self, id: str) -> Album | None:
        """returns the details of an album specified by its id
        https://developer.spotify.com/documentation/web-api/reference/get-an-album

        :param id: Spotify id of the album
        :type id: str
        :returns:  Album object or None if id does not match a track
        """
        url = HTTP_GET_ALBUM.replace("{id}", id)
        response = self._get_api_response_with_access_token(url)
        if response.status_code == 200:
            return self.make_album(response.content)
        return None

    def make_artist(self, json_content: bytes | Any) -> Artist:
        if isinstance(json_content, bytes):
            _dict = json.loads(json_content)
        else:
            _dict = json_content

        # some values maybe present or not depending on the api call (eg. /Artists and /tracks)
        genres: list[str] = []
        images: list[Image] = []
        followers = 0
        if "genres" in _dict:
            genres = [x for x in _dict["genres"]]
        if "images" in _dict:
            images = [Image(x["url"], x["height"], x["width"]) for x in _dict["images"]]
        if "followers" in _dict and "total" in _dict["followers"]:
            followers = _dict["followers"]["total"]

        ext_urls = [{x: _dict["external_urls"][x]} for x in _dict["external_urls"]]

        return Artist(
            id=_dict["id"],
            name=_dict["name"],
            href=_dict["href"],
            uri=_dict["uri"],
            popularity=_value_or_default("popularity", _dict, 0),
            type=_dict["type"],
            followers=followers,
            genres=genres,
            external_urls=ext_urls,
            images=images,
        )

    def make_artists_list(self, json_content: bytes) -> list[Artist]:
        _dict = json.loads(json_content)
        artists_list = []
        for artist in _dict["artists"]:
            if artist:
                artists_list.append(self.make_artist(artist))
        return artists_list

    def make_track(self, json_content: bytes | Any) -> Track:
        if isinstance(json_content, bytes):
            _dict = json.loads(json_content)
        else:
            _dict = json_content

        available_markets = []
        ext_ids = []
        if "available_markets" in _dict:
            available_markets = [x for x in _dict["available_markets"]]
        if "external_ids" in _dict:
            ext_ids = [{x: _dict["external_ids"][x]} for x in _dict["external_ids"]]

        ext_urls = [{x: _dict["external_urls"][x]} for x in _dict["external_urls"]]
        artists = [self.make_artist(x) for x in _dict["artists"]]
        album = self.make_album(_dict["album"]) if "album" in _dict else None

        return Track(
            id=_dict["id"],
            name=_dict["name"],
            href=_dict["href"],
            uri=_dict["uri"],
            popularity=_value_or_default("popularity", _dict, 0),
            type=_dict["type"],
            preview_url=_dict["preview_url"],
            disc_number=_dict["disc_number"],
            track_number=_dict["track_number"],
            duration_ms=_dict["duration_ms"],
            explicit=_dict["explicit"],
            is_local=_dict["is_local"],
            external_ids=ext_ids,
            external_urls=ext_urls,
            artists=artists,
            available_markets=available_markets,
            album=album,
        )

    def make_album(self, json_content: bytes | Any) -> Album:
        if isinstance(json_content, bytes):
            print(json_content)
            _dict = json.loads(json_content)
        else:
            _dict = json_content

        genres: list[str] = []
        available_markets = []
        images: list[Image] = []
        ext_ids = []
        copyrights = []
        tracks = []
        tracks_total = 0
        if "genres" in _dict:
            genres = [x for x in _dict["genres"]]
        if "available_markets" in _dict:
            available_markets = [x for x in _dict["available_markets"]]
        if "images" in _dict:
            images = [Image(x["url"], x["height"], x["width"]) for x in _dict["images"]]
        if "external_ids" in _dict:
            ext_ids = [{x: _dict["external_ids"][x]} for x in _dict["external_ids"]]
        if "copyrights" in _dict:
            copyrights = [x for x in _dict["copyrights"]]
        if "tracks" in _dict and "items" in _dict["tracks"]:
            tracks = [self.make_track(x) for x in _dict["tracks"]["items"]]
        if "tracks" in _dict and "total" in _dict["tracks"]:
            tracks_total = _dict["tracks"]["total"]

        ext_urls = [{x: _dict["external_urls"][x]} for x in _dict["external_urls"]]
        artists = [self.make_artist(x) for x in _dict["artists"]]

        return Album(
            id=_dict["id"],
            name=_dict["name"],
            href=_dict["href"],
            uri=_dict["uri"],
            popularity=_value_or_default("popularity", _dict, 0),
            type=_dict["type"],
            album_type=_dict["type"],
            release_date=_dict["release_date"],
            release_date_precision=_dict["release_date_precision"],
            available_markets=available_markets,
            genres=genres,
            label=_value_or_default("label", _dict, ""),
            external_urls=ext_urls,
            external_ids=ext_ids,
            copyrights=copyrights,
            images=images,
            artists=artists,
            tracks_total=tracks_total,
            tracks=tracks,
        )


def _value_or_default(key: str, _dict: dict[str, Any], default: Any) -> Any:
    if key in _dict:
        return _dict[key]
    return default
