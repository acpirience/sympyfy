from sympyfy import Sympyfy


def main() -> None:
    spotify = Sympyfy()
    spotify.load_credentials()

    # test = spotify.get_artist("xyz")
    # test = spotify.get_artist("1GhPHrq36VKCY3ucVaZCfo")
    # test = spotify.get_several_artists(["5N5tQ9Dx1h8Od7aRmGj7Fi", "xyz"])
    test = spotify.get_several_artists(["zzz", "xyz"])
    # test = spotify.get_artist_related_artists("5N5tQ9Dx1h8Od7aRmGj7Fi")

    print(f"{test=}")


if __name__ == "__main__":
    main()
