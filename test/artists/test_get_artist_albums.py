"""

test for sympyfy.get_artist_albums

"""

from sympyfy import Sympyfy


def test_get_artist_albums() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_albums = test.get_artist_albums("7bu3H8JO7d0UbMoVzbo70s")

    assert test_albums


def test_get_artist_albums_unknown_artist() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_albums = test.get_artist_albums("xyz")

    assert not test_albums
