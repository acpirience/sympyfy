"""

test for sympyfy.get_artist_related_artists

"""

from sympyfy import Sympyfy


def test_get_artist_related_artists() -> None:
    spotify = Sympyfy()
    spotify.load_credentials()

    test_artist_list = spotify.get_artist_related_artists("5N5tQ9Dx1h8Od7aRmGj7Fi")

    assert test_artist_list

    test_artists_ids = [x.id for x in test_artist_list]

    assert "4HxBVyHaUa60eCSsJWxwWR" in test_artists_ids
    assert "7zeHJIIfNStVfxlbT72UwY" in test_artists_ids


def test_get_artist_related_artists_unknow() -> None:
    spotify = Sympyfy()
    spotify.load_credentials()

    test_artist_list = spotify.get_artist_related_artists("zzz")

    assert not test_artist_list
