## SymPyfy ##

A spotify python library.
API implemented so far:

**Artists**
- [x] Get Artist ⮕ **GET** `/artists/{id}`
- [x] Get Several Artists ⮕ **GET** `/artists?ids={ids}`
- [ ] Get Artist's Albums ⮕ **GET** `/artists/{id}/albums`
- [ ] Get Artist's Top Tracks ⮕ **GET** `/artists/{id}/top-tracks`
- [x] Get Artist's Related Artists ⮕ **GET** `/artists/{id}/related-artists`


**Tracks**
- [ ] Get Track ⮕ **GET** `/tracks/{id}`
- [ ] Get Several Tracks ⮕ **GET** `/tracks?ids={ids}`
- [ ] Get User's Saved Tracks ⮕ **GET** `/me/tracks` 🔒
- [ ] Save Tracks for Current User ⮕ **PUT** /me/tracks?ids={ids} 🔒
- [ ] Remove User's Saved Tracks ⮕ **DELETE** /me/tracks?ids={ids} 🔒
- [ ] Check User's Saved Tracks ⮕ **GET** /me/tracks/contains?ids={ids} 🔒
- [ ] Get Several Tracks' Audio Features ⮕ **GET** /audio-features?ids={ids}
- [ ] Get Track's Audio Features ⮕ **GET** /audio-features/{id}
- [ ] Get Track's Audio Analysis ⮕ **GET** /audio-analysis/{id}
- [ ] Get Recommendations ⮕ **GET** /recommendations


