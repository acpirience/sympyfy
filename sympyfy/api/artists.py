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
    popularity: int
    type: str
    uri: str
    href: str
    external_urls: list[dict[str, str]]
    followers: int
    genres: list[str]
    images: list[Image]


def make_artist(json_content: bytes | Any) -> Artist:
    if isinstance(json_content, bytes):
        _dict = json.loads(json_content)
    else:
        _dict = json_content

    ext_urls = [{x: _dict["external_urls"][x]} for x in _dict["external_urls"]]
    genres = [x for x in _dict["genres"]]
    images = [Image(x["url"], x["height"], x["width"]) for x in _dict["images"]]

    return Artist(
        _dict["id"],
        _dict["name"],
        _dict["popularity"],
        _dict["type"],
        _dict["uri"],
        _dict["href"],
        ext_urls,
        _dict["followers"]["total"],
        genres,
        images,
    )


def make_artists_list(json_content: bytes) -> list[Artist]:
    _dict = json.loads(json_content)
    artists_list = []
    for artist in _dict["artists"]:
        if artist:
            artists_list.append(make_artist(artist))
    return artists_list
