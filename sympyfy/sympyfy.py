"""

main sympyfy class

"""
import json
from html import escape
from typing import Any

from requests import Response, get
from rich.console import Console

import sympyfy.api_urls as api
from sympyfy.access_token import Access_token, Auth_type
from sympyfy.api_structures import (
    Album,
    Artist,
    Audio_analysis,
    Audio_features,
    Category,
    Episode,
    Image,
    Navigation,
    Playlist,
    Playlist_item,
    Recommendation,
    Show,
    Track,
    User,
)
from sympyfy.consts import INCLUDE_GROUPS, STYLE, TRACKS_ATTRIBUTES

console = Console()


class Sympyfy:
    # main sympyfy class
    def __init__(self) -> None:
        self._access_token: Access_token
        self._spotify_markets: set[str] = set()
        self._genre_seeds: set[str] = set()

    def load_credentials(
        self,
        auth_type: Auth_type = Auth_type.APP,
        client_id: str = "",
        client_secret: str = "",
        scope: list[str] | None = None,
    ) -> None:
        """Load Spotify credential request for an Access Token. If parameters are provided, they will be used; else environment variables will be used, else we will try in the .env file<br>
        See: [https://developer.spotify.com/documentation/web-api/concepts/access-token](https://developer.spotify.com/documentation/web-api/concepts/access-token)

        Parameters:
            auth_type: Authentication type: APP (client_id/secret) or USER (Oauth2 via Authorization code flow)
            client_id: Client Id of the application, provided by Spotify.
            client_secret: Client secret of the application, provided by Spotify.
            scope: the rights asked given to the app when a USER connection is used. Must be a valid list af scopes. See [https://developer.spotify.com/documentation/web-api/concepts/scopes](https://developer.spotify.com/documentation/web-api/concepts/scopes)
        """
        self._access_token = Access_token(client_id, client_secret)
        self._access_token.load_spotify_credentials()
        self._access_token.load_access_token(auth_type, scope)

    def _get_api_response_with_access_token(self, url: str, params: dict[str, Any]) -> Response:
        # Generic function that returns the json response
        # of an API call using access token
        url = self.__make_url(url, params)
        response = get(url, headers=self._access_token.headers)
        if response.status_code != 200:
            _dict = json.loads(response.content)
            console.print(f"Warning: url:'[link={url}]{url}[/link]'", style=STYLE["NOTICE"])
            console.print(
                f"responded [{response.status_code}] {response.reason} => {_dict['error']['message']}",
                style=STYLE["NOTICE"],
            )
        return response

    def get_artist(self, artist_id: str) -> Artist | None:
        """returns an Artist Object specified by its id<br>
        See: [https://developer.spotify.com/documentation/web-api/reference/get-an-artist](https://developer.spotify.com/documentation/web-api/reference/get-an-artist)

        Parameters:
            artist_id: Spotify id of the artist

        Returns:
            Artist object or None if id does not match an artist
        """
        response = self._get_api_response_with_access_token(api.HTTP_GET_ARTIST, {"id": artist_id})
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
        response = self._get_api_response_with_access_token(
            api.HTTP_GET_SEVERAL_ARTISTS, {"ids": artist_ids}
        )
        return self.__make_artists_list(response.content)

    def get_artist_related_artists(self, artist_id: str) -> list[Artist] | None:
        """returns a list of Artist Objects related to the artist specified by its id<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-an-artists-related-artists](https://developer.spotify.com/documentation/web-api/reference/get-an-artists-related-artists)

        Parameters:
            artist_id: Spotify id of the artist

        Returns:
            list of Artist objects or None if id does not match an artist
        """
        response = self._get_api_response_with_access_token(
            api.HTTP_GET_RELATED_ARTISTS, params={"id": artist_id}
        )
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
            market: An ISO 3166-1 alpha-2 country code. If a country code is specified, only content that is available in that market will be returned. If a valid user access token is specified in the request header, the country associated with the user account will take priority over this parameter.

        Returns:
            list of Tracks objects or None if id does not match an artist
        """
        response = self._get_api_response_with_access_token(
            api.HTTP_GET_ARTIST_TOP_TRACKS, {"id": artist_id, "market": market}
        )
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
        response = self._get_api_response_with_access_token(
            api.HTTP_GET_ARTIST_ALBUMS,
            {
                "id": artist_id,
                "market": market,
                "limit": limit,
                "offset": offset,
                "include_groups": include_groups,
            },
        )
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
        response = self._get_api_response_with_access_token(
            api.HTTP_GET_ALBUM, {"id": album_id, "market": market}
        )
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
        response = self._get_api_response_with_access_token(
            api.HTTP_GET_SEVERAL_ALBUMS, {"ids": album_ids, "market": market}
        )
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
        response = self._get_api_response_with_access_token(
            api.HTTP_GET_ALBUM_TRACKS,
            {"id": album_id, "market": market, "limit": limit, "offset": offset},
        )
        if response.status_code == 200:
            return self.__make_album_tracks(response.content)
        return None

    def get_new_releases(self) -> Navigation:
        """Get a list of new album releases featured in Spotify (shown, for example, on a Spotify player’s “Browse” tab).<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-new-releases](https://developer.spotify.com/documentation/web-api/reference/get-new-releases)

        Returns:
            A Navigation object of Track Objects
        """
        response = self._get_api_response_with_access_token(api.HTTP_GET_NEW_RELEASES, {})
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
        response = self._get_api_response_with_access_token(
            api.HTTP_GET_BROWSE_CATEGORY, {"id": category_id, "locale": locale}
        )
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
        response = self._get_api_response_with_access_token(
            api.HTTP_GET_SEVERAL_BROWSE_CATEGORIES,
            {"locale": locale, "limit": limit, "offset": offset},
        )
        return self.__make_categories_list(response.content)

    def get_show(self, show_id: str, market: str | None = None) -> Show | None:
        """Get Spotify catalog information for a single show identified by its unique Spotify ID.<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-a-show](https://developer.spotify.com/documentation/web-api/reference/get-a-show)

        Parameters:
            show_id: Spotify id of the track

        Returns:
            Show object or None if id does not match a show
        """
        response = self._get_api_response_with_access_token(
            api.HTTP_GET_SHOW, {"id": show_id, "market": market}
        )
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
        response = self._get_api_response_with_access_token(
            api.HTTP_GET_SEVERAL_SHOWS, {"ids": show_ids, "market": market}
        )
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
        response = self._get_api_response_with_access_token(
            api.HTTP_GET_SHOW_EPISODES,
            {"id": show_id, "market": market, "limit": limit, "offset": offset},
        )
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
        response = self._get_api_response_with_access_token(
            api.HTTP_GET_TRACK, {"id": track_id, "market": market}
        )
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
        response = self._get_api_response_with_access_token(
            api.HTTP_GET_SEVERAL_TRACKS, {"ids": track_ids, "market": market}
        )
        return self.__make_tracks_list(response.content)

    def get_track_audio_features(self, track_id: str) -> Audio_features | None:
        """returns a Audio_features Object specified by its ids<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-audio-features](https://developer.spotify.com/documentation/web-api/reference/get-audio-features)

        Parameters:
            track_id: Spotify id of the track

        Returns:
            List of Audio_features object
        """
        response = self._get_api_response_with_access_token(
            api.HTTP_GET_TRACK_AUDIO_FEATURES, {"id": track_id}
        )
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
        response = self._get_api_response_with_access_token(
            api.HTTP_GET_SEVERAL_TRACK_AUDIO_FEATURES, {"ids": track_ids}
        )
        return self.__make_audio_features_list(response.content)

    def get_genres(self) -> set[str]:
        """Retrieve a list of available genres seed parameter values for recommendations.<br>
        Please use the [genres property](0sympyfy.md#sympyfy.Sympyfy.genres), this method is public only to match the Spotify API<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-recommendation-genres](https://developer.spotify.com/documentation/web-api/reference/get-recommendation-genres)

        Returns:
            list of genres seeds. Example: ["alternative","samba"]
        """
        response = self._get_api_response_with_access_token(api.HTTP_GET_GENRES, {})
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
        response = self._get_api_response_with_access_token(api.HTTP_GET_MARKETS, {})
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
        response = self._get_api_response_with_access_token(
            api.HTTP_GET_USER_PROFILE, {"id": user_id}
        )
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
        response = self._get_api_response_with_access_token(
            api.HTTP_GET_USERS_FOLLOW_PLAYLIST, {"id": playlist_id, "ids": user_ids}
        )
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
        params = {"id": playlist_id, "market": market, "fields": fields}
        if additional_types:
            params["additional_types"] = ",".join(additional_types)
        response = self._get_api_response_with_access_token(api.HTTP_GET_PLAYLIST, params)
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
        response = self._get_api_response_with_access_token(
            api.HTTP_GET_PLAYLIST_COVER_IMAGE, {"id": playlist_id}
        )
        if response.status_code == 200:
            return self.__make_playlist_cover_image(response.content)
        return None

    def get_playlists_by_category(
        self, category_id: str, limit: int = 20, offset: int = 0
    ) -> tuple[str, Navigation] | None:
        """Get a list of Spotify playlists tagged with a particular category.<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-playlist-cover](https://developer.spotify.com/documentation/web-api/reference/get-playlist-cover)

        Parameters:
            category_id: The Spotify category ID for the category.
            limit: The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50.
            offset: The index of the first item to return. Default: 0 (the first item). Use with limit to get the next set of items.

        Returns:
            A string containing the localized message of a playlist and a Navigation Object of Playlist Objects.
        """
        response = self._get_api_response_with_access_token(
            api.HTTP_GET_PLAYLISTS_BY_CATEGORY,
            {"id": category_id, "limit": limit, "offset": offset},
        )
        if response.status_code == 200:
            return self.__make_playlists_by_category(response.content)
        return None

    def get_track_recommendations(
        self,
        market: str | None = None,
        limit: int = 20,
        seed_artists: list[str] | None = None,
        seed_genres: list[str] | None = None,
        seed_tracks: list[str] | None = None,
        tunable_track_attributes: dict[str, Any] | None = None,
    ) -> Recommendation:
        """Recommendations are generated based on the available information for a given seed entity and matched against similar artists and tracks. If there is sufficient information about the provided seeds, a list of tracks will be returned together with pool size details.<br>
        For artists and tracks that are very new or obscure there might not be enough data to generate a list of tracks.<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-recommendations](https://developer.spotify.com/documentation/web-api/reference/get-recommendations)

        Parameters:
            market: An ISO 3166-1 alpha-2 country code. If a country code is specified, only content that is available in that market will be returned. If a valid user access token is specified in the request header, the country associated with the user account will take priority over this parameter.
            limit: The target size of the list of recommended tracks. For seeds with unusually small pools or when highly restrictive filtering is applied, it may be impossible to generate the requested number of recommended tracks. Debugging information for such cases is available in the response. Default: 20. Minimum: 1. Maximum: 100.
            seed_artists: A list of Spotify IDs for seed artists. Up to 5 seed values may be provided in any combination of seed_artists, seed_tracks and seed_genres.<br>
                Note: only required if seed_genres and seed_tracks are not set.
            seed_genres: A comma separated list of any genres in the set of available genre seeds. Up to 5 seed values may be provided in any combination of seed_artists, seed_tracks and seed_genres.<br>
                Note: only required if seed_artists and seed_tracks are not set.
            seed_tracks: A comma separated list of Spotify IDs for a seed track. Up to 5 seed values may be provided in any combination of seed_artists, seed_tracks and seed_genres.<br>
                Note: only required if seed_artists and seed_genres are not set.
            tunable_track_attributes: A dictionary of attributes relatives to the track audio features. For each tunable track attribute, a hard floor on the selected track attribute’s value can be provided. See tunable track attributes below for the list of available options.<br>
                The attribute list is: min_acousticness, max_acousticness, target_acousticness, min_danceability, max_danceability, target_danceability, min_duration_ms, max_duration_ms, target_duration_ms, min_energy, max_energy, target_energy, min_instrumentalness, max_instrumentalness, target_instrumentalness, min_key, max_key, target_key, min_liveness, max_liveness, target_liveness, min_loudness, max_loudness, target_loudness, min_mode, max_mode, target_mode, min_popularity, max_popularity, target_popularity, min_speechiness, max_speechiness, target_speechiness, min_tempo, max_tempo, target_tempo, min_time_signature, max_time_signature, target_time_signature, min_valence, max_valence, target_valence<br>
                The explanation of the terms acousticness, danceability ... etc ... can be found in the [Audio_features object Documentation](1structs.md#sympyfy.api_structures.Audio_features).

        Returns:
            A list of recommended Track Objects based the input parameters.
        """
        params = {
            "market": market,
            "limit": limit,
            "tunable_track_attributes": tunable_track_attributes,
        }
        if seed_artists:
            params["seed_artists"] = ",".join(seed_artists)
        if seed_genres:
            params["seed_genres"] = ",".join(seed_genres)
        if seed_tracks:
            params["seed_tracks"] = ",".join(seed_tracks)

        response = self._get_api_response_with_access_token(
            api.HTTP_GET_TRACK_RECOMMENDATIONS, params
        )
        return self.__make_track_recommendations(response.content)

    def get_track_audio_analysis(self, track_id: str) -> Audio_analysis | None:
        """Get a low-level audio analysis for a track in the Spotify catalog. The audio analysis describes the track’s structure and musical content, including rhythm, pitch, and timbre.<br>
        [https://developer.spotify.com/documentation/web-api/reference/get-audio-analysis](https://developer.spotify.com/documentation/web-api/reference/get-audio-analysis)

        Parameters:
            track_id: The Spotify ID for the track.

        Returns:
            An Audio analysis Object
        """
        response = self._get_api_response_with_access_token(
            api.HTTP_GET_TRACK_AUDIO_ANALYSIS,
            {"id": track_id},
        )
        if response.status_code == 200:
            return self.__make_track_audio_analysis(response.content)
        return None

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
        if album.tracks and album.tracks.items:
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
        if navigation.items:
            navigation.items = [Album.model_validate(x) for x in navigation.items]
        return navigation

    def __make_album_tracks(self, json_content: bytes) -> Navigation:
        navigation: Navigation = Navigation.model_validate_json(json_content)
        if navigation.items:
            navigation.items = [Track.model_validate(x) for x in navigation.items]
        return navigation

    def __make_new_releases(self, json_content: bytes) -> Navigation:
        dict_content = json.loads(json_content)
        navigation: Navigation = Navigation.model_validate(dict_content["albums"])
        if navigation.items:
            navigation.items = [Album.model_validate(x) for x in navigation.items]
        return navigation

    def __make_category(self, json_content) -> Category:
        category: Category = Category.model_validate_json(json_content)
        return category

    def __make_categories_list(self, json_content: bytes) -> Navigation:
        dict_content = json.loads(json_content)
        navigation: Navigation = Navigation.model_validate(dict_content["categories"])
        if navigation.items:
            navigation.items = [Category.model_validate(x) for x in navigation.items]
        return navigation

    def __make_show(self, json_content: bytes) -> Show:
        show: Show = Show.model_validate_json(json_content)
        if show.episodes and show.episodes.items:
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
        if navigation.items:
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

    def __make_playlists_by_category(self, json_content: bytes) -> tuple[str, Navigation]:
        dict_content = json.loads(json_content)
        message = dict_content["message"]
        navigation = Navigation.model_validate(dict_content["playlists"])
        navigation.items = [Playlist.model_validate(x) for x in navigation.items]
        return message, navigation

    def __make_track_recommendations(self, json_content: bytes) -> Recommendation:
        recommendation = Recommendation.model_validate_json(json_content)
        return recommendation

    def __make_track_audio_analysis(self, json_content: bytes) -> Audio_analysis:
        audio_analysis = Audio_analysis.model_validate_json(json_content)
        return audio_analysis

    def __make_simple_set(self, json_content: bytes, key: str) -> set[str]:
        dict_content = json.loads(json_content)
        return set(dict_content[key])

    def __make_url(self, base_url: str, param_list: dict[str, Any]) -> str:
        url = base_url
        params = ""

        for param in param_list:
            match param:
                case "id":
                    url = url.replace("{id}", param_list["id"])
                case "ids":
                    url = url.replace("{ids}", "%2C".join(param_list["ids"]))
                case "market":
                    if param_list["market"] and param_list["market"] in self.markets:
                        params += "&market=" + param_list["market"]
                case "limit":
                    limit = param_list["limit"]
                    if limit < 1:
                        limit = 1
                    if limit > 50:
                        limit = 50
                    params += f"&{limit=}"
                case "offset":
                    offset = param_list["offset"]
                    if offset < 0:
                        offset = 0
                    params += f"&{offset=}"
                case "include_groups":
                    param_groups = []
                    for group in param_list["include_groups"]:
                        if group in INCLUDE_GROUPS:
                            param_groups.append(group)
                    if param_groups:
                        params += "&include_groups=" + "%2C".join(param_groups)
                    else:
                        params += "&include_groups=" + "%2C".join(INCLUDE_GROUPS)
                case "tunable_track_attributes":
                    param_attrs = ""
                    for attr in param_list["tunable_track_attributes"]:
                        if attr in TRACKS_ATTRIBUTES:
                            param_attrs += f"&{attr}={param_list['tunable_track_attributes'][attr]}"
                    params += param_attrs
                case _:
                    if param_list[param]:
                        params += f"&{param}={escape(param_list[param])}"

        url = url + params
        # sanitize URL
        if "?" not in url:
            url = url.replace("&", "?", 1)

        return url
