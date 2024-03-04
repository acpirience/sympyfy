"""

test for sympyfy.get_playlists_by_category

"""

from sympyfy import Sympyfy


def test_get_playlist_cover_image() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_playlist = test.get_playlists_by_category("0JQ5DAqbMKFCuoRTxhYWow", limit=3)

    assert test_playlist


def test_get_unknown_playlist() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_playlist = test.get_playlists_by_category("'''")

    assert not test_playlist
