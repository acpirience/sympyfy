"""

test for sympyfy.get_several_track_audio_features

"""

from sympyfy import Sympyfy


def test_get_several_track_audio_features_ok() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_audio_features_list = test.get_several_track_audio_features(
        ["3EEd6ldsPat620GVYMEhOP", "2fKdsBazcOLLIzDiZUQCih"]
    )

    assert test_audio_features_list

    test_duration_ms = [x.duration_ms for x in test_audio_features_list]

    assert 186038 in test_duration_ms
    assert 188693 in test_duration_ms


def test_get_several_track_audio_features_one_unknown() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_audio_features_list = test.get_several_track_audio_features(
        ["3EEd6ldsPat620GVYMEhOP", "xyz"]
    )

    assert test_audio_features_list
    assert len(test_audio_features_list) == 1

    test_duration_ms = [x.duration_ms for x in test_audio_features_list]

    assert 186038 in test_duration_ms
    assert 188693 not in test_duration_ms


def test_get_several_track_audio_features_no_tracks() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_audio_features_list = test.get_several_track_audio_features(["xyz"])

    assert test_audio_features_list == []
