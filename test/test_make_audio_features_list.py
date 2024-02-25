"""

test for sympyfy.make_audio_features_list

"""

from sympyfy import Sympyfy


def test_make_audio_features_list() -> None:
    json_content = b'{\n  "audio_features" : [ {\n    "danceability" : 0.582,\n    "energy" : 0.767,\n    "key" : 4,\n    "loudness" : -11.380,\n    "mode" : 0,\n    "speechiness" : 0.0297,\n    "acousticness" : 0.288,\n    "instrumentalness" : 0.0789,\n    "liveness" : 0.0606,\n    "valence" : 0.736,\n    "tempo" : 141.683,\n    "type" : "audio_features",\n    "id" : "3EEd6ldsPat620GVYMEhOP",\n    "uri" : "spotify:track:3EEd6ldsPat620GVYMEhOP",\n    "track_href" : "https://api.spotify.com/v1/tracks/3EEd6ldsPat620GVYMEhOP",\n    "analysis_url" : "https://api.spotify.com/v1/audio-analysis/3EEd6ldsPat620GVYMEhOP",\n    "duration_ms" : 186038,\n    "time_signature" : 4\n  }, {\n    "danceability" : 0.408,\n    "energy" : 0.717,\n    "key" : 6,\n    "loudness" : -7.750,\n    "mode" : 1,\n    "speechiness" : 0.0393,\n    "acousticness" : 0.000578,\n    "instrumentalness" : 0.0599,\n    "liveness" : 0.0827,\n    "valence" : 0.313,\n    "tempo" : 169.213,\n    "type" : "audio_features",\n    "id" : "2fKdsBazcOLLIzDiZUQCih",\n    "uri" : "spotify:track:2fKdsBazcOLLIzDiZUQCih",\n    "track_href" : "https://api.spotify.com/v1/tracks/2fKdsBazcOLLIzDiZUQCih",\n    "analysis_url" : "https://api.spotify.com/v1/audio-analysis/2fKdsBazcOLLIzDiZUQCih",\n    "duration_ms" : 188693,\n    "time_signature" : 4\n  } ]\n}'

    test_audio_features_list = Sympyfy()._Sympyfy__make_audio_features_list(json_content)  # type: ignore

    test_audio_feature_tempo = [x.tempo for x in test_audio_features_list]

    assert 141.683 in test_audio_feature_tempo
    assert 169.213 in test_audio_feature_tempo
