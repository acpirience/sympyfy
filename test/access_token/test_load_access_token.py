"""

test for sympyfy.load_access_token

"""

import os
from datetime import datetime

import pytest

from sympyfy.access_token import ACCESS_TOKEN_FILE, Access_token, Auth_type


def test_load_access_token_bad_credentials() -> None:
    test = Access_token("ID", "SECRET")
    test.load_spotify_credentials()

    if os.path.isfile(ACCESS_TOKEN_FILE):
        os.rename(ACCESS_TOKEN_FILE, ACCESS_TOKEN_FILE + "_TEST")

    # pytest magic found in https://medium.com/python-pandemonium/testing-sys-exit-with-pytest-10c6e5f7726f
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        test.load_access_token(Auth_type.APP)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1

    os.rename(ACCESS_TOKEN_FILE + "_TEST", ACCESS_TOKEN_FILE)


def test_load_access_token_user_auth_without_scope() -> None:
    test = Access_token()
    test.load_spotify_credentials()

    # pytest magic found in https://medium.com/python-pandemonium/testing-sys-exit-with-pytest-10c6e5f7726f
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        test.load_access_token(Auth_type.USER)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1


def test_load_access_token_good_credentials() -> None:
    test = Access_token()
    test.load_spotify_credentials()
    test.load_access_token(Auth_type.APP)

    assert os.path.isfile(ACCESS_TOKEN_FILE)
    assert test.is_valid()


def test_load_access_token_cache_expired() -> None:
    test = Access_token()
    test.load_spotify_credentials()
    test.load_access_token(Auth_type.APP)

    with open(ACCESS_TOKEN_FILE, "wb") as test_file:
        test_file.write(
            b'{"access_token": "BQB8xcxqNTd3gThWdJOIhvtzB5Ogao109tNOF0opLWzQXPapvOAJVprApi7MF-SfwAGILCYrG96s_PWzP6oQVe94dZnnP7foMgYpMq9_f2OLDjnL-5Q", "expire_date": "2001-01-01T01:01:01.344651"}'
        )

    test.load_access_token(Auth_type.APP)
    assert test.is_valid()


def test_load_access_token_cache_expired_during_a_session() -> None:
    test = Access_token()
    test.load_spotify_credentials()
    test.load_access_token(Auth_type.APP)

    test._expiry = datetime.today()
    assert not test.is_valid()

    _ = test.headers

    assert not test.is_valid()
