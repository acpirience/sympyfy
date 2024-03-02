"""

contains the data structures for the spotify API

"""

from typing import Any, Optional

from pydantic import BaseModel


class Image(BaseModel):
    """
    Stores the data relative to images of Artists or Albums

    Parameters:
        url (str): The source URL of the image.
        height (int): The image height in pixels.
        width (int): The image width in pixels.
    """

    url: str
    height: int
    width: int


class Followers(BaseModel):
    """
    Information about the followers of the artist or user.

    parameters:
        href (str): This will always be set to null, as the Web API does not support it at the moment.<br>
            Optional, default = None
        total (int): The total number of followers.
    """

    href: str | None = None
    total: int


class Artist(BaseModel):
    """
    Stores the data relative to Artist

    Parameters:
        id (str): The Spotify ID for the artist.
        name (str): The name of the artist.
        href (str): A link to the Web API endpoint providing full details of the artist.
        uri (str): The Spotify URI for the artist.
        popularity (int): The popularity of the artist. The value will be between 0 and 100, with 100 being the most popular. The artist's popularity is calculated from the popularity of all the artist's tracks.
        type (str): The object type. Allowed values: "artist"
        followers (Followers): The total number of followers.<br>
            Optional, default = None
        genres (list[str]): A list of the genres the artist is associated with. If not yet classified, the array is empty.<br>
            Optional, default = []
        external_urls (dict[str, str]): Known external URLs for this artist.<br>
            Optional, default = {}
        images (list[Image]): Images of the artist in various sizes, widest first.<br>
            Optional, default = []
    """

    id: str
    name: str
    href: str
    uri: str
    popularity: int = 0
    type: str = "artist"
    followers: Followers | None = None
    genres: list[str] = []
    external_urls: dict[str, str] = {}
    images: list[Image] = []


class Track(BaseModel):
    """
    Stores the data relative to Track

    Parameters:
        id (str): The Spotify ID for the track.
        name (str): The name of the track.
        href (str): A link to the Web API endpoint providing full details of the track.
        uri (str): The Spotify URI for the track.
        popularity (int): The popularity of the track. The value will be between 0 and 100, with 100 being the most popular.
        type (str): The object type: "track". Allowed values: "track"
        preview_url (str): A link to a 30 second preview (MP3 format) of the track. Can be null<br>
            Optional, default = None
        disc_number (int): The disc number (usually 1 unless the album consists of more than one disc).
        track_number (int): The number of the track. If an album has several discs, the track number is the number on the specified disc.
        duration_ms (int): The track length in milliseconds.
        explicit (bool): Whether or not the track has explicit lyrics ( true = yes it does; false = no it does not OR unknown).
        is_local (bool): Whether or not the track is from a local file.
        is_playable (bool): Part of the response when Track Relinking is applied. If true, the track is playable in the given market. Otherwise false.
        external_ids (dict[str, str]): Known external IDs for the track.<br>
            Optional, default = {}
        external_urls (dict[str, str]): Known external URLs for this track.<br>
            Optional, default = {}
        artists (list[Artist]): The artists who performed the track.<br>
            Optional, default = []
        available_markets (list[str]]): A list of the countries in which the track can be played, identified by their ISO 3166-1 alpha-2 code.<br>
            Optional, default = []
        album (Album): The album on which the track appears.<br>
            Optional, default = None
        linked_from (dict[str, Any]): Part of the response when Track Relinking is applied, and the requested track has been replaced with different track. The track in the linked_from object contains information about the originally requested track.<br>
            Optional, default = None
        restrictions (dict[str, str]): Included in the response when a content restriction is applied.<br>
            Optional, default = {}
    """

    id: str
    name: str
    href: str
    uri: str
    popularity: int = 0
    type: str = "track"
    preview_url: str | None = None
    disc_number: int = 1
    track_number: int = 1
    duration_ms: int = 0
    explicit: bool = False
    is_local: bool = False
    is_playable: bool = True
    external_ids: dict[str, str] = {}
    external_urls: dict[str, str] = {}
    artists: list[Artist] = []
    available_markets: list[str] = []
    album: Optional["Album"] = None
    linked_from: Optional[dict[str, Any]] = None
    restrictions: dict[str, str] = {}


class Navigation(BaseModel):
    """
    Stores the data needed to navigate paginated content

    Parameters:
        href (str): A link to the Web API endpoint returning the full result of the request
        next (str): URL to the next page of items. ( null if none)<br>
            Optional, default = None
        previous (str): URL to the previous page of items. ( null if none)<br>
            Optional, default = None
        limit (int): The maximum number of items in the response (as set in the query or by default).
        offset (int): The offset of the items returned (as set in the query or by default)
        total (int): The total number of items available to return.
        items (list[Any]): list of objects paginated
    """

    href: str
    next: str | None = None
    previous: str | None = None
    limit: int = 20
    offset: int = 0
    total: int
    items: list[Any]


