"""

class dealing with all the tracks API calls

"""

import json
from dataclasses import dataclass

from sympyfy.api.artists import Artist, make_artist


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
    # album: Album


def make_track(json_content: bytes) -> Track:
    _dict = json.loads(json_content)

    ext_ids = [{x: _dict["external_ids"][x]} for x in _dict["external_ids"]]
    ext_urls = [{x: _dict["external_urls"][x]} for x in _dict["external_urls"]]
    artists = [make_artist(x) for x in _dict["artists"]]

    return Track(
        id=_dict["id"],
        name=_dict["name"],
        href=_dict["href"],
        uri=_dict["uri"],
        popularity=_dict["popularity"],
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
    )
