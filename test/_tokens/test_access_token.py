"""

test for sympyfy.access_token

"""

from sympyfy.access_token import Access_token


def test_access_token() -> None:
    test = Access_token("ID", "SECRET")
    assert str(test) == f"(Token:'', Expiry:'{test.expiry}')"
