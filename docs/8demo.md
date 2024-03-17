#API DEMO with APP auth

``` py title="DEMO"
from rich.console import Console

from sympyfy import Sympyfy
from operator import itemgetter

console = Console()

    spotify = Sympyfy()
    spotify.load_credentials()

    artist = spotify.get_artist(id)
    albums = spotify.get_artist_albums(id, limit=50, offset=0, include_groups=["album", "compilation", "single"])
    album_ids = []
    more_albums = True
    while more_albums:
        album_ids += [{"name":x.name, "id": x.id, "release_date":x.release_date} for x in albums.items]
        more_albums = albums and albums.next
        albums = spotify.get_artist_albums(id, limit=50, offset=albums.offset + 50, include_groups=["album", "compilation", "single"])

    with open("docs/demo.md", "w") as md:
        md.write(f"#API DEMO with APP auth\n\n")
        md.write(f"##{artist.name}\n")

        for x in sorted(album_ids, key=itemgetter('release_date')):
            md.write(f"###{x['name']}  _({x['release_date']})_\n")

            tracks = spotify.get_album_tracks(x["id"], limit=50, offset=0)
            tracks_ids = []
            more_tracks = True
            while more_tracks:
                tracks_ids += [{"name": x.name, "id": x.id, "disc_number":x.disc_number, "track_number": x.track_number, "sort": f"{x.disc_number:02}-{x.track_number:02}"} for x in tracks.items]
                more_tracks = tracks and tracks.next
                tracks = spotify.get_album_tracks(x["id"], limit=50, offset=tracks.offset + 50)

            for x in sorted(tracks_ids, key=itemgetter('sort')):
                md.write(f" - {x['disc_number']}-{x['track_number']}  {x['name']}\n")

            md.write("\n")
```

---


##Nirvana
__Bleach__  _(1989-06-01)

| Disc - Track | Title |
| :---: | :--- |
| 1-1 | Blew |
| 1-2 | Floyd The Barber |
| 1-3 | About A Girl |
| 1-4 | School |
| 1-5 | Love Buzz |
| 1-6 | Paper Cuts |
| 1-7 | Negative Creep |
| 1-8 | Scoff |
| 1-9 | Swap Meet |
| 1-10 | Mr. Moustache |
| 1-11 | Sifting |
| 1-12 | Big Cheese |
| 1-13 | Downer |

__Bleach (Deluxe Edition)__  _(1989-06-15)

| Disc - Track | Title |
| :---: | :--- |
| 1-1 | Blew |
| 1-2 | Floyd The Barber |
| 1-3 | About A Girl |
| 1-4 | School |
| 1-5 | Love Buzz |
| 1-6 | Paper Cuts |
| 1-7 | Negative Creep |
| 1-8 | Scoff |
| 1-9 | Swap Meet |
| 1-10 | Mr. Moustache |
| 1-11 | Sifting |
| 1-12 | Big Cheese |
| 1-13 | Downer |
| 1-14 | Intro (Live at Pine Street Theatre) |
| 1-15 | School (Live at Pine Street Theatre) |
| 1-16 | Floyd The Barber (Live at Pine Street Theatre) |
| 1-17 | Dive (Live at Pine Street Theatre) |
| 1-18 | Love Buzz (Live at Pine Street Theatre) |
| 1-19 | Spank Thru (Live at Pine Street Theatre) |
| 1-20 | Molly's Lips (Live at Pine Street Theatre) |
| 1-21 | Sappy (Live at Pine Street Theatre) |
| 1-22 | Scoff (Live at Pine Street Theatre) |
| 1-23 | About A Girl (Live at Pine Street Theatre) |
| 1-24 | Been A Son (Live at Pine Street Theatre) |
| 1-25 | Blew (Live at Pine Street Theatre) |

__Nevermind (Super Deluxe Edition)__  _(1991-09-26)

| Disc - Track | Title |
| :---: | :--- |
| 1-1 | Smells Like Teen Spirit |
| 1-2 | In Bloom |
| 1-3 | Come As You Are |
| 1-4 | Breed |
| 1-5 | Lithium |
| 1-6 | Polly |
| 1-7 | Territorial Pissings |
| 1-8 | Drain You |
| 1-9 | Lounge Act |
| 1-10 | Stay Away |
| 1-11 | On A Plain |
| 1-12 | Something In The Way |
| 1-13 | Endless, Nameless |
| 1-14 | Even In His Youth - B-Side |
| 1-15 | Aneurysm |
| 1-16 | Curmudgeon |
| 1-17 | D-7 - Live At The BBC |
| 1-18 | Been A Son - Live At Paramount Theatre B-Side |
| 1-19 | School - Live At Paramount Theatre/1991 |
| 1-20 | Drain You - Live At Paramount Theatre B-Side |
| 1-21 | Sliver - Live At Del Mar B-Side |
| 1-22 | Polly - Live At Del Mar B-Side |
| 2-1 | In Bloom - Smart Sessions |
| 2-2 | Immodium (Breed) - Smart Sessions |
| 2-3 | Lithium - Smart Sessions |
| 2-4 | Polly - Smart Sessions |
| 2-5 | Pay To Play - Smart Sessions |
| 2-6 | Here She Comes Now - Smart Sessions |
| 2-7 | Dive - Smart Sessions |
| 2-8 | Sappy - Smart Sessions |
| 2-9 | Smells Like Teen Spirit - Boombox Rehearsals |
| 2-10 | Verse Chorus Verse - Boombox Rehearsals |
| 2-11 | Territorial Pissings - Boombox Rehearsals |
| 2-12 | Lounge Act - Boombox Rehearsals |
| 2-13 | Come As You Are - Boombox Rehearsals |
| 2-14 | Old Age - Boombox Rehearsals |
| 2-15 | Something In The Way - Boombox Rehearsals |
| 2-16 | On A Plain - Boombox Rehearsals |
| 2-17 | Drain You - Live At The BBC |
| 2-18 | Something In The Way - Live At The BBC |
| 3-1 | Smells Like Teen Spirit - Devonshire Mix |
| 3-2 | In Bloom - Devonshire Mix |
| 3-3 | Come As You Are - Devonshire Mix |
| 3-4 | Breed - Devonshire Mix |
| 3-5 | Lithium - Devonshire Mix |
| 3-6 | Territorial Pissings - Devonshire Mix |
| 3-7 | Drain You - Devonshire Mix |
| 3-8 | Lounge Act - Devonshire Mix |
| 3-9 | Stay Away - Devonshire Mix |
| 3-10 | On A Plain - Devonshire Mix |
| 3-11 | Something In The Way - Devonshire Mix |
| 4-1 | Jesus Doesn't Want Me For A Sunbeam - Live At The Paramount |
| 4-2 | Aneurysm - Live At The Paramount |
| 4-3 | Drain You - Live At The Paramount/1991 |
| 4-4 | School - Live At The Paramount |
| 4-5 | Floyd The Barber - Live At The Paramount |
| 4-6 | Smells Like Teen Spirit - Live At The Paramount |
| 4-7 | About A Girl - Live At The Paramount |
| 4-8 | Polly - Live At The Paramount |
| 4-9 | Breed - Live At The Paramount |
| 4-10 | Sliver - Live At The Paramount |
| 4-11 | Love Buzz - Live At The Paramount |
| 4-12 | Lithium - Live At The Paramount |
| 4-13 | Been A Son - Live At The Paramount |
| 4-14 | Negative Creep - Live At The Paramount |
| 4-15 | On A Plain - Live At The Paramount |
| 4-16 | Blew - Live At The Paramount |
| 4-17 | Rape Me - Live At The Paramount |
| 4-18 | Territorial Pissings - Live At The Paramount |
| 4-19 | Endless, Nameless - Live At The Paramount |

