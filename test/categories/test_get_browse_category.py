"""

test for sympyfy.get_browse_category

"""

from sympyfy import Sympyfy


def test_get_browse_category() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_category = test.get_browse_category("0JQ5DAqbMKFRY5ok2pxXJ0")

    assert test_category and test_category.name == "Cooking & Dining"


def test_get_unknown_category() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_category = test.get_browse_category("xyz")

    assert not test_category
