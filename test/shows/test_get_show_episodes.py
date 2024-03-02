"""

test for sympyfy.get_show_episodes

"""

from sympyfy import Sympyfy


def test_get_show_episodes() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_show = test.get_show_episodes("6Ol9sx1lONDxBSffLW9qcZ", limit=2)

    assert test_show

    assert test_show.limit == 2
    assert len(test_show.items) == 2


def test_get_show_unknown_show() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_show = test.get_show_episodes("xyz")

    assert not test_show