__Nevermind (Remastered)__  _(1991-09-26)

| Disc - Track | Title |
| :---: | :--- |
| 1-1 | Smells Like Teen Spirit |
| 1-2 | In Bloom |
| 1-3 | Come As You Are |
| 1-4 | Breed |
| 1-5 | Lithium |
| 1-6 | Polly |
| 1-7 | Territorial Pissings |
| 1-8 | Drain You |
| 1-9 | Lounge Act |
| 1-10 | Stay Away |
| 1-11 | On A Plain |
| 1-12 | Something In The Way |
| 1-13 | Endless, Nameless |

__Nevermind (Deluxe Edition)__  _(1991-09-26)

| Disc - Track | Title |
| :---: | :--- |
| 1-1 | Smells Like Teen Spirit |
| 1-2 | In Bloom |
| 1-3 | Come As You Are |
| 1-4 | Breed |
| 1-5 | Lithium |
| 1-6 | Polly |
| 1-7 | Territorial Pissings |
| 1-8 | Drain You |
| 1-9 | Lounge Act |
| 1-10 | Stay Away |
| 1-11 | On A Plain |
| 1-12 | Something In The Way |
| 1-13 | Endless, Nameless |
| 1-14 | Even In His Youth - B-Side |
| 1-15 | Aneurysm |
| 1-16 | Curmudgeon |
| 1-17 | D-7 - Live At The BBC |
| 1-18 | Been A Son - Live At Paramount Theatre B-Side |
| 1-19 | School - Live At Paramount Theatre/1991 |
| 1-20 | Drain You - Live At Paramount Theatre B-Side |
| 1-21 | Sliver - Live At Del Mar B-Side |
| 1-22 | Polly - Live At Del Mar B-Side |
| 2-1 | In Bloom - Smart Sessions |
| 2-2 | Immodium (Breed) - Smart Sessions |
| 2-3 | Lithium - Smart Sessions |
| 2-4 | Polly - Smart Sessions |
| 2-5 | Pay To Play - Smart Sessions |
| 2-6 | Here She Comes Now - Smart Sessions |
| 2-7 | Dive - Smart Sessions |
| 2-8 | Sappy - Smart Sessions |
| 2-9 | Smells Like Teen Spirit - Boombox Rehearsals |
| 2-10 | Verse Chorus Verse - Boombox Rehearsals |
| 2-11 | Territorial Pissings - Boombox Rehearsals |
| 2-12 | Lounge Act - Boombox Rehearsals |
| 2-13 | Come As You Are - Boombox Rehearsals |
| 2-14 | Old Age - Boombox Rehearsals |
| 2-15 | Something In The Way - Boombox Rehearsals |
| 2-16 | On A Plain - Boombox Rehearsals |
| 2-17 | Drain You - Live At The BBC |
| 2-18 | Something In The Way - Live At The BBC |

__Incesticide__  _(1992-12-14)

| Disc - Track | Title |
| :---: | :--- |
| 1-1 | Dive |
| 1-2 | Sliver |
| 1-3 | Stain |
| 1-4 | Been A Son - BBC Mark Goodier Session |
| 1-5 | Turnaround - BBC John Peel Session 1990 |
| 1-6 | Molly's Lips - BBC John Peel Session 1990 |
| 1-7 | Son Of A Gun - BBC John Peel Session 1990 |
| 1-8 | (New Wave) Polly - BBC Mark Goodier Session |
| 1-9 | Beeswax |
| 1-10 | Downer |
| 1-11 | Mexican Seafood |
| 1-12 | Hairspray Queen |
| 1-13 | Aero Zeppelin |
| 1-14 | Big Long Now |
| 1-15 | Aneurysm |

__In Utero (Super Deluxe Edition)__  _(1993-09-21)

