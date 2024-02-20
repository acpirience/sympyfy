"""

test for sympyfy.get_track

"""

from sympyfy import Sympyfy


def test_get_known_track() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_track = test.get_track("6Ft7UiAv5SCfK7ZkqVmOCQ")

    assert test_track and test_track.name == "Souljacker Part I"
    assert test_track and test_track.id == "6Ft7UiAv5SCfK7ZkqVmOCQ"


def test_get_unknown_track() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_track = test.get_track("xyz")

    assert not test_track
