"""

test for sympyfy.load_spotify_credentials

"""

import os

from sympyfy.access_token import Access_token


def test_load_spotify_credentials_parameters() -> None:
    test = Access_token("ID", "SECRET")
    test.load_spotify_credentials()

    assert test._client_id == "ID"
    assert test._client_secret == "SECRET"


def test_load_spotify_credentials_environment() -> None:
    test = Access_token()
    os.environ["client_id"] = "ID"
    os.environ["client_secret"] = "SECRET"
    test.load_spotify_credentials()

    assert test._client_id == "ID"
    assert test._client_secret == "SECRET"


def test_load_spotify_credentials_from_env_file() -> None:
    test = Access_token()
    test.load_spotify_credentials()

    assert test._client_id != ""
    assert test._client_secret != ""
