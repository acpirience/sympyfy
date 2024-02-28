"""

test for sympyfy.get_user

"""

from sympyfy import Sympyfy


def test_get_user() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_user = test.get_user_profile("xxx")

    assert test_user and test_user.type == "user"


def test_get_unknown_user() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_user = test.get_user_profile("'''")

    assert not test_user
