from sympyfy import Sympyfy


def main() -> None:
    spotify = Sympyfy()
    spotify.load_credentials()

    # test = spotify.get_artist("xyz")
    # test = spotify.get_artist("1GhPHrq36VKCY3ucVaZCfo")
    # test = spotify.get_several_artists(["5N5tQ9Dx1h8Od7aRmGj7Fi", "xyz"])
    # test = spotify.get_several_artists(["zzz", "xyz"])
    # test = spotify.get_artist_related_artists("5N5tQ9Dx1h8Od7aRmGj7Fi")
    test = spotify.get_track("6Ft7UiAv5SCfK7ZkqVmOCQ")
    # test = spotify.get_several_albums(["2ANVost0y2y52ema1E9xAZ", "3ExyKxlUkqD41I8tQumMDF", "2seoHZbHe4S2fOHRA5Lba9"])
    # test = spotify.get_artist_top_tracks("066X20Nz7iquqkkCW6Jxy6", "us")

    print("*" * 20)
    print(f"{test=}")


if __name__ == "__main__":
    main()
