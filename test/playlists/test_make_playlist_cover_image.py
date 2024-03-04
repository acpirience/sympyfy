"""

test for sympyfy.make_playlist_cover_image
"""
from sympyfy import Sympyfy


def test_make_playlist_cover_image() -> None:
    json_content = b'[ {\n  "height" : 640,\n  "url" : "https://i.scdn.co/image/ab67616d0000b2734f6d78b7fb2ba87ed33fcd7e",\n  "width" : 640\n} ]'

    test_playlist = Sympyfy()._Sympyfy__make_playlist_cover_image(json_content)  # type: ignore

    assert test_playlist
    assert len(test_playlist) == 1
    assert test_playlist[0].width == 640
