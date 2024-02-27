"""

main sympyfy class

"""
import base64
import json
import os
import sys
from typing import Any

from dotenv import dotenv_values
from requests import Response, get, post

import sympyfy.api_urls as api
from sympyfy.api_structures import Album, Artist, Audio_features, Category, Image, Navigation, Track
from sympyfy.common import (
    INCLUDE_GROUPS,
    add_include_groups,
    add_market,
    add_pagination,
    add_url_parameter,
    sanitize,
    value_or_default,
)
from sympyfy.tokens.access_token import Access_token


class Sympyfy:
    # main sympyfy class
    def __init__(self) -> None:
        self._spotify_credentials: dict[str, str]
        self._access_token: Access_token
        self._spotify_markets: set[str] = set()
        self._genre_seeds: set[str] = set()

    def load_credentials(self) -> None:
        """Load Spotify credential request for an Access Token<br>
        See: [https://developer.spotify.com/documentation/web-api/concepts/access-token](https://developer.spotify.com/documentation/web-api/concepts/access-token)
        """
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

        response = post(api.HTTP_GET_APP_TOKEN, headers=headers, data=data)
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

    def get_artist(self, artist_id: str) -> Artist | None:
        """returns an Artist Object specified by its id<br>
        See: [https://developer.spotify.com/documentation/web-api/reference/get-an-artist](https://developer.spotify.com/documentation/web-api/reference/get-an-artist)

        Parameters:
            artist_id: Spotify id of the artist

        Returns:
            Artist object or None if id does not match an artist
        """
        url = api.HTTP_GET_ARTIST.replace("{id}", artist_id)
        response = self._get_api_response_with_access_token(sanitize(url))
        if response.status_code == 200:
            return self.__make_artist(response.content)
        return None

    def get_several_artists(self, artist_ids: list[str]) -> list[Artist]:
        """returns a list of Artist Objects specified by a list of their ids<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-multiple-artists](https://developer.spotify.com/documentation/web-api/reference/get-multiple-artists)

        Parameters:
            artist_ids: list of artists ids

        Returns:
            list of Artist objects
        """
        url = api.HTTP_GET_SEVERAL_ARTISTS.replace("{ids}", "%2C".join(artist_ids))
        response = self._get_api_response_with_access_token(sanitize(url))
        return self.__make_artists_list(response.content)

    def get_artist_albums(
        self,
        artist_id: str,
        market: str | None = None,
        include_groups: list[str] = INCLUDE_GROUPS,
        limit: int = 20,
        offset: int = 0,
    ) -> tuple[list[Album], Navigation] | None:
        """returns a list of album Objects related to the artist specified by its id in a given market. Result is paginated.<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-an-artists-albums](https://developer.spotify.com/documentation/web-api/reference/get-an-artists-albums)

        Parameters:
            artist_id: Spotify id of the artist
            market: ISO 2 character country code of the market
            include_groups: A list of keywords that will be used to filter the response. Valid values are: album, single, appears_on, compilation.
            limit: Maximum number of albums appearing
            offset: Index of first album to return

        Returns:
            Navigation Object and list of Album objects or None if id does not match an artist
        """
        url = (
            api.HTTP_GET_ARTIST_ALBUMS.replace("{id}", artist_id)
            + add_market(market, self.markets)
            + add_pagination(limit, offset)
            + add_include_groups(include_groups)
        )
        response = self._get_api_response_with_access_token(sanitize(url))
        if response.status_code == 200:
            return self.__make_artist_albums(response.content)
        return None

    def get_artist_top_tracks(
        self, artist_id: str, market: str | None = None
    ) -> list[Track] | None:
        """returns a list of top Track Objects related to the artist specified by its id in a given market<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-an-artists-top-tracks](https://developer.spotify.com/documentation/web-api/reference/get-an-artists-top-tracks)

        Parameters:
            artist_id: Spotify id of the artist
            market: ISO 2 character country code of the market

        Returns:
            list of Tracks objects or None if id does not match an artist
        """
        url = api.HTTP_GET_ARTIST_TOP_TRACKS.replace("{id}", artist_id) + add_market(
            market, self.markets
        )
        response = self._get_api_response_with_access_token(sanitize(url))
        if response.status_code == 200:
            return self.__make_tracks_list(response.content)
        return None

    def get_artist_related_artists(self, artist_id: str) -> list[Artist] | None:
        """returns a list of Artist Objects related to the artist specified by its id<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-an-artists-related-artists](https://developer.spotify.com/documentation/web-api/reference/get-an-artists-related-artists)

        Parameters:
            artist_id: Spotify id of the artist

        Returns:
            list of Artist objects or None if id does not match an artist
        """
        url = api.HTTP_GET_RELATED_ARTISTS.replace("{id}", artist_id)
        response = self._get_api_response_with_access_token(sanitize(url))
        if response.status_code == 200:
            return self.__make_artists_list(response.content)
        return None

    def get_album(self, album_id: str, market: str | None = None) -> Album | None:
        """returns the details of an album specified by its id<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-an-album](https://developer.spotify.com/documentation/web-api/reference/get-an-album)

        Parameters:
            album_id: Spotify id of the album
            market: Market to search in

        Returns:
            Album object or None if id does not match a track
        """
        url = api.HTTP_GET_ALBUM.replace("{id}", album_id) + add_market(market, self.markets)
        response = self._get_api_response_with_access_token(sanitize(url))
        if response.status_code == 200:
            return self.__make_album(response.content)
        return None

    def get_several_albums(self, album_ids: list[str], market: str | None = None) -> list[Album]:
        """returns a list of Album Objects specified by a list of their ids<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-multiple-albums](https://developer.spotify.com/documentation/web-api/reference/get-multiple-albums)

        Parameters:
            album_ids: list of albums ids
            market: Market to search in

        Returns:
            list of Albums objects
        """
        url = api.HTTP_GET_SEVERAL_ALBUMS.replace("{ids}", "%2C".join(album_ids)) + add_market(
            market, self.markets
        )
        response = self._get_api_response_with_access_token(sanitize(url))
        return self.__make_albums_list(response.content)

    def get_album_tracks(
        self,
        album_id: str,
        market: str | None = None,
        limit: int = 20,
        offset: int = 0,
    ) -> tuple[list[Track], Navigation] | None:
        """returns a list of track Objects related to the album specified by its id in a given market. Result is paginated.<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-an-albums-tracks](https://developer.spotify.com/documentation/web-api/reference/get-an-albums-tracks)

        Parameters:
            album_id: Spotify id of the artist
            market: ISO 2 character country code of the market
            limit: Maximum number of tracks appearing
            offset: Index of first track to return

        Returns:
            Navigation Object and list of track objects or None if id does not match an album
        """
        url = (
            api.HTTP_GET_ALBUM_TRACKS.replace("{id}", album_id)
            + add_market(market, self.markets)
            + add_pagination(limit, offset)
        )
        response = self._get_api_response_with_access_token(sanitize(url))
        if response.status_code == 200:
            return self.__make_album_tracks(response.content)
        return None

    def get_new_releases(self) -> tuple[list[Track], Navigation]:
        """Get a list of new album releases featured in Spotify (shown, for example, on a Spotify player’s “Browse” tab).<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-new-releases](https://developer.spotify.com/documentation/web-api/reference/get-new-releases)

        Returns:
            List of Track object plus a Navigation object
        """
        url = api.HTTP_GET_NEW_RELEASES
        response = self._get_api_response_with_access_token(sanitize(url))
        return self.__make_new_releases(response.content)

    def get_track(self, track_id: str, market: str | None = None) -> Track | None:
        """returns the details of a track specified by its id<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-track](https://developer.spotify.com/documentation/web-api/reference/get-track)

        Parameters:
            track_id: Spotify id of the track
            market: Market to search in

        Returns:
            Track object or None if id does not match a track
        """
        url = api.HTTP_GET_TRACK.replace("{id}", track_id) + add_market(market, self.markets)
        response = self._get_api_response_with_access_token(sanitize(url))
        if response.status_code == 200:
            return self.__make_track(response.content)
        return None

    def get_several_tracks(self, track_ids: list[str], market: str | None = None) -> list[Track]:
        """returns a list of Track Objects specified by a list of their ids<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-several-tracks](https://developer.spotify.com/documentation/web-api/reference/get-several-tracks)

        Parameters:
            track_ids: list of tracks ids
            market: Market to search in

        Returns:
            list of Tracks objects
        """
        url = api.HTTP_GET_SEVERAL_TRACKS.replace("{ids}", "%2C".join(track_ids)) + add_market(
            market, self.markets
        )
        response = self._get_api_response_with_access_token(sanitize(url))
        return self.__make_tracks_list(response.content)

    def get_track_audio_features(self, track_id: str) -> Audio_features | None:
        """returns a Audio_features Object specified by its ids<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-audio-features](https://developer.spotify.com/documentation/web-api/reference/get-audio-features)

        Parameters:
            track_id: Spotify id of the track

        Returns:
            List of Audio_features object
        """
        url = api.HTTP_GET_TRACK_AUDIO_FEATURES.replace("{id}", track_id)
        response = self._get_api_response_with_access_token(sanitize(url))
        if response.status_code == 200:
            return self.__make_audio_features(response.content)
        return None

    def get_several_track_audio_features(self, track_ids: list[str]) -> list[Audio_features]:
        """returns a list of Audio_features Object specified by a list of their ids<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-several-audio-features](https://developer.spotify.com/documentation/web-api/reference/get-several-audio-features)

        Parameters
            track_ids: list of tracks ids

        Returns:
            List of Audio_features objects
        """
        url = api.HTTP_GET_SEVERAL_TRACK_AUDIO_FEATURES.replace("{ids}", "%2C".join(track_ids))
        response = self._get_api_response_with_access_token(sanitize(url))
        return self.__make_audio_features_list(response.content)

    def get_genres(self) -> set[str]:
        """Retrieve a list of available genres seed parameter values for recommendations.<br>
        Please use the [genres property](0sympyfy.md#sympyfy.Sympyfy.genres), this method is public only to match the Spotify API<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-recommendation-genres](https://developer.spotify.com/documentation/web-api/reference/get-recommendation-genres)

        Returns:
            list of genres seeds. Example: ["alternative","samba"]
        """
        url = api.HTTP_GET_GENRES
        response = self._get_api_response_with_access_token(sanitize(url))
        return self.__make_simple_set(response.content, "genres")

    @property
    def genres(self) -> set[str]:
        """Retrieve a list of available genres seed parameter values for recommendations.<br>
        This is the preferred way to get this information since it is lazy loaded from the api via the method [get_markets](0sympyfy.md#sympyfy.Sympyfy.get_genres)
        [https://developer.spotify.com/documentation/web-api/reference/get-recommendation-genres](https://developer.spotify.com/documentation/web-api/reference/get-recommendation-genres)

        Returns:
            list of genres seeds. Example: ["alternative","samba"]
        """
        if not self._genre_seeds:
            # lazy loading of genres
            self._genre_seeds = self.get_genres()
        return self._genre_seeds

    def get_markets(self) -> set[str]:
        """returns the list of markets where Spotify is available.<br>
        Please use the [markets property](0sympyfy.md#sympyfy.Sympyfy.markets), this method is public only to match the Spotify API<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-available-markets](https://developer.spotify.com/documentation/web-api/reference/get-available-markets)<br>
        [https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

        Returns:
            list of ISO 3166-1 alpha-2 country codes
        """
        url = api.HTTP_GET_MARKETS
        response = self._get_api_response_with_access_token(sanitize(url))
        return self.__make_simple_set(response.content, "markets")

    @property
    def markets(self) -> set[str]:
        """returns the list of markets where Spotify is available.<br>
        This is the preferred way to get this information since it is lazy loaded from the api via the method [get_markets](0sympyfy.md#sympyfy.Sympyfy.get_markets)
        [https://developer.spotify.com/documentation/web-api/reference/get-available-markets](https://developer.spotify.com/documentation/web-api/reference/get-available-markets)<br>
        [https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

        Returns:
            list of ISO 3166-1 alpha-2 country codes
        """
        if not self._spotify_markets:
            # lazy loading of markets
            self._spotify_markets = self.get_markets()
        return self._spotify_markets

    def get_browse_category(self, category_id: str, locale: str | None = None) -> Category | None:
        """Get a single category used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab).<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-a-category](https://developer.spotify.com/documentation/web-api/reference/get-a-category)

        Parameters:
            category_id: The Spotify category ID for the category.
            locale: The desired language, consisting of an ISO 639-1 language code and an ISO 3166-1 alpha-2 country code, joined by an underscore. For example: es_MX, meaning "Spanish (Mexico)". Provide this parameter if you want the category strings returned in a particular language. Note: if locale is not supplied, or if the specified language is not available, the category strings returned will be in the Spotify default language (American English).

        Returns:
            a Category object or None if if the id is unknown
        """
        url = api.HTTP_GET_BROWSE_CATEGORY.replace("{id}", category_id) + add_url_parameter(
            "locale", locale
        )
        response = self._get_api_response_with_access_token(sanitize(url))
        if response.status_code == 200:
            return self.__make_category(response.content)
        return None

    def get_several_browse_categories(
        self,
        locale: str | None = None,
        limit: int = 20,
        offset: int = 0,
    ) -> tuple[list[Category], Navigation]:
        """Get a list of categories used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab).<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-categories](https://developer.spotify.com/documentation/web-api/reference/get-categories)

        Parameters:
            locale: The desired language, consisting of an ISO 639-1 language code and an ISO 3166-1 alpha-2 country code, joined by an underscore. For example: es_MX, meaning "Spanish (Mexico)". Provide this parameter if you want the category strings returned in a particular language. Note: if locale is not supplied, or if the specified language is not available, the category strings returned will be in the Spotify default language (American English).
            limit: The maximum number of Categories to return. Default: 20. Minimum: 1. Maximum: 50.
            offset: The index of the first Category to return. Default: 0 (the first Category). Use with limit to get the next set of Categories.

        Returns:
            a list of Category objects and a Navigation Object
        """
        url = (
            api.HTTP_GET_SEVERAL_BROWSE_CATEGORIES
            + add_url_parameter("locale", locale)
            + add_pagination(limit, offset)
        )
        response = self._get_api_response_with_access_token(sanitize(url))
        print(response.content)
        return self.__make_categories_list(response.content)

    def __make_artist(self, json_content: bytes | Any) -> Artist:
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
            popularity=value_or_default("popularity", _dict, 0),
            type=_dict["type"],
            followers=followers,
            genres=genres,
            external_urls=ext_urls,
            images=images,
        )

    def __make_artists_list(self, json_content: bytes) -> list[Artist]:
        _dict = json.loads(json_content)
        artists_list = []
        for artist in _dict["artists"]:
            if artist:
                artists_list.append(self.__make_artist(artist))
        return artists_list

    def __make_artist_albums(self, json_content: bytes) -> tuple[list[Album], Navigation]:
        _dict = json.loads(json_content)
        navigation = Navigation(
            href=_dict["href"],
            next=_dict["next"],
            previous=_dict["previous"],
            limit=_dict["limit"],
            offset=_dict["offset"],
            total=_dict["total"],
        )

        return self.__make_albums_list({"albums": _dict["items"]}), navigation

    def __make_track(self, json_content: bytes | Any) -> Track:
        if isinstance(json_content, bytes):
            _dict = json.loads(json_content)
        else:
            _dict = json_content

        available_markets = []
        ext_ids = []
        restrictions = ""
        if "available_markets" in _dict:
            available_markets = [x for x in _dict["available_markets"]]
        if "external_ids" in _dict:
            ext_ids = [{x: _dict["external_ids"][x]} for x in _dict["external_ids"]]
        if "restrictions" in _dict and "reason" in _dict["restrictions"]:
            restrictions = _dict["restrictions"]["reason"]

        ext_urls = [{x: _dict["external_urls"][x]} for x in _dict["external_urls"]]
        artists = [self.__make_artist(x) for x in _dict["artists"]]
        album = self.__make_album(_dict["album"]) if "album" in _dict else None

        return Track(
            id=_dict["id"],
            name=_dict["name"],
            href=_dict["href"],
            uri=_dict["uri"],
            popularity=value_or_default("popularity", _dict, 0),
            type=_dict["type"],
            preview_url=value_or_default("preview_url", _dict, None),
            disc_number=value_or_default("disc_number", _dict, 0),
            track_number=value_or_default("track_number", _dict, 0),
            duration_ms=value_or_default("duration_ms", _dict, 0),
            explicit=value_or_default("explicit", _dict, False),
            is_local=value_or_default("is_local", _dict, False),
            is_playable=value_or_default("is_playable", _dict, True),
            external_ids=ext_ids,
            external_urls=ext_urls,
            artists=artists,
            available_markets=available_markets,
            album=album,
            linked_from=value_or_default("linked_from", _dict, None),
            restrictions=restrictions,
        )

    def __make_tracks_list(self, json_content: bytes | Any) -> list[Track]:
        if isinstance(json_content, bytes):
            _dict = json.loads(json_content)
        else:
            _dict = json_content
        track_list = []
        for track in _dict["tracks"]:
            if track:
                track_list.append(self.__make_track(track))
        return track_list

    def __make_album(self, json_content: bytes | Any) -> Album:
        if isinstance(json_content, bytes):
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
            tracks = [self.__make_track(x) for x in _dict["tracks"]["items"]]
        if "tracks" in _dict and "total" in _dict["tracks"]:
            tracks_total = _dict["tracks"]["total"]

        ext_urls = [{x: _dict["external_urls"][x]} for x in _dict["external_urls"]]
        artists = [self.__make_artist(x) for x in _dict["artists"]]

        return Album(
            id=_dict["id"],
            name=_dict["name"],
            href=_dict["href"],
            uri=_dict["uri"],
            popularity=value_or_default("popularity", _dict, 0),
            type=_dict["type"],
            album_type=_dict["type"],
            album_group=value_or_default("album_group", _dict, "album"),
            release_date=_dict["release_date"],
            release_date_precision=_dict["release_date_precision"],
            available_markets=available_markets,
            genres=genres,
            label=value_or_default("label", _dict, ""),
            external_urls=ext_urls,
            external_ids=ext_ids,
            copyrights=copyrights,
            images=images,
            artists=artists,
            tracks_total=tracks_total,
            tracks=tracks,
        )

    def __make_albums_list(self, json_content: bytes | Any) -> list[Album]:
        if isinstance(json_content, bytes):
            _dict = json.loads(json_content)
        else:
            _dict = json_content
        albums_list = []
        for album in _dict["albums"]:
            if album:
                albums_list.append(self.__make_album(album))
        return albums_list

    def __make_album_tracks(self, json_content: bytes | Any) -> tuple[list[Track], Navigation]:
        if isinstance(json_content, bytes):
            _dict = json.loads(json_content)
        else:
            _dict = json_content
        navigation = Navigation(
            href=_dict["href"],
            next=_dict["next"],
            previous=_dict["previous"],
            limit=_dict["limit"],
            offset=_dict["offset"],
            total=_dict["total"],
        )

        return self.__make_tracks_list({"tracks": _dict["items"]}), navigation

    def __make_new_releases(self, json_content: bytes) -> tuple[list[Track], Navigation]:
        _dict = json.loads(json_content)
        return self.__make_album_tracks(_dict["albums"])

    def __make_audio_features(self, json_content: bytes | Any) -> Audio_features:
        if isinstance(json_content, bytes):
            print(json_content)
            _dict = json.loads(json_content)
        else:
            _dict = json_content

        return Audio_features(
            id=_dict["id"],
            track_href=_dict["track_href"],
            uri=_dict["uri"],
            analysis_url=_dict["analysis_url"],
            type=_dict["type"],
            key=_dict["key"],
            mode=_dict["mode"],
            time_signature=_dict["time_signature"],
            duration_ms=_dict["duration_ms"],
            danceability=_dict["danceability"],
            energy=_dict["energy"],
            loudness=_dict["loudness"],
            speechiness=_dict["speechiness"],
            acousticness=_dict["acousticness"],
            instrumentalness=_dict["instrumentalness"],
            liveness=_dict["liveness"],
            valence=_dict["valence"],
            tempo=_dict["tempo"],
        )

    def __make_audio_features_list(self, json_content: bytes) -> list[Audio_features]:
        _dict = json.loads(json_content)
        audio_features_list = []
        for audio_feature in _dict["audio_features"]:
            if audio_feature:
                audio_features_list.append(self.__make_audio_features(audio_feature))
        return audio_features_list

    def __make_simple_set(self, json_content: bytes, key: str) -> set[str]:
        _dict = json.loads(json_content)
        return set(_dict[key])

    def __make_category(self, json_content: bytes | Any) -> Category:
        if isinstance(json_content, bytes):
            print(json_content)
            _dict = json.loads(json_content)
        else:
            _dict = json_content

        icons: list[Image] = []
        if "icons" in _dict:
            icons = [Image(x["url"], x["height"], x["width"]) for x in _dict["icons"]]

        return Category(id=_dict["id"], name=_dict["name"], href=_dict["href"], icons=icons)

    def __make_categories_list(self, json_content: bytes) -> tuple[list[Category], Navigation]:
        _dict = json.loads(json_content)["categories"]
        navigation = Navigation(
            href=_dict["href"],
            next=_dict["next"],
            previous=_dict["previous"],
            limit=_dict["limit"],
            offset=_dict["offset"],
            total=_dict["total"],
        )

        categories_list = []
        for category in _dict["items"]:
            if category:
                categories_list.append(self.__make_category(category))
        return categories_list, navigation
