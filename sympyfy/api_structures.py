"""

contains the data structures for the spotify API

"""

from typing import Any, Optional

from pydantic import AliasChoices, BaseModel, Field


class Image(BaseModel):
    """
    Stores the data relative to images of Artists or Albums

    Parameters:
        url (str): The source URL of the image.
        height (int): The image height in pixels.<br>
            Optional, default = None
        width (int): The image width in pixels.<br>
            Optional, default = None
    """

    url: str
    height: int | None = None
    width: int | None = None


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
        items (list[Track]|list[Episode]|list[Playlist_item]|list[Playlist]): list of objects paginated<br>
            Optional, default = None
    """

    href: str
    next: str | None = None
    previous: str | None = None
    limit: int = 20
    offset: int = 0
    total: int
    items: list[Any] | None = None


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


class Bar(BaseModel):
    """
    The time intervals of the bars throughout the track. A bar (or measure) is a segment of time defined as a given number of beats.

    Parameters:
        start (float): The starting point (in seconds) of the time interval.
        duration (float): The duration (in seconds) of the time interval.
        confidence (float): The confidence, from 0.0 to 1.0, of the reliability of the interval. Range: 0 - 1
    """

    start: float
    duration: float
    confidence: float


class Beat(BaseModel):
    """
    The time intervals of beats throughout the track. A beat is the basic time unit of a piece of music; for example, each tick of a metronome. Beats are typically multiples of tatums.

    Parameters:
        start (float): The starting point (in seconds) of the time interval.
        duration (float): The duration (in seconds) of the time interval.
        confidence (float): The confidence, from 0.0 to 1.0, of the reliability of the interval. Range: 0 - 1
    """

    start: float
    duration: float
    confidence: float


class Tatum(BaseModel):
    """
    A tatum represents the lowest regular pulse train that a listener intuitively infers from the timing of perceived musical events (segments).

    Parameters:
        start (float): The starting point (in seconds) of the time interval.
        duration (float): The duration (in seconds) of the time interval.
        confidence (float): The confidence, from 0.0 to 1.0, of the reliability of the interval. Range: 0 - 1
    """

    start: float
    duration: float
    confidence: float


class Section(BaseModel):
    """
    Sections are defined by large variations in rhythm or timbre, e.g. chorus, verse, bridge, guitar solo, etc. Each section contains its own descriptions of tempo, key, mode, time_signature, and loudness.

    Parameters:
        start (float): The starting point (in seconds) of the section.
        duration (float): The duration (in seconds) of the section.
        confidence (float): The confidence, from 0.0 to 1.0, of the reliability of the section's "designation". Range: 0 - 1
        loudness (float): The overall loudness of the section in decibels (dB). Loudness values are useful for comparing relative loudness of sections within tracks.
        tempo (float): The overall estimated tempo of the section in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.
        tempo_confidence (float):The confidence, from 0.0 to 1.0, of the reliability of the tempo. Some tracks contain tempo changes or sounds which don't contain tempo (like pure speech) which would correspond to a low value in this field. Range: 0 - 1
        key (int): The estimated overall key of the section. The values in this field ranging from 0 to 11 mapping to pitches using standard Pitch Class notation (E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on). If no key was detected, the value is -1.
        key_confidence (float): The confidence, from 0.0 to 1.0, of the reliability of the key. Songs with many key changes may correspond to low values in this field. Range: 0 - 1
        mode (int): Indicates the modality (major or minor) of a section, the type of scale from which its melodic content is derived. This field will contain a 0 for "minor", a 1 for "major", or a -1 for no result. Note that the major key (e.g. C major) could more likely be confused with the minor key at 3 semitones lower (e.g. A minor) as both keys carry the same pitches.
        mode_confidence (float): The confidence, from 0.0 to 1.0, of the reliability of the mode. Range: 0 - 1
        time_signature (int): An estimated time signature. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure). The time signature ranges from 3 to 7 indicating time signatures of "3/4", to "7/4". Range: 3 - 7
        time_signature_confidence (float): The confidence, from 0.0 to 1.0, of the reliability of the time_signature. Sections with time signature changes may correspond to low values in this field. Range: 0 - 1
    """

    start: float
    duration: float
    confidence: float
    loudness: float
    tempo: float
    tempo_confidence: float
    key: int
    key_confidence: float
    mode: int
    mode_confidence: float
    time_signature: int
    time_signature_confidence: float


class Segment(BaseModel):
    """
    Each segment contains a roughly conisistent sound throughout its duration.

    Parameters:
        start (float): The starting point (in seconds) of the section.
        duration (float): The duration (in seconds) of the section.
        confidence (float): The confidence, from 0.0 to 1.0, of the reliability of the section's "designation". Range: 0 - 1
        loudness_start (float): The onset loudness of the segment in decibels (dB). Combined with loudness_max and loudness_max_time, these components can be used to describe the "attack" of the segment.
        loudness_max (float): The peak loudness of the segment in decibels (dB). Combined with loudness_start and loudness_max_time, these components can be used to describe the "attack" of the segment.
        loudness_max_time (float): The segment-relative offset of the segment peak loudness in seconds. Combined with loudness_start and loudness_max, these components can be used to desctibe the "attack" of the segment.
        loudness_end (float): The offset loudness of the segment in decibels (dB). This value should be equivalent to the loudness_start of the following segment.
        pitches (list[int]): Pitch content is given by a “chroma” vector, corresponding to the 12 pitch classes C, C#, D to B, with values ranging from 0 to 1 that describe the relative dominance of every pitch in the chromatic scale. For example a C Major chord would likely be represented by large values of C, E and G (i.e. classes 0, 4, and 7).<br>
                Vectors are normalized to 1 by their strongest dimension, therefore noisy sounds are likely represented by values that are all close to 1, while pure tones are described by one value at 1 (the pitch) and others near 0. As can be seen below, the 12 vector indices are a combination of low-power spectrum values at their respective pitch frequencies.

    """

    start: float
    duration: float
    confidence: float
    loudness_start: float
    loudness_max: float
    loudness_max_time: float
    loudness_end: float
    pitches: list[float]


class Audio_analysis_meta(BaseModel):
    """
    Parameters of the audio analysisn how and when the analysis was done.

    Parameters:
        analyzer_version (str): The version of the Analyzer used to analyze this track.
        platform (str): The platform used to read the track's audio data.
        detailed_status (str): A detailed status code for this track. If analysis data is missing, this code may explain why.
        status_code (int): The return code of the analyzer process. 0 if successful, 1 if any errors occurred.
        timestamp (int): The Unix timestamp (in seconds) at which this track was analyzed.
        analysis_time (float): The amount of time taken to analyze this track.
        input_process (str): The method used to read the track's audio data.
    """

    analyzer_version: str | None = None
    platform: str | None = None
    detailed_status: str | None = None
    status_code: int | None = None
    timestamp: int | None = None
    analysis_time: float | None = None
    input_process: str | None = None


class Audio_analysis_properties(BaseModel):
    """
    Various audio properties linked to the whole track.

    Parameters:
        num_samples (int):The exact number of audio samples analyzed from this track. See also analysis_sample_rate.
        duration (float): Length of the track in seconds.
        sample_md5 (str): This field will always contain the empty string.
        offset_seconds (float): An offset to the start of the region of the track that was analyzed. (As the entire track is analyzed, this should always be 0.)
        window_seconds (float): The length of the region of the track was analyzed, if a subset of the track was analyzed. (As the entire track is analyzed, this should always be 0.)
        analysis_sample_rate (int): The sample rate used to decode and analyze this track. May differ from the actual sample rate of this track available on Spotify.
        analysis_channels (int): The number of channels used for analysis. If 1, all channels are summed together to mono before analysis.
        end_of_fade_in (float): The time, in seconds, at which the track's fade-in period ends. If the track has no fade-in, this will be 0.0.
        start_of_fade_out (float): The time, in seconds, at which the track's fade-out period starts. If the track has no fade-out, this should match the track's length.
        loudness (float): The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typically range between -60 and 0 db.
        tempo (float): The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.
        tempo_confidence (float): The confidence, from 0.0 to 1.0, of the reliability of the tempo.
        time_signature (int): An estimated time signature. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure). The time signature ranges from 3 to 7 indicating time signatures of "3/4", to "7/4". Range: 3 - 7
        time_signature_confidence (float): The confidence, from 0.0 to 1.0, of the reliability of the time_signature. Range: 0 - 1
        key (int): The key the track is in. Integers map to pitches using standard Pitch Class notation. E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1. Range: -1 - 11
        key_confidence (float): The confidence, from 0.0 to 1.0, of the reliability of the key. Range: 0 - 1
        mode (int): Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0.
        mode_confidence (float): The confidence, from 0.0 to 1.0, of the reliability of the mode. Range: 0 - 1
        codestring (str): An Echo Nest Musical Fingerprint (ENMFP) codestring for this track.
        code_version (float): A version number for the Echo Nest Musical Fingerprint format used in the codestring field.
        echoprintstring (str): An EchoPrint codestring for this track.
        echoprint_version (float): A version number for the EchoPrint format used in the echoprintstring field.
        synchstring (str): A Synchstring for this track.
        synch_version (float): A version number for the Synchstring used in the synchstring field.
        rhythmstring (str): A Rhythmstring for this track. The format of this string is similar to the Synchstring.
        rhythm_version (float): A version number for the Rhythmstring used in the rhythmstring field.
    """

    num_samples: int
    duration: float
    sample_md5: str
    offset_seconds: float
    window_seconds: float
    analysis_sample_rate: int
    analysis_channels: int
    end_of_fade_in: float
    start_of_fade_out: float
    loudness: float
    tempo: float
    tempo_confidence: float
    time_signature: int
    time_signature_confidence: float
    key: int
    key_confidence: float
    mode: int
    mode_confidence: float
    codestring: str
    code_version: float
    echoprintstring: str
    echoprint_version: float
    synchstring: str
    synch_version: float
    rhythmstring: str
    rhythm_version: float


class Audio_analysis(BaseModel):
    """
    Get a low-level audio analysis for a track in the Spotify catalog. The audio analysis describes the track’s structure and musical content, including rhythm, pitch, and timbre.

    Parameters:
        audio_analysis_meta (Audio_analysis_meta): Audio_analysis_meta Object
        audio_analysis_properties (Audio_analysis_properties): Audio_analysis_properties Object
        bars (list[Bar]): list of Bar Objects
        beats (list[Beat]): list of Beat Objects
        tatums (list[Tatum]): list of Tatum Objects
        sections (list[Section]): list of Section Objects
        segments (list[Segment]): list of Segment Objects

    """

    audio_analysis_meta: Audio_analysis_meta = Field(validation_alias=AliasChoices("meta"))
    audio_analysis_properties: Audio_analysis_properties = Field(
        validation_alias=AliasChoices("track")
    )
    bars: list[Bar]
    beats: list[Beat]
    tatums: list[Tatum]
    sections: list[Section]
    segments: list[Segment]


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
        images (list[Image]): The user's profile image.<br>
            Optional, default = []
    """

    id: str
    display_name: str | None = None
    href: str
    uri: str
    type: str = "user"
    followers: Followers | None = None
    external_urls: dict[str, str] = {}
    images: list[Image] = []


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


