"""

class dealing with all the artists API calls

"""

import json
from dataclasses import dataclass
from typing import Any

from sympyfy.api.common import Image


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


def make_artist(json_content: bytes | Any) -> Artist:
    if isinstance(json_content, bytes):
        _dict = json.loads(json_content)
    else:
        _dict = json_content

    # some values maybe present or not depending on the api call (eg. /Artists and /tracks)
    ext_urls = []
    genres: list[str] = []
    images: list[Image] = []
    followers = 0

    if "external_urls" in _dict:
        ext_urls = [{x: _dict["external_urls"][x]} for x in _dict["external_urls"]]
    if "genres" in _dict:
        genres = [x for x in _dict["genres"]]
    if "images" in _dict:
        images = [Image(x["url"], x["height"], x["width"]) for x in _dict["images"]]
    if "followers" in _dict and "total" in _dict["followers"]:
        followers = _dict["followers"]["total"]

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


def make_artists_list(json_content: bytes) -> list[Artist]:
    _dict = json.loads(json_content)
    artists_list = []
    for artist in _dict["artists"]:
        if artist:
            artists_list.append(make_artist(artist))
    return artists_list


def _value_or_default(key: str, _dict: dict[str, Any], default: Any) -> Any:
    if key in _dict:
        return _dict[key]
    return default
