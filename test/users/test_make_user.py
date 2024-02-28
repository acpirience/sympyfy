"""

test for sympyfy.make_user
"""
from sympyfy import Sympyfy


def test_make_user() -> None:
    json_content = b'{\n  "display_name" : "liam",\n  "external_urls" : {\n    "spotify" : "https://open.spotify.com/user/xxx"\n  },\n  "href" : "https://api.spotify.com/v1/users/xxx",\n  "id" : "xxx",\n  "images" : [ {\n    "url" : "https://i.scdn.co/image/ab67757000003b82cbbf8dfe1fe9e0f8c4d86461",\n    "height" : 64,\n    "width" : 64\n  }, {\n    "url" : "https://i.scdn.co/image/ab6775700000ee85cbbf8dfe1fe9e0f8c4d86461",\n    "height" : 300,\n    "width" : 300\n  } ],\n  "type" : "user",\n  "uri" : "spotify:user:xxx",\n  "followers" : {\n    "href" : null,\n    "total" : 23\n  }\n}'

    test_user = Sympyfy()._Sympyfy__make_user(json_content)  # type: ignore

    assert test_user.display_name == "liam"
    assert test_user.followers == 23
