"""

test for sympyfy.make_users_follow_playlist
"""
from sympyfy import Sympyfy


def test_make_users_follow_playlist() -> None:
    json_content = b"[ true, false, false ]"

    test = Sympyfy()._Sympyfy__make_users_follow_playlist(json_content)  # type: ignore

    assert test == [True, False, False]
