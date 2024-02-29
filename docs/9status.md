# Spotify Api Implementation status

###Albums

- [x] Get Album ⮕ **GET** `/albums/{id}`
- [x] Get Several Albums ⮕ **GET** `/albums?ids={ids}`
- [x] Get Album Tracks ⮕ **GET** `/albums/{id}/tracks`
- [ ] Get User's Saved Albums ⮕ **GET** `/me/albums` 🔒
- [ ] Save Albums for Current User ⮕ **PUT** `/me/albums` 🔒
- [ ] Remove Users' Saved Albums ⮕ **DELETE** `/me/albums` 🔒
- [ ] Check User's Saved Albums ⮕ **GET** `/me/albums/contains?ids={ids}` 🔒
- [x] Get New Releases ⮕ **GET** `/browse/new-releases`


###Artists

- [x] Get Artist ⮕ **GET** `/artists/{id}`
- [x] Get Several Artists ⮕ **GET** `/artists?ids={ids}`
- [x] Get Artist's Albums ⮕ **GET** `/artists/{id}/albums`
- [x] Get Artist's Top Tracks ⮕ **GET** `/artists/{id}/top-tracks`
- [x] Get Artist's Related Artists ⮕ **GET** `/artists/{id}/related-artists`

###Audiobooks

_Since audiobooks are not available in my country, I won't implement this part of the API_


###Categories

- [x] Get Single Browse Category ⮕ **GET** `/browse/categories/{category_id}`
- [x] Get Several Browse Categories ⮕ **GET** `/browse/categories`


###Chapters

_Since audiobooks are not available in my country, I won't implement this part of the API_


###Episodes

- [ ] Get Episode ⮕ **GET** `/episodes/{id}` 🔒
- [ ] Get Several Episodes ⮕ **GET** `/episodes` 🔒
- [ ] Get User's Saved Episodes ⮕ **GET** `/me/episodes` 🔒
- [ ] Save Episodes for Current User ⮕ **PUT** `/me/episodes` 🔒
- [ ] Remove User's Saved Episodes ⮕ **DELETE** `/me/episodes` 🔒
- [ ] Check User's Saved Episodes ⮕ **GET** `/me/episodes/contains` 🔒


###Genres

- [x] Get Available Genre Seeds ⮕ **GET** `/recommendations/available-genre-seeds`


###Markets

- [x] Get Available Markets ⮕ **GET** `/markets`


###Player

- [ ] Get Playback State ⮕ **GET** `/me/player` 🔒
- [ ] Transfer Playback ⮕ **PUT** `/me/player` 🔒
- [ ] Get Available Devices ⮕ **GET** `/me/player/devices` 🔒
- [ ] Get Currently Playing Track ⮕ **GET** `/me/player/currently-playing` 🔒
- [ ] Start/Resume Playback ⮕ **PUT** `/me/player/play` 🔒
- [ ] Pause Playback ⮕ **PUT** `/me/player/pause` 🔒
- [ ] Skip To Next ⮕ **POST** `/me/player/next` 🔒
- [ ] Skip To Previous ⮕ **POST** `/me/player/previous` 🔒
- [ ] Seek To Position ⮕ **GET** `/me/player/seek` 🔒
- [ ] Set Repeat Mode ⮕ **PUT** `/me/player/repeat` 🔒
- [ ] Set Playback Volume ⮕ **PUT** `/me/player/volume` 🔒
- [ ] Toggle Playback Shuffle ⮕ **PUT** `/me/player/shuffle` 🔒
- [ ] Get Recently Played Tracks ⮕ **GET** `/me/player/recently-played` 🔒
- [ ] Get the User's Queue ⮕ **GET** `/me/player/queue` 🔒
- [ ] Add Item to Playback Queue ⮕ **POST** `/me/player/queue` 🔒


###Playlists

