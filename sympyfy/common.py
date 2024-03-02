"""

common classes used by other objects

"""


INCLUDE_GROUPS = ["album", "single", "appears_on", "compilation"]


def sanitize(url: str) -> str:
    if "?" in url:
        return url
    return url.replace("&", "?", 1)


def add_market(market: str | None, markets: set[str]) -> str:
    if market:
        if market in markets:
            return "&market=" + market
        print("Warning: Wrong market, switching to default")
    return ""


def add_url_parameter(param_name: str, param_value: str | None) -> str:
    if param_value:
        return f"&{param_name}={param_value}"
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
