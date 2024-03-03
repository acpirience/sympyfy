"""

contains Urls for the spotify API

"""

HTTP_GET_APP_TOKEN = "https://accounts.spotify.com/api/token"
HTTP_API_ROOT = "https://api.spotify.com/v1"

# albums
HTTP_GET_ALBUM = HTTP_API_ROOT + "/albums/{id}"
HTTP_GET_SEVERAL_ALBUMS = HTTP_API_ROOT + "/albums?ids={ids}"
HTTP_GET_ALBUM_TRACKS = HTTP_API_ROOT + "/albums/{id}/tracks"
HTTP_GET_NEW_RELEASES = HTTP_API_ROOT + "/browse/new-releases"

# artists
HTTP_GET_ARTIST = HTTP_API_ROOT + "/artists/{id}"
HTTP_GET_SEVERAL_ARTISTS = HTTP_API_ROOT + "/artists?ids={ids}"
HTTP_GET_ARTIST_ALBUMS = HTTP_API_ROOT + "/artists/{id}/albums"
HTTP_GET_ARTIST_TOP_TRACKS = HTTP_API_ROOT + "/artists/{id}/top-tracks"
HTTP_GET_RELATED_ARTISTS = HTTP_API_ROOT + "/artists/{id}/related-artists"

# categories
HTTP_GET_BROWSE_CATEGORY = HTTP_API_ROOT + "/browse/categories/{id}"
HTTP_GET_SEVERAL_BROWSE_CATEGORIES = HTTP_API_ROOT + "/browse/categories"

# episodes
# HTTP_GET_EPISODE = HTTP_API_ROOT + "/episodes/{id}"
# HTTP_GET_SEVERAL_EPISODES = HTTP_API_ROOT + "/episodes?ids={ids}"


# genres
HTTP_GET_GENRES = HTTP_API_ROOT + "/recommendations/available-genre-seeds"

# markets
HTTP_GET_MARKETS = HTTP_API_ROOT + "/markets"

# playlists
# HTTP_GET_PLAYLIST = HTTP_API_ROOT + "/playlists/{id}"

# shows
HTTP_GET_SHOW = HTTP_API_ROOT + "/shows/{id}"
HTTP_GET_SEVERAL_SHOWS = HTTP_API_ROOT + "/shows?ids={ids}"
HTTP_GET_SHOW_EPISODES = HTTP_API_ROOT + "/shows/{id}/episodes"


# tracks
HTTP_GET_TRACK = HTTP_API_ROOT + "/tracks/{id}"
HTTP_GET_SEVERAL_TRACKS = HTTP_API_ROOT + "/tracks?ids={ids}"
HTTP_GET_TRACK_AUDIO_FEATURES = HTTP_API_ROOT + "/audio-features/{id}"
HTTP_GET_SEVERAL_TRACK_AUDIO_FEATURES = HTTP_API_ROOT + "/audio-features?ids={ids}"

# Users
HTTP_GET_USER_PROFILE = HTTP_API_ROOT + "/users/{id}"
HTTP_GET_USERS_FOLLOW_PLAYLIST = HTTP_API_ROOT + "/playlists/{id}/followers/contains?ids={ids}"
