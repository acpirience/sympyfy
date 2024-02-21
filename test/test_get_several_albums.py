"""

test for sympyfy.get_several_albums

"""

from sympyfy import Sympyfy


def test_get_known_albums() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_albums_list = test.get_several_albums(
        ["2ANVost0y2y52ema1E9xAZ", "3ExyKxlUkqD41I8tQumMDF", "2seoHZbHe4S2fOHRA5Lba9"]
    )

    assert test_albums_list

    test_albums_names = [x.name for x in test_albums_list]

    assert "The Undertones" in test_albums_names
    assert "Thriller" in test_albums_names
    assert "Barbie" not in test_albums_names


def test_get_unknown_albums() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_albums_list = test.get_several_albums(["2ANVost0y2y52ema1E9xAZ", "xyz"])

    assert test_albums_list
    assert len(test_albums_list) == 1

    assert "Thriller" in test_albums_list[0].name