class Playlist(BaseModel):
    """
    Get a playlist owned by a Spotify user. Every can be optional since they can be filtered by the 'fields' filter dor the query.<br>
    See [https://developer.spotify.com/documentation/web-api/reference/get-playlist](https://developer.spotify.com/documentation/web-api/reference/get-playlist) for more explanations.

    Parameters:
        id (str): The Spotify ID for the playlist.
        name (str): The name of the playlist.
        owner (User) : The user who owns the playlist
        href (str): A link to the Web API endpoint providing full details of the playlist.
        uri (str): The Spotify URI for the playlist.
        type (str): The object type: "playlist"
        description (str): The playlist description. Only returned for modified, verified playlists,
        followers (Followers): Information about the followers of the playlist.
        snapshot_id (str) : The version identifier for the current playlist. Can be supplied in other requests to target a specific playlist version
        public (bool): The playlist's public/private status: true the playlist is public, false the playlist is private, null the playlist status is not relevant. For more about public/private status, see Working with Playlists
        collaborative (bool): True if the owner allows other users to modify the playlist. otherwise null.
        external_urls (dict[str, str]): Known external URLs for this playlist.
        images (list[Image]): Images for the playlist. The array may be empty or contain up to three images. The images are returned by size in descending order. See Working with Playlists. Note: If returned, the source URL for the image (url) is temporary and will expire in less than a day.
        tracks (Navigation): The tracks of the playlist. A navigation Object of Playlist_item Objects
    """

    id: str = ""
    name: str = ""
    owner: User | None = None
    href: str = ""
    uri: str = ""
    type: str = "playlist"
    description: str = ""
    followers: Followers | None = None
    snapshot_id: str = ""
    public: bool = False
    collaborative: bool | None = None
    external_urls: (dict[str, str]) = {}
    images: list[Image] = []
    tracks: Navigation


