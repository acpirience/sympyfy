"""

test for common.add_market

"""

from sympyfy.common import add_market


def test_add_market_empty() -> None:
    test = add_market(None)

    assert test == ""


def test_add_market_incorrect_country() -> None:
    test = add_market("AZERTY")

    assert test == ""


def test_add_market_correct_country() -> None:
    test = add_market("FR")

    assert test == "?market=FR"
