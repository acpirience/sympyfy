"""

test for sympyfy.get_track_audio_features

"""

from sympyfy import Sympyfy


def test_get_track_audio_features() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_track = test.get_track_audio_features("6Ft7UiAv5SCfK7ZkqVmOCQ")

    assert test_track and test_track.type == "audio_features"
    assert test_track and test_track.time_signature == 4


def test_get_unknown_track() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_track = test.get_track_audio_features("xyz")

    assert not test_track
