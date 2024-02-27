"""

test for sympyfy.get_new_releases

"""

from sympyfy import Sympyfy


def test_get_new_releases() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_tracks = test.get_new_releases()

    assert test_tracks
