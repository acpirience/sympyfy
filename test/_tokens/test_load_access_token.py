"""

test for sympyfy.load_access_token

"""

import os

import pytest

from sympyfy.tokens.access_token import ACCESS_TOKEN_FILE, Access_token


def test_load_access_token_bad_credentials() -> None:
    test = Access_token("ID", "SECRET")
    test.load_spotify_credentials()

    if os.path.isfile(ACCESS_TOKEN_FILE):
        os.remove(ACCESS_TOKEN_FILE)

    # pytest magic found in https://medium.com/python-pandemonium/testing-sys-exit-with-pytest-10c6e5f7726f
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        test.load_access_token()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1


def test_load_access_token_good_credentials() -> None:
    test = Access_token()
    test.load_spotify_credentials()
    test.load_access_token()

    assert os.path.isfile(ACCESS_TOKEN_FILE)
    assert test.is_valid()


def test_load_access_token_cache_expired() -> None:
    test = Access_token()
    test.load_spotify_credentials()
    test.load_access_token()

    with open(ACCESS_TOKEN_FILE, "wb") as test_file:
        test_file.write(
            b'{"access_token": "BQB8xcxqNTd3gThWdJOIhvtzB5Ogao109tNOF0opLWzQXPapvOAJVprApi7MF-SfwAGILCYrG96s_PWzP6oQVe94dZnnP7foMgYpMq9_f2OLDjnL-5Q", "expire_date": "2001-01-01T01:01:01.344651"}'
        )

    test.load_access_token()
    assert test.is_valid()
