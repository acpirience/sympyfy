"""

contains Urls for the spotify API

"""

HTTP_GET_APP_TOKEN = "https://accounts.spotify.com/api/token"
HTTP_API_ROOT = "https://api.spotify.com/v1"

# artists
HTTP_GET_ARTIST = HTTP_API_ROOT + "/artists/{id}"
HTTP_GET_SEVERAL_ARTISTS = HTTP_API_ROOT + "/artists?ids={ids}"
HTTP_GET_RELATED_ARTISTS = HTTP_API_ROOT + "/artists/{id}/related-artists"

# tracks
HTTP_GET_TRACK = HTTP_API_ROOT + "/tracks/{id}"
HTTP_GET_SEVERAL_TRACKS = HTTP_API_ROOT + "/tracks?ids={ids}"
HTTP_GET_TRACK_AUDIO_FEATURES = HTTP_API_ROOT + "/audio-features/{id}"

# albums
HTTP_GET_ALBUM = HTTP_API_ROOT + "/albums/{id}"
HTTP_GET_SEVERAL_ALBUMS = HTTP_API_ROOT + "/albums?ids={ids}"
HTTP_GET_ARTIST_TOP_TRACKS = HTTP_API_ROOT + "/artists/{id}/top-tracks"
