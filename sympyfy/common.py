"""

common classes used by other objects

"""

from dataclasses import dataclass
from typing import Any

from sympyfy.isoCountryCodes import ISO3166


@dataclass
class Image:
    url: str
    height: int
    width: int


def value_or_default(key: str, _dict: dict[str, Any], default: Any) -> Any:
    if key in _dict:
        return _dict[key]
    return default


def add_market(market: str | None) -> str:
    if market:
        if market in ISO3166:
            return "?market=" + market
        print("Warning: Wrong market, switching to default")
    return ""