| Disc - Track | Title |
| :---: | :--- |
| 1-1 | Serve The Servants |
| 1-2 | Scentless Apprentice |
| 1-3 | Heart-Shaped Box |
| 1-4 | Rape Me |
| 1-5 | Frances Farmer Will Have Her Revenge On Seattle |
| 1-6 | Dumb |
| 1-7 | Very Ape |
| 1-8 | Milk It |
| 1-9 | Pennyroyal Tea |
| 1-10 | Radio Friendly Unit Shifter |
| 1-11 | Tourette's |
| 1-12 | All Apologies |
| 1-13 | Gallons Of Rubbing Alcohol Flow Through The Strip |
| 1-14 | Marigold |
| 1-15 | Moist Vagina - 2013 Mix |
| 1-16 | Sappy - 2013 Mix |
| 1-17 | I Hate Myself And Want To Die - 2013 Mix |
| 1-18 | Pennyroyal Tea - Scott Litt Mix |
| 1-19 | Heart Shaped Box - Original Steve Albini 1993 Mix |
| 1-20 | All Apologies - Original Steve Albini 1993 Mix |
| 2-1 | Serve The Servants - 2013 Mix |
| 2-2 | Scentless Apprentice - 2013 Mix |
| 2-3 | Heart Shaped Box - 2013 Mix |
| 2-4 | Rape Me - 2013 Mix |
| 2-5 | Frances Farmer Will Have Her Revenge On Seattle - 2013 Mix |
| 2-6 | Dumb - 2013 Mix |
| 2-7 | Very Ape - 2013 Mix |
| 2-8 | Milk It - 2013 Mix |
| 2-9 | Pennyroyal Tea - 2013 Mix |
| 2-10 | Radio Friendly Unit Shifter - 2013 Mix |
| 2-11 | Tourette's - 2013 Mix |
| 2-12 | All Apologies - 2013 Mix |
| 2-13 | Scentless Apprentice - Demo |
| 2-14 | Frances Farmer Will Have Her Revenge On Seattle - Demo / Instrumental |
| 2-15 | Dumb - Demo / Instrumental |
| 2-16 | Very Ape - Demo / Instrumental |
| 2-17 | Pennyroyal Tea - Demo / Instrumental |
| 2-18 | Radio Friendly Unit Shifter - Demo / Instrumental |
| 2-19 | Tourette's - Demo / Instrumental |
| 2-20 | Marigold - Demo |
| 2-21 | All Apologies - Demo |
| 2-22 | Forgotten Tune - Demo / Instrumental |
| 2-23 | Jam - Demo |
| 3-1 | Radio Friendly Unit Shifter - Live & Loud |
| 3-2 | Drain You - Live & Loud |
| 3-3 | Breed - Live & Loud |
| 3-4 | Serve The Servants - Live & Loud |
| 3-5 | Rape Me - Live & Loud |
| 3-6 | Sliver - Live & Loud |
| 3-7 | Pennyroyal Tea - Live & Loud |
| 3-8 | Scentless Apprentice - Live & Loud |
| 3-9 | All Apologies - Live & Loud |
| 3-10 | Heart Shaped Box - Live & Loud |
| 3-11 | Blew - Live & Loud |
| 3-12 | The Man Who Sold The World - Live & Loud |
| 3-13 | School - Live & Loud |
| 3-14 | Come As You Are - Live & Loud |
| 3-15 | Lithium - Live & Loud |
| 3-16 | About A Girl - Live & Loud |
| 3-17 | Endless, Nameless - Live & Loud |

__In Utero (Deluxe Edition)__  _(1993-09-21)

| Disc - Track | Title |
| :---: | :--- |
| 1-1 | Serve The Servants |
| 1-2 | Scentless Apprentice |
| 1-3 | Heart-Shaped Box |
| 1-4 | Rape Me |
| 1-5 | Frances Farmer Will Have Her Revenge On Seattle |
| 1-6 | Dumb |
| 1-7 | Very Ape |
| 1-8 | Milk It |
| 1-9 | Pennyroyal Tea |
| 1-10 | Radio Friendly Unit Shifter |
| 1-11 | Tourette's |
| 1-12 | All Apologies |
| 1-13 | Gallons Of Rubbing Alcohol Flow Through The Strip |
| 1-14 | Marigold |
| 1-15 | Moist Vagina - 2013 Mix |
| 1-16 | Sappy - 2013 Mix |
| 1-17 | I Hate Myself And Want To Die - 2013 Mix |
| 1-18 | Pennyroyal Tea - Scott Litt Mix |
| 1-19 | Heart Shaped Box - Original Steve Albini 1993 Mix |
| 1-20 | All Apologies - Original Steve Albini 1993 Mix |
| 2-1 | Serve The Servants - 2013 Mix |
| 2-2 | Scentless Apprentice - 2013 Mix |
| 2-3 | Heart Shaped Box - 2013 Mix |
| 2-4 | Rape Me - 2013 Mix |
| 2-5 | Frances Farmer Will Have Her Revenge On Seattle - 2013 Mix |
| 2-6 | Dumb - 2013 Mix |
| 2-7 | Very Ape - 2013 Mix |
| 2-8 | Milk It - 2013 Mix |
| 2-9 | Pennyroyal Tea - 2013 Mix |
| 2-10 | Radio Friendly Unit Shifter - 2013 Mix |
| 2-11 | Tourette's - 2013 Mix |
| 2-12 | All Apologies - 2013 Mix |
| 2-13 | Scentless Apprentice - Demo |
| 2-14 | Frances Farmer Will Have Her Revenge On Seattle - Demo / Instrumental |
| 2-15 | Dumb - Demo / Instrumental |
| 2-16 | Very Ape - Demo / Instrumental |
| 2-17 | Pennyroyal Tea - Demo / Instrumental |
| 2-18 | Radio Friendly Unit Shifter - Demo / Instrumental |
| 2-19 | Tourette's - Demo / Instrumental |
| 2-20 | Marigold - Demo |
| 2-21 | All Apologies - Demo |
| 2-22 | Forgotten Tune - Demo / Instrumental |
| 2-23 | Jam - Demo |

__In Utero__  _(1993-09-21)

