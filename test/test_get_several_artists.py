"""

test for sympyfy.get_several_artists

"""

from sympyfy import Sympyfy


def test_get_known_artists() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_artist_list = test.get_several_artists(
        ["5N5tQ9Dx1h8Od7aRmGj7Fi", "0Zy4ncr8h1jd7Nzr9946fD"]
    )

    assert test_artist_list

    test_artists_names = [x.name for x in test_artist_list]

    assert "The Cramps" not in test_artists_names
    assert "Bauhaus" in test_artists_names
    assert "Killing Joke" in test_artists_names


def test_get_unknown_artist() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_artist_list = test.get_several_artists(["5N5tQ9Dx1h8Od7aRmGj7Fi", "xyz"])

    assert test_artist_list
    assert len(test_artist_list) == 1

    test_artists_names = [x.name for x in test_artist_list]

    assert "Bauhaus" in test_artists_names
