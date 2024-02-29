"""

test for sympyfy.get_several_shows

"""

from sympyfy import Sympyfy


def test_get_several_show() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_show = test.get_several_shows(["6Ol9sx1lONDxBSffLW9qcZ", "4GC4FMJmYDDrqJI5t8I1Yy"])

    assert test_show
    assert len(test_show) == 2


def test_get_several_show_unknown_show() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_show = test.get_several_shows(["xyz", "abc"])

    assert not test_show
