"""

test for _get_spotify_credentials

"""

import os

from sympyfy import Sympyfy


def test_env_variables() -> None:
    os.environ["client_id"] = "123"
    os.environ["client_secret"] = "456"

    test = Sympyfy()

    assert test._spotify_credentials == {"client_id": "123", "client_secret": "456"}


def test_env_file() -> None:
    os.environ.pop("client_id", None)
    os.environ.pop("client_secret", None)

    test = Sympyfy()
    assert "client_id" in test._spotify_credentials
    assert "client_secret" in test._spotify_credentials
