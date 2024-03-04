"""

test for sympyfy.make_playlists_by_category
"""
from sympyfy import Sympyfy


def test_make_playlists_by_category() -> None:
    json_content = b'{"message":"Sleep","playlists":{"href":"https://api.spotify.com/v1/browse/categories/0JQ5DAqbMKFCuoRTxhYWow/playlists?offset=0&limit=3","items":[{"collaborative":false,"description":"Gentle Ambient piano to help you fall asleep. ","external_urls":{"spotify":"https://open.spotify.com/playlist/37i9dQZF1DWZd79rJ6a7lp"},"href":"https://api.spotify.com/v1/playlists/37i9dQZF1DWZd79rJ6a7lp","id":"37i9dQZF1DWZd79rJ6a7lp","images":[{"height":null,"url":"https://i.scdn.co/image/ab67706f0000000281722192322800ae99c2ed06","width":null}],"name":"Sleep","owner":{"display_name":"Spotify","external_urls":{"spotify":"https://open.spotify.com/user/spotify"},"href":"https://api.spotify.com/v1/users/spotify","id":"spotify","type":"user","uri":"spotify:user:spotify"},"primary_color":"#ffffff","public":true,"snapshot_id":"Zd5tuAAAAACzsQNWOne0nU0JhLRtPry/","tracks":{"href":"https://api.spotify.com/v1/playlists/37i9dQZF1DWZd79rJ6a7lp/tracks","total":275},"type":"playlist","uri":"spotify:playlist:37i9dQZF1DWZd79rJ6a7lp"},{"collaborative":false,"description":"Ten hours long continuous white noise to help you relax and let go. ","external_urls":{"spotify":"https://open.spotify.com/playlist/37i9dQZF1DWUZ5bk6qqDSy"},"href":"https://api.spotify.com/v1/playlists/37i9dQZF1DWUZ5bk6qqDSy","id":"37i9dQZF1DWUZ5bk6qqDSy","images":[{"height":null,"url":"https://i.scdn.co/image/ab67706f00000002e3c324443862abeb46220f00","width":null}],"name":"White Noise 10 Hours","owner":{"display_name":"Spotify","external_urls":{"spotify":"https://open.spotify.com/user/spotify"},"href":"https://api.spotify.com/v1/users/spotify","id":"spotify","type":"user","uri":"spotify:user:spotify"},"primary_color":"#ffffff","public":true,"snapshot_id":"Zd4l/wAAAAAH0pvBanE6EDPKHZyOOWXo","tracks":{"href":"https://api.spotify.com/v1/playlists/37i9dQZF1DWUZ5bk6qqDSy/tracks","total":214},"type":"playlist","uri":"spotify:playlist:37i9dQZF1DWUZ5bk6qqDSy"},{"collaborative":false,"description":"Le sommeil, c\'est la sant\xc3\xa9, alors laissez-vous bercer.","external_urls":{"spotify":"https://open.spotify.com/playlist/37i9dQZF1DX6RUdhus57oC"},"href":"https://api.spotify.com/v1/playlists/37i9dQZF1DX6RUdhus57oC","id":"37i9dQZF1DX6RUdhus57oC","images":[{"height":null,"url":"https://i.scdn.co/image/ab67706f000000029f096ba60bf2adafc6b1f9d1","width":null}],"name":"Douce nuit","owner":{"display_name":"Spotify","external_urls":{"spotify":"https://open.spotify.com/user/spotify"},"href":"https://api.spotify.com/v1/users/spotify","id":"spotify","type":"user","uri":"spotify:user:spotify"},"primary_color":"#ffffff","public":true,"snapshot_id":"ZRZBywAAAABSoUs5f3Csat1slluN1aCM","tracks":{"href":"https://api.spotify.com/v1/playlists/37i9dQZF1DX6RUdhus57oC/tracks","total":48},"type":"playlist","uri":"spotify:playlist:37i9dQZF1DX6RUdhus57oC"}],"limit":3,"next":"https://api.spotify.com/v1/browse/categories/0JQ5DAqbMKFCuoRTxhYWow/playlists?offset=3&limit=3","offset":0,"previous":null,"total":56}}'

    test_playlist = Sympyfy()._Sympyfy__make_playlists_by_category(json_content)  # type: ignore

    assert test_playlist
    message, navigation = test_playlist
    assert message == "Sleep"

    assert navigation.limit == 3
    assert len(navigation.items) == 3
