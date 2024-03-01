"""

test for access_token

"""

from datetime import datetime, timedelta

from sympyfy.tokens.access_token import Access_token


def test_access_token() -> None:
    test_json = b'{"access_token":"test","token_type":"Bearer","expires_in":3600}'
    test = Access_token(test_json)

    assert test.token == "test"
    assert test.is_valid()
    assert test.expiry > datetime.now() + timedelta(seconds=3000)


def test_access_repr() -> None:
    test = Access_token(b'{"access_token":"test","token_type":"Bearer","expires_in":3600}')
    test.expiry = datetime(2024, 2, 14, 0, 0, 1)

    assert str(test) == ("(Token:'test', Expiry:'2024-02-14 00:00:01')")
