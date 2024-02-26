"""

contains the data structures for the spotify API

"""

from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Image:
    """
    Stores the data relative to images of Artists or Albums

    Parameters:
        url: The source URL of the image.
        height: The image height in pixels.
        width: The image width in pixels.
     """
    url: str
    height: int
    width: int

@dataclass
class Artist:
    """
    Stores the data relative to Artist

    Parameters:
        id: The Spotify ID for the artist.
        name: The name of the artist.
        href: A link to the Web API endpoint providing full details of the artist.
        uri: The Spotify URI for the artist.
        popularity: The popularity of the artist. The value will be between 0 and 100, with 100 being the most popular. The artist's popularity is calculated from the popularity of all the artist's tracks.
        type: The object type. Allowed values: "artist"
        followers: The total number of followers.
        genres: A list of the genres the artist is associated with. If not yet classified, the array is empty.
        external_urls: Known external URLs for this artist.
        images: Images of the artist in various sizes, widest first.
     """
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
    """
    Stores the data relative to Track

    Parameters:
        id: The Spotify ID for the track.
        name: The name of the track.
        href: A link to the Web API endpoint providing full details of the track.
        uri: The Spotify URI for the track.
        popularity: The popularity of the track. The value will be between 0 and 100, with 100 being the most popular.
        type: The object type: "track". Allowed values: "track"
        preview_url: A link to a 30 second preview (MP3 format) of the track. Can be null
        disc_number: The disc number (usually 1 unless the album consists of more than one disc).
        track_number: The number of the track. If an album has several discs, the track number is the number on the specified disc.
        duration_ms: The track length in milliseconds.
        explicit: Whether or not the track has explicit lyrics ( true = yes it does; false = no it does not OR unknown).
        is_local: Whether or not the track is from a local file.
        is_playable: Part of the response when Track Relinking is applied. If true, the track is playable in the given market. Otherwise false.
        external_ids: Known external IDs for the track.
        external_urls: Known external URLs for this track.
        artists: The artists who performed the track.
        available_markets: A list of the countries in which the track can be played, identified by their ISO 3166-1 alpha-2 code.
        album: The album on which the track appears.
        linked_from: Part of the response when Track Relinking is applied, and the requested track has been replaced with different track. The track in the linked_from object contains information about the originally requested track.
        restrictions: Included in the response when a content restriction is applied.
     """
    id: str
    name: str
    href: str
    uri: str
    popularity: int
    type: str
    preview_url: str | None
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
    linked_from: Optional[dict[str, Any]]
    restrictions: str


@dataclass
class Audio_features:
    """
    Stores the data relative to the Album

    Parameters:
        id: The Spotify ID for the track.
        track_href: A link to the Web API endpoint providing full details of the track.
        uri: The Spotify URI for the track.
        analysis_url: A URL to access the full audio analysis of this track. An access token is required to access this data.
        type: The object type. Allowed values: "audio_features"
        key: The key the track is in. Integers map to pitches using standard Pitch Class notation. E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1. Range: -1 - 11
        mode: Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0.
        time_signature: An estimated time signature. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure). The time signature ranges from 3 to 7 indicating time signatures of "3/4", to "7/4". Range: 3 - 7
        duration_ms: The duration of the track in milliseconds.
        danceability: Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
        energy: Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.
        loudness: The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typically range between -60 and 0 db.
        speechiness: Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks.
        acousticness: A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic. Range: 0 - 1
        instrumentalness: Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.
        liveness: Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.
        valence: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry). Range: 0 - 1
        tempo: The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.
    """
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
    """
    Stores the data relative to the Album

    Parameters:
        id: The Spotify ID of the album.
        name: The name of the album. In case of an album takedown, the value may be an empty string.
        href: A link to the Web API endpoint providing full details of the album.
        uri: The Spotify URI for the album.
        popularity: The popularity of the album. The value will be between 0 and 100, with 100 being the most popular.
        type: The object type. Allowed values: "album"
        album_type: The type of the album. Allowed values: "album", "single", "compilation"
        album_group: This field describes the relationship between the artist and the album. Allowed values: "album", "single", "compilation", "appears_on"
        release_date: The date the album was first released.
        release_date_precision: The precision with which release_date value is known. Allowed values: "year", "month", "day"
        available_markets: The markets in which the album is available: ISO 3166-1 alpha-2 country codes. NOTE: an album is considered available in a market when at least 1 of its tracks is available in that market.
        genres: A list of the genres the album is associated with. If not yet classified, the array is empty.
        label: The label associated with the album.
        external_urls: Known external URLs for this album.
        external_ids: Known external IDs for the album.
        copyrights: The copyright statements of the album.
        images: The cover art for the album in various sizes, widest first.
        artists: The artists of the album.
        tracks_total: The total number of items available to return.
        tracks: The tracks of the album.
    """
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
    """
    Stores the data needed to navigate paginated content

    Parameters:
        href: A link to the Web API endpoint returning the full result of the request
        next: URL to the next page of items. ( null if none)
        previous: URL to the previous page of items. ( null if none)
        limit: The maximum number of items in the response (as set in the query or by default).
        offset: The offset of the items returned (as set in the query or by default)
        total: The total number of items available to return.
    """
    href: str
    next: str | None
    previous: str | None
    limit: int
    offset: int
    total: int
