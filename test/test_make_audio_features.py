"""

test for sympyfy.make_audio_features

"""
from sympyfy import Sympyfy


def test_make_make_audio_features() -> None:
    json_content = b'{\n  "danceability" : 0.602,\n  "energy" : 0.752,\n  "key" : 9,\n  "loudness" : -5.489,\n  "mode" : 1,\n  "speechiness" : 0.0618,\n  "acousticness" : 0.0107,\n  "instrumentalness" : 0.232,\n  "liveness" : 0.172,\n  "valence" : 0.113,\n  "tempo" : 100.929,\n  "type" : "audio_features",\n  "id" : "6Ft7UiAv5SCfK7ZkqVmOCQ",\n  "uri" : "spotify:track:6Ft7UiAv5SCfK7ZkqVmOCQ",\n  "track_href" : "https://api.spotify.com/v1/tracks/6Ft7UiAv5SCfK7ZkqVmOCQ",\n  "analysis_url" : "https://api.spotify.com/v1/audio-analysis/6Ft7UiAv5SCfK7ZkqVmOCQ",\n  "duration_ms" : 194707,\n  "time_signature" : 4\n}'

    test_track = Sympyfy()._Sympyfy__make_audio_features(json_content)  # type: ignore

    assert test_track.type == "audio_features"
    assert test_track.time_signature == 4
