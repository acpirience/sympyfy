"""

test for common.value_orèdefault

"""

from sympyfy.common import value_or_default


def test_value_or_default_ok() -> None:
    test = value_or_default("key", {"key": "ok"}, "ko")

    assert test == "ok"


def test_value_or_default_ko() -> None:
    test = value_or_default("keys", {"key": "ok"}, "ko")

    assert test == "ko"