| Disc - Track | Title |
| :---: | :--- |
| 1-1 | Serve The Servants |
| 1-2 | Scentless Apprentice |
| 1-3 | Heart-Shaped Box |
| 1-4 | Rape Me |
| 1-5 | Frances Farmer Will Have Her Revenge On Seattle |
| 1-6 | Dumb |
| 1-7 | Very Ape |
| 1-8 | Milk It |
| 1-9 | Pennyroyal Tea |
| 1-10 | Radio Friendly Unit Shifter |
| 1-11 | Tourette's |
| 1-12 | All Apologies |

__MTV Unplugged In New York (25th Anniversary)__  _(1994-11-01)

| Disc - Track | Title |
| :---: | :--- |
| 1-1 | About A Girl - Live |
| 1-2 | Come As You Are - Live |
| 1-3 | Jesus Doesn't Want Me For A Sunbeam - Live |
| 1-4 | The Man Who Sold The World - Live |
| 1-5 | Pennyroyal Tea - Live |
| 1-6 | Dumb - Live |
| 1-7 | Polly - Live |
| 1-8 | On A Plain - Live |
| 1-9 | Something In The Way - Live |
| 1-10 | Plateau - Live |
| 1-11 | Oh Me - Live |
| 1-12 | Lake Of Fire - Live |
| 1-13 | All Apologies - Live |
| 1-14 | Where Did You Sleep Last Night - Live |
| 1-15 | Come As You Are - Rehearsal |
| 1-16 | Polly - Rehearsal |
| 1-17 | Plateau - Rehearsal |
| 1-18 | Pennyroyal Tea - Rehearsal |
| 1-19 | The Man Who Sold The World - Rehearsal |

__MTV Unplugged In New York__  _(1994-11-01)

| Disc - Track | Title |
| :---: | :--- |
| 1-1 | About A Girl - Live |
| 1-2 | Come As You Are - Live |
| 1-3 | Jesus Doesn't Want Me For A Sunbeam - Live |
| 1-4 | The Man Who Sold The World - Live |
| 1-5 | Pennyroyal Tea - Live |
| 1-6 | Dumb - Live |
| 1-7 | Polly - Live |
| 1-8 | On A Plain - Live |
| 1-9 | Something In The Way - Live |
| 1-10 | Plateau - Live |
| 1-11 | Oh Me - Live |
| 1-12 | Lake Of Fire - Live |
| 1-13 | All Apologies - Live |
| 1-14 | Where Did You Sleep Last Night - Live |

__From The Muddy Banks Of The Wishkah (Live)__  _(1996-10-01)

| Disc - Track | Title |
| :---: | :--- |
| 1-1 | Intro - Live At London Astoria, UK, December 3, 1989 |
| 1-2 | School - Live In Amsterdam, Netherlands/1991 |
| 1-3 | Drain You - Live At Del Mar Fairgrounds, CA., December 28, 1991 |
| 1-4 | Aneurysm - Live In Del Mar, California/1991 |
| 1-5 | Smells Like Teen Spirit - Live In Del Mar, California/1991 |
| 1-6 | Been A Son - Live In Amsterdam, Netherlands/1991 |
| 1-7 | Lithium - Live In Amsterdam, Netherlands/1991 |
| 1-8 | Sliver - Live In Springfield, MA., November 10, 1993 |
| 1-9 | Spank Thru - Live In Rome, Italy, November 19, 1991 |
| 1-10 | Scentless Apprentice - Live In Seattle, WA., December 13, 1993 |
| 1-11 | Heart-Shaped Box - Live In Los Angeles, CA, December 30, 1993 |
| 1-12 | Milk It - Live In Seattle, WA., January 5, 1994 |
| 1-13 | Negative Creep - Live In Seattle, WA., October 31, 1991 |
| 1-14 | Polly - Live At London Astoria, UK, December 3, 1989 |
| 1-15 | Breed - Live At London Astoria, UK, December 3, 1989 |
| 1-16 | Tourette's - Live At Reading Festival, UK, August 30, 1992 |
| 1-17 | Blew - Live In Amsterdam, Netherlands/1991 |

__Nirvana__  _(2002-10-29)

| Disc - Track | Title |
| :---: | :--- |
| 1-1 | You Know You're Right |
| 1-2 | About A Girl |
| 1-3 | Been A Son - Blew EP Version |
| 1-4 | Sliver |
| 1-5 | Smells Like Teen Spirit |
| 1-6 | Come As You Are |
| 1-7 | Lithium |
| 1-8 | In Bloom |
| 1-9 | Heart-Shaped Box |
| 1-10 | Pennyroyal Tea - Single Mix |
| 1-11 | Rape Me |
| 1-12 | Dumb |
| 1-13 | All Apologies - Live |
| 1-14 | The Man Who Sold The World - Live |

__With The Lights Out - Box Set__  _(2004-11-23)

