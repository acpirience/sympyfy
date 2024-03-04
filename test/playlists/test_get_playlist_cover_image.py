"""

test for sympyfy.get_playlist_cover_image

"""

from sympyfy import Sympyfy


def test_get_playlist_cover_image() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_playlist = test.get_playlist_cover_image("2LbyMChvxpn1emaIiDKKnT")

    assert test_playlist


def test_get_unknown_playlist() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_playlist = test.get_playlist_cover_image("'''")

    assert not test_playlist