class Audio_features(BaseModel):
    """
    Stores the data relative to the Album

    Parameters:
        id (str): The Spotify ID for the track.
        track_href (str): A link to the Web API endpoint providing full details of the track.
        uri (str): The Spotify URI for the track.
        analysis_url (str): A URL to access the full audio analysis of this track. An access token is required to access this data.<br>
            Optional, default = None
        type (str): The object type. Allowed values: "audio_features"
        key (int): The key the track is in. Integers map to pitches using standard Pitch Class notation. E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1. Range: -1 - 11<br>
            Optional, default = None
        mode (int): Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0.<br>
            Optional, default = None
        time_signature (int): An estimated time signature. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure). The time signature ranges from 3 to 7 indicating time signatures of "3/4", to "7/4". Range: 3 - 7<br>
            Optional, default = None
        duration_ms (int): The duration of the track in milliseconds.
        danceability (float): Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.<br>
            Optional, default = None
        energy (float): Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.<br>
            Optional, default = None
        loudness (float): The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typically range between -60 and 0 db.<br>
            Optional, default = None
        speechiness (float): Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks.<br>
            Optional, default = None
        acousticness (float): A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic. Range: 0 - 1<br>
            Optional, default = None
        instrumentalness (float): Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.<br>
            Optional, default = None
        liveness (float): Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.<br>
            Optional, default = None
        valence (float): A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry). Range: 0 - 1<br>
            Optional, default = None
        tempo (float): The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.<br>
            Optional, default = None
    """

    id: str
    track_href: str
    uri: str
    analysis_url: str | None = None
    type: str = "audio_features"
    key: int | None = None
    mode: int | None = None
    time_signature: int | None = None
    duration_ms: int = 0
    danceability: float | None = None
    energy: float | None = None
    loudness: float | None = None
    speechiness: float | None = None
    acousticness: float | None = None
    instrumentalness: float | None = None
    liveness: float | None = None
    valence: float | None = None
    tempo: float | None = None


class Album(BaseModel):
    """
    Stores the data relative to the Album

    Parameters:
        id (str): The Spotify ID of the album.
        name (str): The name of the album. In case of an album takedown, the value may be an empty string.
        href (str): A link to the Web API endpoint providing full details of the album.
        uri (str): The Spotify URI for the album.
        popularity (int): The popularity of the album. The value will be between 0 and 100, with 100 being the most popular.
        type (str): The object type. Allowed values: "album"
        album_type (str): The type of the album. Allowed values: "album", "single", "compilation"
        album_group (str): This field describes the relationship between the artist and the album. Allowed values: "album", "single", "compilation", "appears_on"<br>
            Optional, default = None
        release_date (str): The date the album was first released.
        release_date_precision (str): The precision with which release_date value is known. Allowed values: "year", "month", "day"
        available_markets (list[str]): The markets in which the album is available: ISO 3166-1 alpha-2 country codes. NOTE: an album is considered available in a market when at least 1 of its tracks is available in that market.<br>
            Optional, default = []
        genres (list[str]): A list of the genres the album is associated with. If not yet classified, the array is empty.<br>
            Optional, default = []
        label (str): The label associated with the album.
        external_urls (dict[str, str]): Known external URLs for this album.<br>
            Optional, default = {}
        external_ids (dict[str, str]): Known external IDs for the album.<br>
            Optional, default = {}
        copyrights (list[dict[str, str]]): The copyright statements of the album.<br>
            Optional, default = []
        restrictions (dict[str, str]): Included in the response when a content restriction is applied.<br>
            Optional, default = {}
        images (list[Image]): The cover art for the album in various sizes, widest first.<br>
            Optional, default = []
        artists (list[Artist]): The artists of the album.
        total_tracks (int): The total number of items available to return.
        tracks (Navigation): The tracks of the album in a Navigation Object<br>
            Optional, default = None
    """

    id: str
    name: str
    href: str
    uri: str
    popularity: int = 0
    type: str = "album"
    album_type: str
    album_group: str | None = None
    release_date: str
    release_date_precision: str
    available_markets: list[str] = []
    genres: list[str] = []
    label: str = ""
    external_urls: dict[str, str] = {}
    external_ids: dict[str, str] = {}
    copyrights: list[dict[str, str]] = []
    restrictions: dict[str, str] = {}
    images: list[Image] = []
    artists: list[Artist]
    total_tracks: int
    tracks: Navigation | None = None


class Category(BaseModel):
    """
    Get a single category used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab).

    Parameters:
        id (str): The Spotify category ID of the category.
        name (str): The name of the category.
        href (str): A link to the Web API endpoint returning full details of the category.
        icons (list[Image]): The category icon, in various sizes.
    """

    id: str
    name: str
    href: str
    icons: list[Image]