| Disc - Track | Title |
| :---: | :--- |
| 1-1 | Heartbreaker - Live |
| 1-2 | Anorexorcist - Live |
| 1-3 | White Lace And Strange - Live |
| 1-4 | Help Me, I'm Hungry - Live |
| 1-5 | Mrs. Butterworth - 1988 Rehearsal |
| 1-6 | If You Must - Demo |
| 1-7 | Pen Cap Chew - Demo |
| 1-8 | Downer - Live |
| 1-9 | Floyd The Barber - Live |
| 1-10 | Raunchola/Moby Dick - Live |
| 1-11 | Beans - Solo Acoustic |
| 1-12 | Don't Want It All - Solo Acoustic |
| 1-13 | Clean Up Before She Comes - Solo Acoustic |
| 1-14 | Polly - Solo Acoustic Demo |
| 1-15 | About A Girl - Home Demo |
| 1-16 | Blandest - Demo |
| 1-17 | Dive - Demo |
| 1-18 | They Hung Him On A Cross - Demo |
| 1-19 | Grey Goose - Instrumental Demo |
| 1-20 | Ain't It A Shame - Demo |
| 1-21 | Token Eastern Song - Demo |
| 1-22 | Even In His Youth - Demo |
| 1-23 | Polly - Demo |
| 2-1 | Opinion - Live Solo Acoustic |
| 2-2 | Lithium - Live Solo Acoustic |
| 2-3 | Been A Son - Live Solo Acoustic |
| 2-4 | Sliver - Solo Acoustic Demo |
| 2-5 | Where Did You Sleep Last Night - Solo Acoustic Demo |
| 2-6 | Pay To Play - Demo |
| 2-7 | Here She Comes Now - Demo |
| 2-8 | Drain You - Demo |
| 2-9 | Aneurysm |
| 2-10 | Smells Like Teen Spirit - Rehearsal Demo |
| 2-11 | Breed - Rough Mix |
| 2-12 | Verse Chorus Verse - Outtake |
| 2-13 | Old Age - Nevermind Outtake |
| 2-14 | Endless, Nameless - 1991 Radio Appearance |
| 2-15 | Dumb - 1991 Radio Appearance |
| 2-16 | D-7 - 1990 Radio Appearance |
| 2-17 | Oh The Guilt |
| 2-18 | Curmudgeon |
| 2-19 | Return Of The Rat - Outtake |
| 2-20 | Smells Like Teen Spirit - Butch Vig Mix |
| 3-1 | Rape Me - Solo Acoustic |
| 3-2 | Rape Me - Demo |
| 3-3 | Scentless Apprentice - Rehearsal Demo |
| 3-4 | Heart Shaped Box - Demo |
| 3-5 | I Hate Myself And Want To Die - Demo |
| 3-6 | Milk It - Demo |
| 3-7 | Moist Vagina - Demo |
| 3-8 | Gallons Of Rubbing Alcohol Flow Through The Strip |
| 3-9 | The Other Improv - Demo |
| 3-10 | Serve The Servants - Solo Acoustic |
| 3-11 | Very Ape - Solo Acoustic |
| 3-12 | Pennyroyal Tea - Solo Acoustic |
| 3-13 | Marigold |
| 3-14 | Sappy |
| 3-15 | Jesus Doesn't Want Me For A Sunbeam - Rehearsal Demo |
| 3-16 | Do Re Mi - Home Demo |
| 3-17 | You Know You're Right - Home Demo |
| 3-18 | All Apologies - Home Demo |

__Sliver - The Best Of The Box__  _(2005-01-01)

| Disc - Track | Title |
| :---: | :--- |
| 1-1 | Spank Thru - 1985 Fecal Matter Demo |
| 1-2 | Heartbreaker - Live |
| 1-3 | Mrs. Butterworth - 1988 Rehearsal |
| 1-4 | Floyd The Barber - Live |
| 1-5 | Clean Up Before She Comes - Solo Acoustic |
| 1-6 | About A Girl - Home Demo |
| 1-7 | Blandest - Demo |
| 1-8 | Ain't It A Shame - Demo |
| 1-9 | Sappy - 1990 Studio Demo |
| 1-10 | Opinion - Live Solo Acoustic |
| 1-11 | Lithium - Live Solo Acoustic |
| 1-12 | Sliver - Solo Acoustic Demo |
| 1-13 | Smells Like Teen Spirit - Rehearsal Demo |
| 1-14 | Come As You Are - Boom Box Version |
| 1-15 | Old Age - Nevermind Outtake |
| 1-16 | Oh The Guilt |
| 1-17 | Rape Me - Solo Acoustic |
| 1-18 | Rape Me - Demo |
| 1-19 | Heart Shaped Box - Demo |
| 1-20 | Do Re Mi - Home Demo |
| 1-21 | You Know You're Right - Home Demo |
| 1-22 | All Apologies - Home Demo |

__Live at Reading__  _(2009-01-01)

| Disc - Track | Title |
| :---: | :--- |
| 1-1 | Breed - 1992/Live at Reading |
| 1-2 | Drain You - 1992/Live at Reading |
| 1-3 | Aneurysm - 1992/Live at Reading |
| 1-4 | School - 1992/Live at Reading |
| 1-5 | Sliver - 1992/Live at Reading |
| 1-6 | In Bloom - 1992/Live at Reading |
| 1-7 | Come As You Are - 1992/Live at Reading |
| 1-8 | Lithium - 1992/Live at Reading |
| 1-9 | About A Girl - 1992/Live at Reading |
| 1-10 | Tourette's - 1992/Live at Reading |
| 1-11 | Polly - 1992/Live at Reading |
| 1-12 | Lounge Act - 1992/Live at Reading |
| 1-13 | Smells Like Teen Spirit - 1992/Live at Reading |
| 1-14 | On A Plain - 1992/Live at Reading |
| 1-15 | Negative Creep - 1992/Live at Reading |
| 1-16 | Been A Son - 1992/Live at Reading |
| 1-17 | All Apologies - 1992/Live at Reading |
| 1-18 | Blew - 1992/Live at Reading |
| 1-19 | Dumb - 1992/Live at Reading |
| 1-20 | Stay Away - 1992/Live at Reading |
| 1-21 | Spank Thru - 1992/Live at Reading |
| 1-22 | The Money Will Roll Right In - 1992/Live at Reading |
| 1-23 | D-7 - 1992/Live at Reading |
| 1-24 | Territorial Pissings - 1992/Live at Reading |

__Live At The Paramount__  _(2019-04-12)

