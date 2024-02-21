"""

test for sympyfy.make_artists_list

"""

from sympyfy import Sympyfy


def test_make_artists_list() -> None:
    test = Sympyfy()

    json_content = b'{\n  "artists" : [ {\n    "external_urls" : {\n      "spotify" : "https://open.spotify.com/artist/4lYtGx5NZQJHsMyhHc5iz3"\n    },\n    "followers" : {\n      "href" : null,\n      "total" : 455675\n    },\n    "genres" : [ "garage rock", "gothabilly", "post-punk", "psychobilly", "punk" ],\n    "href" : "https://api.spotify.com/v1/artists/4lYtGx5NZQJHsMyhHc5iz3",\n    "id" : "4lYtGx5NZQJHsMyhHc5iz3",\n    "images" : [ {\n      "height" : 712,\n      "url" : "https://i.scdn.co/image/fc6b731da9ccf21380f2c32a37a825b8b6e41fc8",\n      "width" : 999\n    }, {\n      "height" : 456,\n      "url" : "https://i.scdn.co/image/e9d56abd96718369e0b4addcf2cce6b3e8156d5f",\n      "width" : 640\n    }, {\n      "height" : 142,\n      "url" : "https://i.scdn.co/image/fe97cfdd0fedcac25df0f9e60f09fcef0ec05376",\n      "width" : 199\n    }, {\n      "height" : 46,\n      "url" : "https://i.scdn.co/image/878ae3eddf6187f64b9191040d17e458a2f43d31",\n      "width" : 64\n    } ],\n    "name" : "The Cramps",\n    "popularity" : 54,\n    "type" : "artist",\n    "uri" : "spotify:artist:4lYtGx5NZQJHsMyhHc5iz3"\n  }, {\n    "external_urls" : {\n      "spotify" : "https://open.spotify.com/artist/5N5tQ9Dx1h8Od7aRmGj7Fi"\n    },\n    "followers" : {\n      "href" : null,\n      "total" : 817321\n    },\n    "genres" : [ "alternative rock", "dark wave", "dream pop", "gothic rock", "industrial rock", "new wave", "post-punk", "uk post-punk" ],\n    "href" : "https://api.spotify.com/v1/artists/5N5tQ9Dx1h8Od7aRmGj7Fi",\n    "id" : "5N5tQ9Dx1h8Od7aRmGj7Fi",\n    "images" : [ {\n      "height" : 686,\n      "url" : "https://i.scdn.co/image/9676688ae196b8abf4ed89ce6620a7ad04027095",\n      "width" : 1000\n    }, {\n      "height" : 439,\n      "url" : "https://i.scdn.co/image/7cfcb4df12bb3a2442e240e06cf901859b1046ea",\n      "width" : 640\n    }, {\n      "height" : 137,\n      "url" : "https://i.scdn.co/image/57fd269a0e234d409318ae0d41b7e4b6ffa0991a",\n      "width" : 200\n    }, {\n      "height" : 44,\n      "url" : "https://i.scdn.co/image/25c8070cffb44e28bc6614dfd311657b628f5912",\n      "width" : 64\n    } ],\n    "name" : "Bauhaus",\n    "popularity" : 53,\n    "type" : "artist",\n    "uri" : "spotify:artist:5N5tQ9Dx1h8Od7aRmGj7Fi"\n  }, {\n    "external_urls" : {\n      "spotify" : "https://open.spotify.com/artist/0Zy4ncr8h1jd7Nzr9946fD"\n    },\n    "followers" : {\n      "href" : null,\n      "total" : 321683\n    },\n    "genres" : [ "gothic rock", "industrial rock", "new wave", "post-punk", "punk", "uk post-punk" ],\n    "href" : "https://api.spotify.com/v1/artists/0Zy4ncr8h1jd7Nzr9946fD",\n    "id" : "0Zy4ncr8h1jd7Nzr9946fD",\n    "images" : [ {\n      "height" : 640,\n      "url" : "https://i.scdn.co/image/ab6761610000e5ebb27c2f14d0deaac56f64c1f4",\n      "width" : 640\n    }, {\n      "height" : 320,\n      "url" : "https://i.scdn.co/image/ab67616100005174b27c2f14d0deaac56f64c1f4",\n      "width" : 320\n    }, {\n      "height" : 160,\n      "url" : "https://i.scdn.co/image/ab6761610000f178b27c2f14d0deaac56f64c1f4",\n      "width" : 160\n    } ],\n    "name" : "Killing Joke",\n    "popularity" : 47,\n    "type" : "artist",\n    "uri" : "spotify:artist:0Zy4ncr8h1jd7Nzr9946fD"\n  } ]\n}'

    test_artist_list = test.make_artists_list(json_content)

    test_artists_names = [x.name for x in test_artist_list]

    assert "The Cramps" in test_artists_names
    assert "Bauhaus" in test_artists_names
    assert "Killing Joke" in test_artists_names
