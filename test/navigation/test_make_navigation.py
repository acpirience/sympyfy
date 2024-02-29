"""

test for sympyfy.make_navigation

"""

from sympyfy import Sympyfy


def test_navigation() -> None:
    test_dict = {
        "href": "https://api.spotify.com/v1/shows/6Ol9sx1lONDxBSffLW9qcZ/episodes?offset=0&limit=50",
        "next": "https://api.spotify.com/v1/shows/6Ol9sx1lONDxBSffLW9qcZ/episodes?offset=50&limit=50",
        "previous": None,
        "limit": 50,
        "offset": 0,
        "total": 250,
    }

    test = Sympyfy()._Sympyfy__make_navigation(test_dict)  # type: ignore
    assert test.limit == 50
    assert test.total == 250
