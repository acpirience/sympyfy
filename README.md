## SymPyfy ##
![GitHub top language](https://img.shields.io/github/languages/top/acpirience/sympyfy?style=flat) ![GitHub License](https://img.shields.io/github/license/acpirience/sympyfy?style=flat) ![GitHub last commit](https://img.shields.io/github/last-commit/acpirience/sympyfy) ![GitHub repo size](https://img.shields.io/github/repo-size/acpirience/sympyfy?style=flat)


A spotify python library.

The project is still ongoing, see [Documentation](https://acpirience.github.io/sympyfy/) for update on the Spotify API implementation status

### Pre-requisite ###
A pre-requisite for using this library is to get a Spotify access token: [https://developer.spotify.com/documentation/web-api/tutorials/getting-started#request-an-access-token](https://developer.spotify.com/documentation/web-api/tutorials/getting-started#request-an-access-token).

Sympyfy needs either:  

- The client_id and client_secret passed as parameters of the `load_credentials()` method.
- The client_id and client_secret environment variables present.
- a .env file creating those variables

Exemple:
```
client_id="MY_CLIENT_ID"
client_secret="MY_CLIENT_SECRET"
```

### Usage ###
``` py
from sympyfy import Sympyfy
from rich.console import Console

console = Console()

spotify = Sympyfy()
spotify.load_credentials()
    
artist = spotify.get_artist("1GhPHrq36VKCY3ucVaZCfo")
    
console.print(artist)
```
```
Artist(
    id='1GhPHrq36VKCY3ucVaZCfo',
    name='The Chemical Brothers',
    href='https://api.spotify.com/v1/artists/1GhPHrq36VKCY3ucVaZCfo',
    uri='spotify:artist:1GhPHrq36VKCY3ucVaZCfo',
    popularity=61,
    type='artist',
    followers=Followers(href=None, total=2013511),
    genres=[
        'alternative dance',
        'big beat',
        'breakbeat',
        'electronica',
        'rave',
        'trip hop'
    ],
    external_urls={
        'spotify': 'https://open.spotify.com/artist/1GhPHrq36VKCY3ucVaZCfo'
    },
    images=[
        Image(
            url='https://i.scdn.co/image/ab6761610000e5ebae05213e52565bfd7e7489
b3',
            height=640,
            width=640
        ),
        Image(
            url='https://i.scdn.co/image/ab67616100005174ae05213e52565bfd7e7489
b3',
            height=320,
            width=320
        ),
        Image(
            url='https://i.scdn.co/image/ab6761610000f178ae05213e52565bfd7e7489
b3',
            height=160,
            width=160
        )
    ]
)
```