class User(BaseModel):
    """
    Get public profile information about a Spotify user.

    Parameters:
        id (str): The user's Spotify user ID.
        display_name (str): The name displayed on the user's profile. null if not available.<br>
            Optional, default = None
        href (str): A link to the Web API endpoint for this user.
        uri (str): The Spotify URI for this user.
        type (str): The object type. Allowed values: "user"
        followers (Followers): Information about the followers of this user.<br>
            Optional, default = None
        external_urls (dict[str, str]): Known public external URLs for this user.<br>
            Optional, default = {}
        images (list[Image]): The user's profile image.
    """

    id: str
    display_name: str | None = None
    href: str
    uri: str
    type: str = "user"
    followers: Followers | None = None
    external_urls: dict[str, str] = {}
    images: list[Image]


class Resume_point(BaseModel):
    """
    The user's most recent position in the episode. Set if the supplied access token is a user token and has the scope 'user-read-playback-position'.

    parameters:
        fully_played (bool): Whether or not the episode has been fully played by the user.
        resume_position_ms (int): The user's most recent position in the episode in milliseconds.
    """

    fully_played: bool = True
    resume_position_ms: int = 0


class Episode(BaseModel):
    """
    Get Spotify catalog information for a single show.

    Parameters:
        id (str): The Spotify ID for the episode.
        name (str): The name of the episode.
        href (str): A link to the Web API endpoint providing full details of the episode.
        uri (str): The Spotify URI for the episode.
        type (str): The object type. Allowed values: "episode"
        description (str): A description of the episode. HTML tags are stripped away from this field, use html_description field in case HTML tags are needed.
        html_description (str): A description of the episode. This field may contain HTML tags.
        audio_preview_url (str): A URL to a 30 second preview (MP3 format) of the episode. null if not available.
        release_date (str): The date the episode was first released, for example "1981-12-15". Depending on the precision, it might be shown as "1981" or "1981-12".
        release_date_precision (str): The precision with which release_date value is known. Allowed values: "year", "month", "day"
        duration_ms (int): The episode length in milliseconds.
        explicit (bool): Whether or not the episode has explicit content (true = yes it does; false = no it does not OR unknown).
        is_externally_hosted (bool): True if the episode is hosted outside of Spotify's CDN.
        is_playable (bool): True if the episode is playable in the given market. Otherwise false.
        languages (list[str]): A list of the languages used in the episode, identified by their ISO 639-1 code.
        restrictions (list[str]): Included in the response when a content restriction is applied.<br>
            Optional, default = {}
        external_urls (dict[str, str]):External URLs for this episode.<br>
            Optional, default = {}
        images (list[Image]): The cover art for the episode in various sizes, widest first.
        resume_point (Resume_point): The user's most recent position in the episode. Set if the supplied access token is a user token and has the scope 'user-read-playback-position'.<br>
            Optional, default = None
    """

    id: str
    name: str
    href: str
    uri: str
    type: str = "episode"
    description: str
    html_description: str
    audio_preview_url: str
    release_date: str
    release_date_precision: str
    duration_ms: int
    explicit: bool
    is_externally_hosted: bool
    is_playable: bool
    languages: list[str]
    restrictions: dict[str, str] = {}
    external_urls: dict[str, str] = {}
    images: list[Image] = []
    resume_point: Resume_point | None = None


class Show(BaseModel):
    """
    Get Spotify catalog information for a single show.

    Parameters:
        id (str): The Spotify ID for the show.
        name (str): The name of the show.
        href (str): A link to the Web API endpoint providing full details of the show.
        uri (str): The Spotify URI for the show.
        type (str): The object type. Allowed values: "show"
        media_type (str): The media type of the show.
        publisher (str): The publisher of the show.
        description (str): A description of the show. HTML tags are stripped away from this field, use html_description field in case HTML tags are needed.
        html_description (str): A description of the show. This field may contain HTML tags.
        total_episodes (int): The total number of episodes in the show.
        available_markets (list[str]): A list of the countries in which the show can be played, identified by their ISO 3166-1 alpha-2 code.
        explicit (bool): Whether or not the show has explicit content (true = yes it does; false = no it does not OR unknown).
        is_externally_hosted (bool): True if all of the shows episodes are hosted outside of Spotify's CDN. This field might be null in some cases.
        languages (list[str]): A list of the languages used in the show, identified by their ISO 639 code.
        external_urls (dict[str, str]): External URLs for this show.<br>
            Optional, default = {}
        copyrights (list[dict[str, str]]): The copyright statements of the show.<br>
            Optional, default = []
        images (list[Image]): The cover art for the show in various sizes, widest first.<br>
            Optional, default = []
        episodes (Navigation]: The episodes of the show in a Navigation Object<br>
            Optional, default = None
    """

    id: str
    name: str
    href: str
    uri: str
    type: str = "show"
    media_type: str
    publisher: str
    description: str
    html_description: str
    total_episodes: int
    available_markets: list[str]
    explicit: bool
    is_externally_hosted: bool
    languages: list[str]
    external_urls: dict[str, str] = {}
    copyrights: list[dict[str, str]] = []
    images: list[Image] = []
    episodes: Navigation | None = None
