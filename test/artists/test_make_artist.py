"""

test for sympyfy.make_artist

"""
from sympyfy import Sympyfy
from sympyfy.api_structures import Image


def test_make_artist() -> None:
    json_content = b'{\n  "external_urls" : {\n    "spotify" : "https://open.spotify.com/artist/1GhPHrq36VKCY3ucVaZCfo"\n  },\n  "followers" : {\n    "href" : null,\n    "total" : 2004610\n  },\n  "genres" : [ "alternative dance", "big beat", "breakbeat", "electronica", "rave", "trip hop" ],\n  "href" : "https://api.spotify.com/v1/artists/1GhPHrq36VKCY3ucVaZCfo",\n  "id" : "1GhPHrq36VKCY3ucVaZCfo",\n  "images" : [ {\n    "height" : 640,\n    "url" : "https://i.scdn.co/image/ab6761610000e5ebae05213e52565bfd7e7489b3",\n    "width" : 640\n  }, {\n    "height" : 320,\n    "url" : "https://i.scdn.co/image/ab67616100005174ae05213e52565bfd7e7489b3",\n    "width" : 320\n  }, {\n    "height" : 160,\n    "url" : "https://i.scdn.co/image/ab6761610000f178ae05213e52565bfd7e7489b3",\n    "width" : 160\n  } ],\n  "name" : "The Chemical Brothers",\n  "popularity" : 61,\n  "type" : "artist",\n  "uri" : "spotify:artist:1GhPHrq36VKCY3ucVaZCfo"\n}'

    test_artist = Sympyfy()._Sympyfy__make_artist(json_content)  # type: ignore

    assert test_artist.name == "The Chemical Brothers"
    assert test_artist.popularity == 61
    assert "breakbeat" in test_artist.genres
    assert "rave" in test_artist.genres
    assert (
        Image("https://i.scdn.co/image/ab6761610000e5ebae05213e52565bfd7e7489b3", 640, 640)
        in test_artist.images
    )