- [ ] Get Playlist ⮕ **GET** `/playlists/{playlist_id}`
- [ ] Change Playlist Details ⮕ **PUT** `/playlists/{playlist_id}` 🔒
- [ ] Get Playlist Items ⮕ **GET** `/playlists/{playlist_id}/tracks` 🔒
- [ ] Update Playlist Items ⮕ **PUT** `/playlists/{playlist_id}/tracks` 🔒
- [ ] Add Items to Playlist ⮕ **POST** `/playlists/{playlist_id}/tracks` 🔒
- [ ] Remove Playlist Items ⮕ **DELETE** `/playlists/{playlist_id}/tracks` 🔒
- [ ] Get Current User's Playlists ⮕ **GET** `/me/playlists` 🔒
- [ ] Get User's Playlists ⮕ **GET** `/users/{user_id}/playlists` 🔒
- [ ] Create Playlist ⮕ **POST** `/users/{user_id}/playlists` 🔒
- [ ] Get Featured Playlists ⮕ **GET** `/browse/featured-playlists`
- [ ] Get Category's Playlists ⮕ **GET** `/browse/categories/{category_id}/playlists`
- [ ] Get Playlist Cover Image ⮕ **GET** `/playlists/{playlist_id}/images`
- [ ] Add Custom Playlist Cover Image ⮕ **PUT** `/playlists/{playlist_id}/images` 🔒


###Search

- [ ] Search for Item ⮕ **GET** `/search`


###Shows

- [x] Get Show ⮕ **GET** `/shows/{id}` 🔒 (partial, resume_point not implemented)
- [ ] Get Several Shows ⮕ **GET** `/shows`
- [ ] Get Show Episodes ⮕ **GET** `/shows/{id}/episodes` 🔒 (?)
- [ ] Get User's Saved Shows ⮕ **GET** `/me/shows` 🔒
- [ ] Save Shows for Current User ⮕ **PUT** `/me/shows` 🔒
- [ ] Remove User's Saved Shows ⮕ **DELETE** `/me/shows` 🔒
- [ ] Check User's Saved Shows ⮕ **GET** `/me/shows/contains` 🔒


###Tracks

- [x] Get Track ⮕ **GET** `/tracks/{id}`
- [x] Get Several Tracks ⮕ **GET** `/tracks?ids={ids}`
- [ ] Get User's Saved Tracks ⮕ **GET** `/me/tracks` 🔒
- [ ] Save Tracks for Current User ⮕ **PUT** `/me/tracks?ids={ids}` 🔒
- [ ] Remove User's Saved Tracks ⮕ **DELETE** `/me/tracks?ids={ids}` 🔒
- [ ] Check User's Saved Tracks ⮕ **GET** `/me/tracks/contains?ids={ids}` 🔒
- [x] Get Track's Audio Features ⮕ **GET** `/audio-features/{id}`
- [x] Get Several Tracks' Audio Features ⮕ **GET** `/audio-features?ids={ids}`
- [ ] Get Track's Audio Analysis ⮕ **GET** `/audio-analysis/{id}`
- [ ] Get Recommendations ⮕ **GET** `/recommendations`


###Users

- [ ] Get Current User's Profile ⮕ **GET** `/me` 🔒
- [ ] Get User's Top Items ⮕ **GET** `/me/top/{type}` 🔒
- [x] Get User's Profile ⮕ **GET** `/users/{user_id}`
- [ ] Follow Playlist ⮕ **GET** `/playlists/{playlist_id}/followers` 🔒
- [ ] Unfollow Playlist ⮕ **DELETE** `/playlists/{playlist_id}/followers` 🔒
- [ ] Get Followed Artists ⮕ **GET** `/me/following` 🔒
- [ ] Follow Artists or Users ⮕ **PUT** `/me/following` 🔒
- [ ] Unfollow Artists or Users ⮕ **DELETE** `/me/following` 🔒
- [ ] Check If User Follows Artists or Users ⮕ **GET** `/me/following/contains` 🔒
- [ ] Check if Users Follow Playlist ⮕ **GET** `/playlists/{playlist_id}/followers/contains`