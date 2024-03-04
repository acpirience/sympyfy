"""

main sympyfy class

"""
import json

from requests import Response, get
from rich.console import Console

import sympyfy.api_urls as api
from sympyfy.api_structures import (
    Album,
    Artist,
    Audio_features,
    Category,
    Episode,
    Image,
    Navigation,
    Playlist,
    Playlist_item,
    Show,
    Track,
    User,
)
from sympyfy.common import (
    INCLUDE_GROUPS,
    add_include_groups,
    add_market,
    add_pagination,
    add_url_parameter,
    sanitize,
)
from sympyfy.tokens.access_token import Access_token

console = Console()


class Sympyfy:
    # main sympyfy class
    def __init__(self) -> None:
        self._access_token: Access_token
        self._spotify_markets: set[str] = set()
        self._genre_seeds: set[str] = set()

    def load_credentials(self, client_id: str = "", client_secret: str = "") -> None:
        """Load Spotify credential request for an Access Token. If parameters are provided, they will be used; else environment variables will be used, else we will try in the .env file<br>
        See: [https://developer.spotify.com/documentation/web-api/concepts/access-token](https://developer.spotify.com/documentation/web-api/concepts/access-token)

        Parameters:
            client_id: Client Id of the application, provided by Spotify.
            client_secret: Client secret of the application, provided by Spotify.
        """
        self._access_token = Access_token(client_id, client_secret)
        self._access_token.load_spotify_credentials()
        self._access_token.load_access_token()

    def _get_api_response_with_access_token(self, url: str) -> Response:
        # Generic function that returns the json response
        # of an API call using access token
        return get(url, headers=self._access_token.headers)

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

    def get_artist_albums(
        self,
        artist_id: str,
        market: str | None = None,
        include_groups: list[str] = INCLUDE_GROUPS,
        limit: int = 20,
        offset: int = 0,
    ) -> Navigation | None:
        """Get Spotify catalog information about an artist's albums.<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-an-artists-albums](https://developer.spotify.com/documentation/web-api/reference/get-an-artists-albums)

        Parameters:
            artist_id: The Spotify ID of the artist.
            market: An ISO 3166-1 alpha-2 country code. If a country code is specified, only content that is available in that market will be returned. If a valid user access token is specified in the request header, the country associated with the user account will take priority over this parameter.
            include_groups: A list of keywords that will be used to filter the response. Valid values are: album, single, appears_on, compilation.
            limit: The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50.
            offset: The index of the first item to return. Default: 0 (the first item). Use with limit to get the next set of items.

        Returns:
            A Navigation Object of Album Objects
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

    def get_album(self, album_id: str, market: str | None = None) -> Album | None:
        """returns the details of an album specified by its id<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-an-album](https://developer.spotify.com/documentation/web-api/reference/get-an-album)

        Parameters:
            album_id: Spotify id of the album
            market: Market to search in²

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
        console.print(response.json())
        return self.__make_albums_list(response.content)

    def get_album_tracks(
        self,
        album_id: str,
        market: str | None = None,
        limit: int = 20,
        offset: int = 0,
    ) -> Navigation | None:
        """returns a list of track Objects related to the album specified by its id in a given market. Result is paginated.<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-an-albums-tracks](https://developer.spotify.com/documentation/web-api/reference/get-an-albums-tracks)

        Parameters:
            album_id: Spotify id of the artist
            market: ISO 2 character country code of the market
            limit: Maximum number of tracks appearing
            offset: Index of first track to return

        Returns:
            A Navigation Object of Track Objects
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

    def get_new_releases(self) -> Navigation:
        """Get a list of new album releases featured in Spotify (shown, for example, on a Spotify player’s “Browse” tab).<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-new-releases](https://developer.spotify.com/documentation/web-api/reference/get-new-releases)

        Returns:
            A Navigation object of Track Objects
        """
        url = api.HTTP_GET_NEW_RELEASES
        response = self._get_api_response_with_access_token(sanitize(url))
        return self.__make_new_releases(response.content)

    def get_browse_category(self, category_id: str, locale: str | None = None) -> Category | None:
        """Get a single category used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab).<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-a-category](https://developer.spotify.com/documentation/web-api/reference/get-a-category)

        Parameters:
            category_id: The Spotify category ID for the category.
            locale: The desired language, consisting of an ISO 639-1 language code and an ISO 3166-1 alpha-2 country code, joined by an underscore. For example: es_MX, meaning "Spanish (Mexico)". Provide this parameter if you want the category strings returned in a particular language. Note: if locale is not supplied, or if the specified language is not available, the category strings returned will be in the Spotify default language (American English).

        Returns:
            a Category object or None if its the id is unknown
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
    ) -> Navigation:
        """Get a list of categories used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab).<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-categories](https://developer.spotify.com/documentation/web-api/reference/get-categories)

        Parameters:
            locale: The desired language, consisting of an ISO 639-1 language code and an ISO 3166-1 alpha-2 country code, joined by an underscore. For example: es_MX, meaning "Spanish (Mexico)". Provide this parameter if you want the category strings returned in a particular language. Note: if locale is not supplied, or if the specified language is not available, the category strings returned will be in the Spotify default language (American English).
            limit: The maximum number of Categories to return. Default: 20. Minimum: 1. Maximum: 50.
            offset: The index of the first Category to return. Default: 0 (the first Category). Use with limit to get the next set of Categories.

        Returns:
            a Navigation Object of Category Objects
        """
        url = (
            api.HTTP_GET_SEVERAL_BROWSE_CATEGORIES
            + add_url_parameter("locale", locale)
            + add_pagination(limit, offset)
        )
        response = self._get_api_response_with_access_token(sanitize(url))
        return self.__make_categories_list(response.content)

    def get_show(self, show_id: str, market: str | None = None) -> Show | None:
        """Get Spotify catalog information for a single show identified by its unique Spotify ID.<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-a-show](https://developer.spotify.com/documentation/web-api/reference/get-a-show)

        Parameters:
            show_id: Spotify id of the track

        Returns:
            Show object or None if id does not match a show
        """
        url = api.HTTP_GET_SHOW.replace("{id}", show_id) + add_market(market, self.markets)
        response = self._get_api_response_with_access_token(sanitize(url))
        if response.status_code == 200:
            return self.__make_show(response.content)
        return None

    def get_several_shows(self, show_ids: list[str], market: str | None = None) -> list[Show]:
        """Get Spotify catalog information for several shows based on their Spotify IDs.<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-multiple-shows](https://developer.spotify.com/documentation/web-api/reference/get-multiple-shows)

        Parameters:
            show_ids: A list of the Spotify IDs for the shows. Maximum: 50 IDs.

        Returns:
            list of Show objects
        """
        url = api.HTTP_GET_SEVERAL_SHOWS.replace("{ids}", "%2C".join(show_ids)) + add_market(
            market, self.markets
        )
        response = self._get_api_response_with_access_token(sanitize(url))
        return self.__make_shows_list(response.content)

    def get_show_episodes(
        self, show_id: str, market: str | None = None, limit: int = 20, offset: int = 0
    ) -> Navigation | None:
        """Get Spotify catalog information about an show’s episodes. Optional parameters can be used to limit the number of episodes returned.<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-a-shows-episodes](https://developer.spotify.com/documentation/web-api/reference/get-a-shows-episodes)

        Parameters:
            show_id: The Spotify ID for the show.
            market: An ISO 3166-1 alpha-2 country code. If a country code is specified, only content that is available in that market will be returned. If a valid user access token is specified in the request header, the country associated with the user account will take priority over this parameter.
            limit: The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50.
            offset: The index of the first item to return. Default: 0 (the first item). Use with limit to get the next set of items.

        Returns:
            A navigation Objet of Show Objects or None if id does not match a show
        """
        url = (
            api.HTTP_GET_SHOW_EPISODES.replace("{id}", show_id)
            + add_market(market, self.markets)
            + add_pagination(limit, offset)
        )
        response = self._get_api_response_with_access_token(sanitize(url))
        if response.status_code == 200:
            return self.__make_show_episodes(response.content)
        return None

    def get_track(self, track_id: str, market: str | None = None) -> Track | None:
        """Get Spotify catalog information for a single track identified by its unique Spotify ID.<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-track](https://developer.spotify.com/documentation/web-api/reference/get-track)

        Parameters:
            track_id: Spotify id of the track
            market: An ISO 3166-1 alpha-2 country code. If a country code is specified, only content that is available in that market will be returned. If a valid user access token is specified in the request header, the country associated with the user account will take priority over this parameter.

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

    def get_user_profile(self, user_id: str) -> User | None:
        """Get public profile information about a Spotify user specified by its id<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-users-profile](https://developer.spotify.com/documentation/web-api/reference/get-users-profile)

        Parameters:
            user_id: The user's Spotify user ID.

        Returns:
            User Object
        """
        url = api.HTTP_GET_USER_PROFILE.replace("{id}", user_id)
        response = self._get_api_response_with_access_token(sanitize(url))
        if response.status_code == 200:
            return self.__make_user(response.content)
        return None

    def get_users_follow_playlist(self, playlist_id: str, user_ids: list[str]) -> list[bool] | None:
        """Check to see if one or more Spotify users are following a specified playlist.<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-users-profile](https://developer.spotify.com/documentation/web-api/reference/get-users-profile)

        Parameters:
            playlist_id: The Spotify ID of the playlist.
            user_ids: A  list of Spotify User IDs ; the ids of the users that you want to check to see if they follow the playlist. Maximum: 5 ids.

        Returns:
            list of bool
        """
        url = api.HTTP_GET_USERS_FOLLOW_PLAYLIST.replace("{id}", playlist_id).replace(
            "{ids}", "%2C".join(user_ids)
        )
        response = self._get_api_response_with_access_token(sanitize(url))
        if response.status_code == 200:
            return self.__make_users_follow_playlist(response.content)
        return None

    def get_playlist(
        self,
        playlist_id: str,
        market: str | None = None,
        fields: str | None = None,
        additional_types: list[str] | None = None,
    ) -> Playlist | None:
        """Get a playlist owned by a Spotify user.<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-playlist](https://developer.spotify.com/documentation/web-api/reference/get-playlist)

        Parameters:
            playlist_id: The Spotify ID of the playlist.
            market: An ISO 3166-1 alpha-2 country code. If a country code is specified, only content that is available in that market will be returned. If a valid user access token is specified in the request header, the country associated with the user account will take priority over this parameter.
            fields: Filters for the query: a comma-separated list of the fields to return. If omitted, all fields are returned. For example, to get just the playlist''s description and URI: fields=description,uri. A dot separator can be used to specify non-reoccurring fields, while parentheses can be used to specify reoccurring fields within objects. For example, to get just the added date and user ID of the adder: fields=tracks.items(added_at,added_by.id). Use multiple parentheses to drill down into nested objects, for example: fields=tracks.items(track(name,href,album(name,href))). Fields can be excluded by prefixing them with an exclamation mark, for example: fields=tracks.items(track(name,href,album(!name,href)))<br>
                Example: fields=items(added_by.id,track(name,href,album(name,href)))
            additional_types: A comma-separated list of item types that your client supports besides the default track type. Valid types are: track and episode.<br>
                Note: This parameter was introduced to allow existing clients to maintain their current behaviour and might be deprecated in the future.

        Returns:
            Playlist Object
        """
        if additional_types is None:
            additional_types = []
        url = (
            api.HTTP_GET_PLAYLIST.replace("{id}", playlist_id)
            + add_market(market, self.markets)
            + add_url_parameter("fields", fields)
            + (
                add_url_parameter("additional_types", ",".join(additional_types))
                if additional_types
                else ""
            )
        )
        response = self._get_api_response_with_access_token(sanitize(url))
        if response.status_code == 200:
            return self.__make_playlist(response.content)
        return None

    def get_playlist_cover_image(self, playlist_id: str) -> list[Image] | None:
        """Get the current image associated with a specific playlist.<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-playlist-cover](https://developer.spotify.com/documentation/web-api/reference/get-playlist-cover)

        Parameters:
            playlist_id: The Spotify ID of the playlist.

        Returns:
            List of Image Objects
        """
        url = api.HTTP_GET_PLAYLIST_COVER_IMAGE.replace("{id}", playlist_id)
        response = self._get_api_response_with_access_token(sanitize(url))
        if response.status_code == 200:
            return self.__make_playlist_cover_image(response.content)
        return None

    def __make_simple_set(self, json_content: bytes, key: str) -> set[str]:
        dict_content = json.loads(json_content)
        return set(dict_content[key])

    def __make_artist(self, json_content: bytes) -> Artist:
        artist: Artist = Artist.model_validate_json(json_content)
        return artist

    def __make_artists_list(self, json_content: bytes) -> list[Artist]:
        dict_content = json.loads(json_content)
        artists_list: list[Artist] = []
        for x in dict_content["artists"]:
            if x:
                artists_list.append(Artist.model_validate(x))
        return artists_list

    def __make_track(self, json_content: bytes) -> Track:
        track: Track = Track.model_validate_json(json_content)
        return track

    def __make_tracks_list(self, json_content: bytes) -> list[Track]:
        dict_content = json.loads(json_content)
        tracks_list: list[Track] = []
        for x in dict_content["tracks"]:
            if x:
                tracks_list.append(Track.model_validate(x))
        return tracks_list

    def __make_album(self, json_content: bytes) -> Album:
        album: Album = Album.model_validate_json(json_content)
        if album.tracks:
            album.tracks.items = [Track.model_validate(x) for x in album.tracks.items]
        return album

    def __make_albums_list(self, json_content: bytes) -> list[Album]:
        dict_content = json.loads(json_content)
        albums_list: list[Album] = []
        for x in dict_content["albums"]:
            if x:
                album = Album.model_validate(x)
                album.tracks.items = [Track.model_validate(x) for x in album.tracks.items]
                albums_list.append(album)
        return albums_list

    def __make_artist_albums(self, json_content: bytes) -> Navigation:
        navigation: Navigation = Navigation.model_validate_json(json_content)
        navigation.items = [Album.model_validate(x) for x in navigation.items]
        return navigation

    def __make_album_tracks(self, json_content: bytes) -> Navigation:
        navigation: Navigation = Navigation.model_validate_json(json_content)
        navigation.items = [Track.model_validate(x) for x in navigation.items]
        return navigation

    def __make_new_releases(self, json_content: bytes) -> Navigation:
        dict_content = json.loads(json_content)
        navigation: Navigation = Navigation.model_validate(dict_content["albums"])
        navigation.items = [Album.model_validate(x) for x in navigation.items]
        return navigation

    def __make_category(self, json_content) -> Category:
        category: Category = Category.model_validate_json(json_content)
        return category

    def __make_categories_list(self, json_content: bytes) -> Navigation:
        dict_content = json.loads(json_content)
        navigation: Navigation = Navigation.model_validate(dict_content["categories"])
        navigation.items = [Category.model_validate(x) for x in navigation.items]
        return navigation

    def __make_show(self, json_content: bytes) -> Show:
        show: Show = Show.model_validate_json(json_content)
        if show.episodes:
            show.episodes.items = [Episode.model_validate(x) for x in show.episodes.items]
        return show

    def __make_shows_list(self, json_content: bytes) -> list[Show]:
        dict_content = json.loads(json_content)
        shows_list: list[Show] = []
        for x in dict_content["shows"]:
            if x:
                shows_list.append(Show.model_validate(x))
        return shows_list

    def __make_show_episodes(self, json_content: bytes) -> Navigation:
        navigation: Navigation = Navigation.model_validate_json(json_content)
        navigation.items = [Episode.model_validate(x) for x in navigation.items]
        return navigation

    def __make_audio_features(self, json_content: bytes) -> Audio_features:
        audio_features = Audio_features.model_validate_json(json_content)
        return audio_features

    def __make_audio_features_list(self, json_content: bytes) -> list[Audio_features]:
        dict_content = json.loads(json_content)
        audio_features_list: list[Audio_features] = []
        for x in dict_content["audio_features"]:
            if x:
                audio_features_list.append(Audio_features.model_validate(x))
        return audio_features_list

    def __make_user(self, json_content: bytes) -> User:
        user: User = User.model_validate_json(json_content)
        return user

    def __make_users_follow_playlist(self, json_content: bytes) -> list[bool]:
        dict_content = json.loads(json_content)
        return dict_content

    def __make_playlist(self, json_content: bytes) -> Playlist:
        playlist = Playlist.model_validate_json(json_content)
        playlist.tracks.items = [Playlist_item.model_validate(x) for x in playlist.tracks.items]
        return playlist

    def __make_playlist_cover_image(self, json_content: bytes) -> list[Image]:
        dict_content = json.loads(json_content)
        print(json_content)
        images_list: list[Image] = [Image.model_validate(x) for x in dict_content]
        return images_list