| Disc - Track | Title |
| :---: | :--- |
| 1-1 | Jesus Doesn't Want Me For A Sunbeam - Live At The Paramount/1991 |
| 1-2 | Aneurysm - Live At The Paramount/1991 |
| 1-3 | Drain You - Live At The Paramount/1991 |
| 1-4 | School - Live At The Paramount/1991 |
| 1-5 | Floyd The Barber - Live At The Paramount/1991 |
| 1-6 | Smells Like Teen Spirit - Live At The Paramount/1991 |
| 1-7 | About A Girl - Live At The Paramount/1991 |
| 1-8 | Polly - Live At The Paramount/1991 |
| 1-9 | Breed - Live At The Paramount/1991 |
| 1-10 | Sliver - Live At The Paramount/1991 |
| 1-11 | Love Buzz - Live At The Paramount/1991 |
| 1-12 | Lithium - Live At The Paramount/1991 |
| 1-13 | Been A Son - Live At The Paramount/1991 |
| 1-14 | Negative Creep - Live At The Paramount/1991 |
| 1-15 | On A Plain - Live At The Paramount/1991 |
| 1-16 | Blew - Live At The Paramount/1991 |
| 1-17 | Rape Me - Live At The Paramount/1991 |
| 1-18 | Territorial Pissings - Live At The Paramount/1991 |
| 1-19 | Endless, Nameless - Live At The Paramount/1991 |

__Live And Loud__  _(2019-07-26)

| Disc - Track | Title |
| :---: | :--- |
| 1-1 | Radio Friendly Unit Shifter - Live & Loud |
| 1-2 | Drain You - Live & Loud |
| 1-3 | Breed - Live & Loud |
| 1-4 | Serve The Servants - Live & Loud |
| 1-5 | Rape Me - Live & Loud |
| 1-6 | Sliver - Live & Loud |
| 1-7 | Pennyroyal Tea - Live & Loud |
| 1-8 | Scentless Apprentice - Live & Loud |
| 1-9 | All Apologies - Live & Loud |
| 1-10 | Heart Shaped Box - Live & Loud |
| 1-11 | Blew - Live & Loud |
| 1-12 | The Man Who Sold The World - Live & Loud |
| 1-13 | School - Live & Loud |
| 1-14 | Come As You Are - Live & Loud |
| 1-15 | Lithium - Live & Loud |
| 1-16 | About A Girl - Live & Loud |
| 1-17 | Endless, Nameless - Live & Loud |

__Breed (Live In Amsterdam, Netherlands/1991)__  _(2021-09-23)

| Disc - Track | Title |
| :---: | :--- |
| 1-1 | Breed - Live In Amsterdam, Netherlands/1991 |

__Lithium / Breed (Live)__  _(2021-10-08)

| Disc - Track | Title |
| :---: | :--- |
| 1-1 | Lithium - Live In Melbourne, Australia For Triple J/1992 |
| 1-2 | Breed - Live In Amsterdam, Netherlands/1991 |

__On A Plain / Lithium / Breed (Live)__  _(2021-10-22)

| Disc - Track | Title |
| :---: | :--- |
| 1-1 | On A Plain - Live In Tokyo, Japan/1992 |
| 1-2 | Lithium - Live In Melbourne, Australia For Triple J/1992 |
| 1-3 | Breed - Live In Amsterdam, Netherlands/1991 |

__In Bloom / On A Plain / Lithium / Breed__  _(2021-11-05)

| Disc - Track | Title |
| :---: | :--- |
| 1-1 | In Bloom - Remastered 2021 |
| 1-2 | On A Plain - Live In Tokyo, Japan/1992 |
| 1-3 | Lithium - Live In Melbourne, Australia For Triple J/1992 |
| 1-4 | Breed - Live In Amsterdam, Netherlands/1991 |

__Smells Like Teen Spirit / In Bloom / On A Plain / Lithium / Breed__  _(2021-11-10)

| Disc - Track | Title |
| :---: | :--- |
| 1-1 | Smells Like Teen Spirit - Remastered 2021 |
| 1-2 | In Bloom - Remastered 2021 |
| 1-3 | On A Plain - Live In Tokyo, Japan/1992 |
| 1-4 | Lithium - Live In Melbourne, Australia For Triple J/1992 |
| 1-5 | Breed - Live In Amsterdam, Netherlands/1991 |

__Nevermind (30th Anniversary Super Deluxe)__  _(2021-11-12)

