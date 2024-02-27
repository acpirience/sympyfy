"""

test for sympyfy.make_category

"""
from sympyfy import Sympyfy


def test_make_category() -> None:
    json_content = b'{"href":"https://api.spotify.com/v1/browse/categories/0JQ5DAqbMKFRY5ok2pxXJ0","id":"0JQ5DAqbMKFRY5ok2pxXJ0","icons":[{"height":274,"url":"https://t.scdn.co/media/original/dinner_1b6506abba0ba52c54e6d695c8571078_274x274.jpg","width":274}],"name":"Cooking & Dining"}'

    test_category = Sympyfy()._Sympyfy__make_category(json_content)  # type: ignore

    assert test_category.name == "Cooking & Dining"
    assert len(test_category.icons) == 1
