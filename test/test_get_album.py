"""

test for sympyfy.get_album

"""

from sympyfy import Sympyfy


def test_get_known_album() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_album = test.get_album("2ANVost0y2y52ema1E9xAZ")

    assert test_album and test_album.name == "Thriller"
    assert test_album and test_album.id == "2ANVost0y2y52ema1E9xAZ"


def test_get_unknown_album() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_track = test.get_album("xyz")

    assert not test_track