| Disc - Track | Title |
| :---: | :--- |
| 1-1 | Smells Like Teen Spirit - Remastered 2021 |
| 1-2 | In Bloom - Remastered 2021 |
| 1-3 | Come As You Are - Remastered 2021 |
| 1-4 | Breed - Remastered 2021 |
| 1-5 | Lithium - Remastered 2021 |
| 1-6 | Polly - Remastered 2021 |
| 1-7 | Territorial Pissings - Remastered 2021 |
| 1-8 | Drain You - Remastered 2021 |
| 1-9 | Lounge Act - Remastered 2021 |
| 1-10 | Stay Away - Remastered 2021 |
| 1-11 | On A Plain - Remastered 2021 |
| 1-12 | Something In The Way - Remastered 2021 |
| 1-13 | Endless, Nameless - Remastered 2021 |
| 2-1 | Drain You - Live In Amsterdam, Netherlands/1991 |
| 2-2 | Aneurysm - Live In Amsterdam, Netherlands/1991 |
| 2-3 | School - Live In Amsterdam, Netherlands/1991 |
| 2-4 | Floyd The Barber - Live In Amsterdam, Netherlands/1991 |
| 2-5 | Smells Like Teen Spirit - Live In Amsterdam, Netherlands/1991 |
| 2-6 | About A Girl - Live In Amsterdam, Netherlands/1991 |
| 2-7 | Polly - Live In Amsterdam, Netherlands/1991 |
| 2-8 | Lithium - Live In Amsterdam, Netherlands/1991 |
| 2-9 | Sliver - Live In Amsterdam, Netherlands/1991 |
| 2-10 | Breed - Live In Amsterdam, Netherlands/1991 |
| 2-11 | Come As You Are - Live In Amsterdam, Netherlands/1991 |
| 2-12 | Been A Son - Live In Amsterdam, Netherlands/1991 |
| 2-13 | Negative Creep - Live In Amsterdam, Netherlands/1991 |
| 2-14 | On A Plain - Live In Amsterdam, Netherlands/1991 |
| 2-15 | Blew - Live In Amsterdam, Netherlands/1991 |
| 2-16 | Love Buzz - Live In Amsterdam, Netherlands/1991 |
| 2-17 | Territorial Pissings - Live In Amsterdam, Netherlands/1991 |
| 3-1 | Drain You - Live In Del Mar, California/1991 |
| 3-2 | Aneurysm - Live In Del Mar, California/1991 |
| 3-3 | School - Live In Del Mar, California/1991 |
| 3-4 | Floyd The Barber - Live In Del Mar, California/1991 |
| 3-5 | Smells Like Teen Spirit - Live In Del Mar, California/1991 |
| 3-6 | About A Girl - Live In Del Mar, California/1991 |
| 3-7 | Polly - Live In Del Mar, California/1991 |
| 3-8 | Sliver - Live In Del Mar, California/1991 |
| 3-9 | Breed - Live In Del Mar, California/1991 |
| 3-10 | Come As You Are - Live In Del Mar, California/1991 |
| 3-11 | Lithium - Live In Del Mar, California/1991 |
| 3-12 | Territorial Pissings - Live In Del Mar, California/1991 |
| 4-1 | Aneurysm - Live In Melbourne, Australia For Triple J/1992 |
| 4-2 | Drain You - Live In Melbourne, Australia For Triple J/1992 |
| 4-3 | School - Live In Melbourne, Australia For Triple J/1992 |
| 4-4 | Sliver - Live In Melbourne, Australia For Triple J/1992 |
| 4-5 | About A Girl - Live In Melbourne, Australia For Triple J/1992 |
| 4-6 | Come As You Are - Live In Melbourne, Australia For Triple J/1992 |
| 4-7 | Lithium - Live In Melbourne, Australia For Triple J/1992 |
| 4-8 | Breed - Live In Melbourne, Australia For Triple J/1992 |
| 4-9 | Polly - Live In Melbourne, Australia For Triple J/1992 |
| 4-10 | Lounge Act - Live In Melbourne, Australia For Triple J/1992 |
| 4-11 | In Bloom - Live In Melbourne, Australia For Triple J/1992 |
| 4-12 | Love Buzz - Live In Melbourne, Australia For Triple J/1992 |
| 4-13 | Smells Like Teen Spirit - Live In Melbourne, Australia For Triple J/1992 |
| 4-14 | Feedback Jam - Live In Melbourne, Australia For Triple J/1992 |
| 4-15 | Negative Creep - Live In Melbourne, Australia For Triple J/1992 |
| 4-16 | On A Plain - Live In Melbourne, Australia For Triple J/1992 |
| 4-17 | Blew - Live In Melbourne, Australia For Triple J/1992 |
| 5-1 | Negative Creep - Live In Tokyo, Japan/1992 |
| 5-2 | Been A Son - Live In Tokyo, Japan/1992 |
| 5-3 | On A Plain - Live In Tokyo, Japan/1992 |
| 5-4 | Blew - Live In Tokyo, Japan/1992 |
| 5-5 | Come As You Are - Live In Tokyo, Japan/1992 |
| 5-6 | Lithium - Live In Tokyo, Japan/1992 |
| 5-7 | Breed - Live In Tokyo, Japan/1992 |
| 5-8 | Sliver - Live In Tokyo, Japan/1992 |
| 5-9 | Drain You - Live In Tokyo, Japan/1992 |
| 5-10 | About A Girl - Live In Tokyo, Japan/1992 |
| 5-11 | School - Live In Tokyo, Japan/1992 |
| 5-12 | Aneurysm - Live In Tokyo, Japan/1992 |
| 5-13 | Love Buzz - Live In Tokyo, Japan/1992 |
| 5-14 | Polly - Live In Tokyo, Japan/1992 |
| 5-15 | Territorial Pissings - Live In Tokyo, Japan/1992 |
| 5-16 | Smells Like Teen Spirit - Live In Tokyo, Japan/1992 |

__In Utero 30th Live__  _(2023-09-29)

| Disc - Track | Title |
| :---: | :--- |
| 1-1 | Frances Farmer Will Have Her Revenge On Seattle - Live In Seattle, Seattle Center Arena - January 7, 1994 |
| 1-2 | All Apologies - Live In Los Angeles, Great Western Forum - December 30, 1993 |
| 1-3 | Pennyroyal Tea - Live In Los Angeles, Great Western Forum - December 30, 1993 |
| 1-4 | Scentless Apprentice - Live In Seattle, Seattle Center Arena - January 7, 1994 |

__In Utero (30th Anniversary Super Deluxe)__  _(2023-10-27)

