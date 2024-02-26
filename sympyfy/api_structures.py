"""

contains the data structures for the spotify API

"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Image:
    url: str
    height: int
    width: int


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
    is_playable: bool
    external_ids: list[dict[str, str]]
    external_urls: list[dict[str, str]]
    artists: list[Artist]
    available_markets: list[str]
    album: Optional["Album"]


@dataclass
class Audio_features:
    id: str
    track_href: str
    uri: str
    analysis_url: str
    type: str
    key: int
    mode: int
    time_signature: int
    duration_ms: int
    danceability: float
    energy: float
    loudness: float
    speechiness: float
    acousticness: float
    instrumentalness: float
    liveness: float
    valence: float
    tempo: float


@dataclass
class Album:
    id: str
    name: str
    href: str
    uri: str
    popularity: int
    type: str
    album_type: str
    album_group: str
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


@dataclass
class Navigation:
    href: str
    next: str | None
    previous: str | None
    limit: int
    offset: int
    total: int
