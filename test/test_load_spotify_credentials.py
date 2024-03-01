"""

test for sympyfy._get_spotify_credentials

"""

import os

from sympyfy import Sympyfy


def test_env_variables() -> None:
    os.environ["client_id"] = "123"
    os.environ["client_secret"] = "456"

    test = Sympyfy()
    test._load_spotify_credentials()

    assert test._spotify_credentials == {"client_id": "123", "client_secret": "456"}


def test_method_parameters() -> None:
    test = Sympyfy()
    test._load_spotify_credentials(client_id="123", client_secret="456")

    assert test._spotify_credentials == {"client_id": "123", "client_secret": "456"}


def test_env_file_content() -> None:
    os.environ.pop("client_id", None)
    os.environ.pop("client_secret", None)

    test = Sympyfy()
    test._load_spotify_credentials()

    assert "client_id" in test._spotify_credentials
    assert "client_secret" in test._spotify_credentials


def test_env_file_credentials() -> None:
    test = Sympyfy()
    test.load_credentials()

    assert "client_id" in test._spotify_credentials
    assert "client_secret" in test._spotify_credentials

    assert test._access_token.token
