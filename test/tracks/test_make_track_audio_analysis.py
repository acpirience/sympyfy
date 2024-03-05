"""

test for sympyfy.make_track_audio_analysis

"""
from sympyfy import Sympyfy


def test_make_track_audio_analysis() -> None:

    test_audio = Sympyfy()._Sympyfy__make_track_audio_analysis(json_content)  # type: ignore

    assert test_audio.audio_analysis_meta.analyzer_version == "4.0.0"
    assert test_audio.audio_analysis_properties.num_samples == 11971823
    assert len(test_audio.bars) == 373