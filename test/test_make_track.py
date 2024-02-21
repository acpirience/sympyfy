"""

test for sympyfy.make_track

"""
from sympyfy import Sympyfy


def test_make_track() -> None:
    test = Sympyfy()

    json_content = b'{\n  "album" : {\n    "album_type" : "album",\n    "artists" : [ {\n      "external_urls" : {\n        "spotify" : "https://open.spotify.com/artist/3zunDAtRDg7kflREzWAhxl"\n      },\n      "href" : "https://api.spotify.com/v1/artists/3zunDAtRDg7kflREzWAhxl",\n      "id" : "3zunDAtRDg7kflREzWAhxl",\n      "name" : "Eels",\n      "type" : "artist",\n      "uri" : "spotify:artist:3zunDAtRDg7kflREzWAhxl"\n    } ],\n    "available_markets" : [ "AR", "AU", "AT", "BE", "BO", "BR", "BG", "CA", "CL", "CO", "CR", "CY", "CZ", "DK", "DO", "DE", "EC", "EE", "SV", "FI", "FR", "GR", "GT", "HN", "HK", "HU", "IS", "IE", "IT", "LV", "LT", "LU", "MY", "MT", "MX", "NL", "NZ", "NI", "NO", "PA", "PY", "PE", "PH", "PL", "PT", "SG", "SK", "ES", "SE", "CH", "TW", "TR", "UY", "US", "GB", "AD", "LI", "MC", "ID", "JP", "TH", "VN", "RO", "IL", "ZA", "SA", "AE", "BH", "QA", "OM", "KW", "EG", "MA", "DZ", "TN", "LB", "JO", "PS", "IN", "BY", "KZ", "MD", "UA", "AL", "BA", "HR", "ME", "MK", "RS", "SI", "KR", "BD", "PK", "LK", "GH", "KE", "NG", "TZ", "UG", "AG", "AM", "BS", "BB", "BZ", "BT", "BW", "BF", "CV", "CW", "DM", "FJ", "GM", "GE", "GD", "GW", "GY", "HT", "JM", "KI", "LS", "LR", "MW", "MV", "ML", "MH", "FM", "NA", "NR", "NE", "PW", "PG", "WS", "SM", "ST", "SN", "SC", "SL", "SB", "KN", "LC", "VC", "SR", "TL", "TO", "TT", "TV", "VU", "AZ", "BN", "BI", "KH", "CM", "TD", "KM", "GQ", "SZ", "GA", "GN", "KG", "LA", "MO", "MR", "MN", "NP", "RW", "TG", "UZ", "ZW", "BJ", "MG", "MU", "MZ", "AO", "CI", "DJ", "ZM", "CD", "CG", "IQ", "LY", "TJ", "VE", "ET", "XK" ],\n    "external_urls" : {\n      "spotify" : "https://open.spotify.com/album/2C2XdewxdarvJoW1kmUbtk"\n    },\n    "href" : "https://api.spotify.com/v1/albums/2C2XdewxdarvJoW1kmUbtk",\n    "id" : "2C2XdewxdarvJoW1kmUbtk",\n    "images" : [ {\n      "height" : 640,\n      "url" : "https://i.scdn.co/image/ab67616d0000b273d1f1e9631fa6529a056e9c4e",\n      "width" : 640\n    }, {\n      "height" : 300,\n      "url" : "https://i.scdn.co/image/ab67616d00001e02d1f1e9631fa6529a056e9c4e",\n      "width" : 300\n    }, {\n      "height" : 64,\n      "url" : "https://i.scdn.co/image/ab67616d00004851d1f1e9631fa6529a056e9c4e",\n      "width" : 64\n    } ],\n    "name" : "Souljacker",\n    "release_date" : "2002-01-01",\n    "release_date_precision" : "day",\n    "total_tracks" : 16,\n    "type" : "album",\n    "uri" : "spotify:album:2C2XdewxdarvJoW1kmUbtk"\n  },\n  "artists" : [ {\n    "external_urls" : {\n      "spotify" : "https://open.spotify.com/artist/3zunDAtRDg7kflREzWAhxl"\n    },\n    "href" : "https://api.spotify.com/v1/artists/3zunDAtRDg7kflREzWAhxl",\n    "id" : "3zunDAtRDg7kflREzWAhxl",\n    "name" : "Eels",\n    "type" : "artist",\n    "uri" : "spotify:artist:3zunDAtRDg7kflREzWAhxl"\n  } ],\n  "available_markets" : [ "AR", "AU", "AT", "BE", "BO", "BR", "BG", "CA", "CL", "CO", "CR", "CY", "CZ", "DK", "DO", "DE", "EC", "EE", "SV", "FI", "FR", "GR", "GT", "HN", "HK", "HU", "IS", "IE", "IT", "LV", "LT", "LU", "MY", "MT", "MX", "NL", "NZ", "NI", "NO", "PA", "PY", "PE", "PH", "PL", "PT", "SG", "SK", "ES", "SE", "CH", "TW", "TR", "UY", "US", "GB", "AD", "LI", "MC", "ID", "JP", "TH", "VN", "RO", "IL", "ZA", "SA", "AE", "BH", "QA", "OM", "KW", "EG", "MA", "DZ", "TN", "LB", "JO", "PS", "IN", "BY", "KZ", "MD", "UA", "AL", "BA", "HR", "ME", "MK", "RS", "SI", "KR", "BD", "PK", "LK", "GH", "KE", "NG", "TZ", "UG", "AG", "AM", "BS", "BB", "BZ", "BT", "BW", "BF", "CV", "CW", "DM", "FJ", "GM", "GE", "GD", "GW", "GY", "HT", "JM", "KI", "LS", "LR", "MW", "MV", "ML", "MH", "FM", "NA", "NR", "NE", "PW", "PG", "WS", "SM", "ST", "SN", "SC", "SL", "SB", "KN", "LC", "VC", "SR", "TL", "TO", "TT", "TV", "VU", "AZ", "BN", "BI", "KH", "CM", "TD", "KM", "GQ", "SZ", "GA", "GN", "KG", "LA", "MO", "MR", "MN", "NP", "RW", "TG", "UZ", "ZW", "BJ", "MG", "MU", "MZ", "AO", "CI", "DJ", "ZM", "CD", "CG", "IQ", "LY", "TJ", "VE", "ET", "XK" ],\n  "disc_number" : 1,\n  "duration_ms" : 194706,\n  "explicit" : false,\n  "external_ids" : {\n    "isrc" : "USDW10110359"\n  },\n  "external_urls" : {\n    "spotify" : "https://open.spotify.com/track/6Ft7UiAv5SCfK7ZkqVmOCQ"\n  },\n  "href" : "https://api.spotify.com/v1/tracks/6Ft7UiAv5SCfK7ZkqVmOCQ",\n  "id" : "6Ft7UiAv5SCfK7ZkqVmOCQ",\n  "is_local" : false,\n  "name" : "Souljacker Part I",\n  "popularity" : 45,\n  "preview_url" : "https://p.scdn.co/mp3-preview/a766c0beec60e25ca6506b3bd3e8e796f2e070ba?cid=ab95b5368d394475a7ed703547b2175c",\n  "track_number" : 5,\n  "type" : "track",\n  "uri" : "spotify:track:6Ft7UiAv5SCfK7ZkqVmOCQ"\n}'

    test_track = test.make_track(json_content)

    assert test_track.name == "Souljacker Part I"
    assert test_track.type == "track"

    assert len(test_track.artists) == 1
    assert test_track.artists[0].name == "Eels"