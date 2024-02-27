"""

test for sympyfy.get_markets
"""

from sympyfy import Sympyfy


def test_get_markets() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_markets = test.get_markets()

    assert "FR" in test_markets


def test_get_markets_property() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_markets = test.markets

    assert "FR" in test_markets
