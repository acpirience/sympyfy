"""

test for sympyfy.get_playlist

"""

from sympyfy import Sympyfy


def test_get_playlist() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_playlist = test.get_playlist("2LbyMChvxpn1emaIiDKKnT")

    assert test_playlist and test_playlist.type == "playlist"


def test_get_playlist_with_additional_types() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_playlist = test.get_playlist(
        "2LbyMChvxpn1emaIiDKKnT", additional_types=["track", "episode"]
    )

    assert test_playlist and test_playlist.type == "playlist"


def test_get_unknown_playlist() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_playlist = test.get_playlist("'''")

    assert not test_playlist
