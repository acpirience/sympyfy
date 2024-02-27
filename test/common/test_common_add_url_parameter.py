"""

test for common.add_url_parameter

"""

from sympyfy.common import add_url_parameter


def test_add_url_parameter() -> None:
    test = add_url_parameter("test", "tested")

    assert test == "&test=tested"


def test_test_add_url_parameter_no_value() -> None:
    test = add_url_parameter("test", None)

    assert test == ""
