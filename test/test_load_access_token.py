"""

test for sympyfy._load_access_token

"""

import os

import pytest

from sympyfy import Sympyfy


def test_load_access_token_system_exits() -> None:
    os.environ["client_id"] = "123"
    os.environ["client_secret"] = "456"

    test = Sympyfy()
    test._load_spotify_credentials()

    # pytest magic found in https://medium.com/python-pandemonium/testing-sys-exit-with-pytest-10c6e5f7726f
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        test._load_access_token()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1