| Disc - Track | Title |
| :---: | :--- |
| 1-1 | Serve The Servants - 2023 Remaster |
| 1-2 | Scentless Apprentice - 2023 Remaster |
| 1-3 | Heart-Shaped Box - 2023 Remaster |
| 1-4 | Rape Me - 2023 Remaster |
| 1-5 | Frances Farmer Will Have Her Revenge On Seattle - 2023 Remaster |
| 1-6 | Dumb - 2023 Remaster |
| 1-7 | Very Ape - 2023 Remaster |
| 1-8 | Milk It - 2023 Remaster |
| 1-9 | Pennyroyal Tea - 2023 Remaster |
| 1-10 | Radio Friendly Unit Shifter - 2023 Remaster |
| 1-11 | tourette's - 2023 Remaster |
| 1-12 | All Apologies - 2023 Remaster |
| 1-13 | Gallons Of Rubbing Alcohol Flow Through The Strip - 2023 Remaster |
| 1-14 | Marigold - 2023 Remaster |
| 1-15 | Sappy - 2023 Remaster |
| 1-16 | Moist Vagina - 2023 Remaster |
| 1-17 | I Hate Myself And Want To Die - 2023 Remaster |
| 2-1 | Radio Friendly Unit Shifter - Live In Los Angeles, Great Western Forum - December 30, 1993 |
| 2-2 | Drain You - Live In Los Angeles, Great Western Forum - December 30, 1993 |
| 2-3 | Breed - Live In Los Angeles, Great Western Forum - December 30, 1993 |
| 2-4 | Serve The Servants - Live In Los Angeles, Great Western Forum - December 30, 1993 |
| 2-5 | Come As You Are - Live In Los Angeles, Great Western Forum - December 30, 1993 |
| 2-6 | Smells Like Teen Spirit - Live In Los Angeles, Great Western Forum - December 30, 1993 |
| 2-7 | Sliver - Live In Los Angeles, Great Western Forum - December 30, 1993 |
| 2-8 | Dumb - Live In Los Angeles, Great Western Forum - December 30, 1993 |
| 2-9 | In Bloom - Live In Los Angeles, Great Western Forum - December 30, 1993 |
| 2-10 | About A Girl - Live In Los Angeles, Great Western Forum - December 30, 1993 |
| 2-11 | Lithium - Live In Los Angeles, Great Western Forum - December 30, 1993 |
| 2-12 | Pennyroyal Tea - Live In Los Angeles, Great Western Forum - December 30, 1993 |
| 2-13 | School - Live In Los Angeles, Great Western Forum - December 30, 1993 |
| 2-14 | Polly - Live In Los Angeles, Great Western Forum - December 30, 1993 |
| 2-15 | Frances Farmer Will Have Her Revenge On Seattle - Live In Los Angeles, Great Western Forum - December 30, 1993 |
| 2-16 | Rape Me - Live In Los Angeles, Great Western Forum - December 30, 1993 |
| 2-17 | Territorial Pissings - Live In Los Angeles, Great Western Forum - December 30, 1993 |
| 2-18 | Jesus Doesn't Want Me For A Sunbeam - Live In Los Angeles, Great Western Forum - December 30, 1993 |
| 2-19 | The Man Who Sold The World - Live In Los Angeles, Great Western Forum - December 30, 1993 |
| 2-20 | All Apologies - Live In Los Angeles, Great Western Forum - December 30, 1993 |
| 2-21 | On A Plain - Live In Los Angeles, Great Western Forum - December 30, 1993 |
| 2-22 | Heart-Shaped Box - Live In Los Angeles, Great Western Forum - December 30, 1993 |
| 2-23 | Blew - Live In Los Angeles, Great Western Forum - December 30, 1993 |
| 2-24 | Feedback Jam - Live In Los Angeles, Great Western Forum - December 30, 1993 |
| 3-1 | Radio Friendly Unit Shifter - Live In Seattle, Seattle Center Arena - January 7, 1994 |
| 3-2 | Drain You - Live In Seattle, Seattle Center Arena - January 7, 1994 |
| 3-3 | Breed - Live In Seattle, Seattle Center Arena - January 7, 1994 |
| 3-4 | Serve The Servants - Live In Seattle, Seattle Center Arena - January 7, 1994 |
| 3-5 | Come As You Are - Live In Seattle, Seattle Center Arena - January 7, 1994 |
| 3-6 | Smells Like Teen Spirit - Live In Seattle, Seattle Center Arena - January 7, 1994 |
| 3-7 | Sliver - Live In Seattle, Seattle Center Arena - January 7, 1994 |
| 3-8 | Dumb - Live In Seattle, Seattle Center Arena - January 7, 1994 |
| 3-9 | In Bloom - Live In Seattle, Seattle Center Arena - January 7, 1994 |
| 3-10 | About A Girl - Live In Seattle, Seattle Center Arena - January 7, 1994 |
| 3-11 | Lithium - Live In Seattle, Seattle Center Arena - January 7, 1994 |
| 3-12 | Pennyroyal Tea - Live In Seattle, Seattle Center Arena - January 7, 1994 |
| 3-13 | School - Live In Seattle, Seattle Center Arena - January 7, 1994 |
| 3-14 | Polly - Live In Seattle, Seattle Center Arena - January 7, 1994 |
| 3-15 | Frances Farmer Will Have Her Revenge On Seattle - Live In Seattle, Seattle Center Arena - January 7, 1994 |
| 3-16 | Milk It - Live In Seattle, Seattle Center Arena - January 7, 1994 |
| 3-17 | Rape Me - Live In Seattle, Seattle Center Arena - January 7, 1994 |
| 3-18 | Territorial Pissings - Live In Seattle, Seattle Center Arena - January 7, 1994 |
| 3-19 | Jesus Doesn't Want Me For A Sunbeam - Live In Seattle, Seattle Center Arena - January 7, 1994 |
| 3-20 | The Man Who Sold The World - Live In Seattle, Seattle Center Arena - January 7, 1994 |
| 3-21 | All Apologies - Live In Seattle, Seattle Center Arena - January 7, 1994 |
| 3-22 | On A Plain - Live In Seattle, Seattle Center Arena - January 7, 1994 |
| 3-23 | Scentless Apprentice - Live In Seattle, Seattle Center Arena - January 7, 1994 |
| 3-24 | Heart-Shaped Box - Live In Seattle, Seattle Center Arena - January 7, 1994 |
| 3-25 | Blew - Live In Seattle, Seattle Center Arena - January 7, 1994 |
| 3-26 | Serve The Servants - Live In Rome, Palaghiaccio Di Marino - February 22, 1994 |
| 3-27 | Scentless Apprentice - Live In Rome, Palaghiaccio Di Marino - February 22, 1994 |
| 3-28 | Heart-Shaped Box - Live In Rome, Palaghiaccio Di Marino - February 22, 1994 |
| 3-29 | Very Ape - Live In Rome, Palaghiaccio Di Marino - February 22, 1994 |
| 3-30 | Milk It - Live In Springfield, Springfield Civic Center - November 10, 1993 |
| 3-31 | tourette's - Live In New York, Roseland Ballroom - July 23, 1993 |

