"""

test for sympyfy.get_genres
"""

from sympyfy import Sympyfy


def test_get_genres() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_genres = test.get_genres()

    assert "dubstep" in test_genres


def test_genres_property() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_genres = test.genres

    assert "dubstep" in test_genres
