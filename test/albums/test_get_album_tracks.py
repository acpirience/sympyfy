"""

test for sympyfy.get_album_tracks

"""

from sympyfy import Sympyfy


def test_get_album_tracks() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_albums = test.get_album_tracks("2ANVost0y2y52ema1E9xAZ")

    assert test_albums


def test_get_album_tracks_unknown_artist() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_albums = test.get_album_tracks("xyz")

    assert not test_albums
