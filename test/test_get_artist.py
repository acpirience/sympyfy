"""

test for sympyfy.get_artist

"""

from sympyfy import Sympyfy


def test_get_known_artist() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_artist = test.get_artist("1GhPHrq36VKCY3ucVaZCfo")

    assert test_artist and test_artist.name == "The Chemical Brothers"
    assert test_artist and "breakbeat" in test_artist.genres


def test_get_unknown_artist() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_artist = test.get_artist("xyz")

    assert not test_artist