class Playlist_item(BaseModel):
    """
    The tracks of the playlist.

    Parameters:
        added_at (str): The date and time the track or episode was added. Note: some very old playlists may return null in this field.<br>
            Optional, default = None
        added_by (User): The Spotify user who added the track or episode. Note: some very old playlists may return null in this field.<br>
            Optional, default = None
        is_local (bool): Whether this track or episode is a local file or not.<br>
            Optional, default = False
        track (Track | Episode): Either a Track object or an Episode Object<br>
            Optional, default = None
    """

    added_at: str | None = None
    added_by: User | None = None
    is_local: bool = False
    track: Track | Episode | None = None


class Seed(BaseModel):
    """
    A recommendation seed objects that give statistics about the search.

    Parameters:
        afterFilteringSize (int): The number of tracks available after min_* and max_* filters have been applied.
        afterRelinkingSize (int): The number of tracks available after relinking for regional availability.
        href (str): A link to the full track or artist data for this seed. For tracks this will be a link to a Track Object. For artists a link to an Artist Object. For genre seeds, this value will be null.<br>
            Optional, default = None (is always None for GENRE)
        id (str): The id used to select this seed. This will be the same as the string used in the seed_artists, seed_tracks or seed_genres parameter.
        initialPoolSize (int): The number of recommended tracks available for this seed.
        type (str): The entity type of this seed. One of "ARTIST", "TRACK" or "GENRE".
    """

    id: str
    href: str | None = None
    type: str
    afterFilteringSize: int
    afterRelinkingSize: int
    initialPoolSize: int


class Recommendation(BaseModel):
    """
    Recommendations are generated based on the available information for a given seed entity and matched against similar artists and tracks. If there is sufficient information about the provided seeds, a list of tracks will be returned together with pool size details.<br>
    For artists and tracks that are very new or obscure there might not be enough data to generate a list of tracks.<br>

    Parameters:
        seeds (list[Seed]): A list of recommendation seed objects.
        tracks (list[Track]): A list of recommended Track Objects.
    """

    seeds: list[Seed]
    tracks: list[Track]
