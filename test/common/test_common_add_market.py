"""

test for common.add_market

"""

from sympyfy.common import add_market


def test_add_market_empty() -> None:
    test = add_market(None, {"FR", "US"})

    assert test == ""


def test_add_market_incorrect_country() -> None:
    test = add_market("AZERTY", {"FR", "US"})

    assert test == ""


def test_add_market_correct_country() -> None:
    test = add_market("FR", {"FR", "US"})

    assert test == "&market=FR"
