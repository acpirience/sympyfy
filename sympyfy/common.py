"""

common classes used by other objects

"""

from typing import Any

from sympyfy.isoCountryCodes import ISO3166

INCLUDE_GROUPS = ["album", "single", "appears_on", "compilation"]


def value_or_default(key: str, _dict: dict[str, Any], default: Any) -> Any:
    if key in _dict:
        return _dict[key]
    return default


def sanitize(url: str) -> str:
    if "?" in url:
        return url
    return url.replace("&", "?", 1)


def add_market(market: str | None) -> str:
    if market:
        if market in ISO3166:
            return "?market=" + market
        print("Warning: Wrong market, switching to default")
    return ""


def add_pagination(limit: int, offset: int) -> str:
    if limit < 1:
        limit = 1
    if limit > 50:
        limit = 50
    if offset < 0:
        offset = 0

    return f"&{offset=}&{limit=}"


def add_include_groups(groups: list[str]) -> str:
    ret_groups = []
    for group in groups:
        if group in INCLUDE_GROUPS:
            ret_groups.append(group)

    if ret_groups:
        return "&include_groups=" + "%2C".join(ret_groups)
    return "&include_groups=" + "%2C".join(INCLUDE_GROUPS)
