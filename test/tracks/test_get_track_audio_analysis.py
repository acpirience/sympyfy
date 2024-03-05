"""

test for sympyfy.get_track_audio_analysis

"""

from sympyfy import Sympyfy


def test_get_track_audio_analysis() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_audio = test.get_track_audio_analysis("2IQ61J0AFfjnxBm4lQEU0W")

    assert test_audio and test_audio.audio_analysis_meta.analyzer_version == "4.0.0"


def test_get_track_audio_analysis_unknown() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_audio = test.get_track_audio_analysis("xyz")

    assert not test_audio
