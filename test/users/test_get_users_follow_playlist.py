"""

test for sympyfy.get_users_playlist

"""

from sympyfy import Sympyfy


def test_get_users_follow_playlist() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_user = test.get_users_follow_playlist(
        "3cEYpjA9oz9GiPac4AsH4n", ["jmperezperez", "thelinmichael", "wizzler"]
    )

    assert test_user and test_user == [True, False, False]


def test_get_users_follow_playlist_unknown() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_user = test.get_users_follow_playlist("xyz", ["jmperezperez", "thelinmichael", "wizzler"])

    assert not test_user
