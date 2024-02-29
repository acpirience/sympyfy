"""

test for sympyfy.get_show

"""

from sympyfy import Sympyfy


def test_get_show() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_show = test.get_show("6Ol9sx1lONDxBSffLW9qcZ")

    assert test_show


def test_get_show_unknown_show() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_show = test.get_show("xyz")

    assert not test_show
