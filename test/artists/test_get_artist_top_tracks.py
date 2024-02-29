"""

test for sympyfy.get_artist_top_tracks

"""

from sympyfy import Sympyfy


def test_get_artist_top_tracks() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_tracks_list = test.get_artist_top_tracks("5N5tQ9Dx1h8Od7aRmGj7Fi", "US")

    assert test_tracks_list

    test_track_names = [x.name for x in test_tracks_list]

    assert "All We Ever Wanted Was Everything" in test_track_names
    assert "Bela Lugosi's Dead (Official Version)" in test_track_names


def test_get_artist_top_tracks_unknown_artist() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_track_list_artist_ko = test.get_artist_top_tracks("xyz", "US")
    assert not test_track_list_artist_ko

    test_track_list_market_ko = test.get_artist_top_tracks("5N5tQ9Dx1h8Od7aRmGj7Fi", "xyz")
    assert test_track_list_market_ko
