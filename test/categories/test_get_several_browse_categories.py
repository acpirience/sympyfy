"""

test for sympyfy.get_several_browse_categories

"""

from sympyfy import Sympyfy


def test_get_several_categories() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_cat = test.get_several_browse_categories()

    assert test_cat
