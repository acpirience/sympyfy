# Home


###Pre-requisite
A pre-requisite for using this library is to get a Spotify access token: [https://developer.spotify.com/documentation/web-api/tutorials/getting-started#request-an-access-token](https://developer.spotify.com/documentation/web-api/tutorials/getting-started#request-an-access-token).

Sympyfy needs either:  

- The client_id and client_secret environment variables present.
- a .env file creating those variables

Exemple:
```
client_id="MY_CLIENT_ID"
client_secret="MY_CLIENT_SECRET"
```

###Usage
``` py title="USAGE"
from sympyfy import Sympyfy
import pprint

spotify = Sympyfy()
spotify.load_credentials()
    
artist = spotify.get_artist("1GhPHrq36VKCY3ucVaZCfo")
    
pprint.pprint(artist)
```
```
Artist(id='1GhPHrq36VKCY3ucVaZCfo',
       name='The Chemical Brothers',
       href='https://api.spotify.com/v1/artists/1GhPHrq36VKCY3ucVaZCfo',
       uri='spotify:artist:1GhPHrq36VKCY3ucVaZCfo',
       popularity=61,
       type='artist',
       followers=2008901,
       genres=['alternative dance',
               'big beat',
               'breakbeat',
               'electronica',
               'rave',
               'trip hop'],
       external_urls=[{'spotify': 'https://open.spotify.com/artist/1GhPHrq36VKCY3ucVaZCfo'}],
       images=[Image(url='https://i.scdn.co/image/ab6761610000e5ebae05213e52565bfd7e7489b3',
                     height=640,
                     width=640),
               Image(url='https://i.scdn.co/image/ab67616100005174ae05213e52565bfd7e7489b3',
                     height=320,
                     width=320),
               Image(url='https://i.scdn.co/image/ab6761610000f178ae05213e52565bfd7e7489b3',
                     height=160,
                     width=160)])
```