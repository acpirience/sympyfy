"""

test for common.add_pagination

"""

from sympyfy.common import add_pagination


def test_add_pagination_ok() -> None:
    test = add_pagination(limit=20, offset=20)

    assert test == "&offset=20&limit=20"


def test_add_pagination_limit_ko() -> None:
    test = add_pagination(limit=0, offset=0)
    assert test == "&offset=0&limit=1"

    test = add_pagination(limit=200, offset=0)
    assert test == "&offset=0&limit=50"


def test_add_pagination_offset_ko() -> None:
    test = add_pagination(limit=1, offset=-20)
    assert test == "&offset=0&limit=1"
