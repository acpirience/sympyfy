"""

test for sympyfy.get_search

"""

from sympyfy import Sympyfy


def test_get_search() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_search = test.get_search(
        q="artist:Fatboy Slim", type=["album", "artist", "playlist", "track", "show", "episode"]
    )

    assert test_search and test_search.albums


def test_get_search_episodes() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_search = test.get_search(
        q="year:2023", type=["episode"]
    )

    assert test_search and test_search.episodes.total > 20


def test_get_search_empty() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_search = test.get_search(
        q="artist:-!xxsz", type=["album", "artist", "playlist", "track", "show", "episode"]
    )

    assert test_search and test_search.albums
    assert test_search and test_search.artists
    assert test_search and test_search.playlists
    assert test_search and test_search.tracks
    assert test_search and test_search.shows
    assert test_search and test_search.episodes

    assert test_search and test_search.artists.total == 0
