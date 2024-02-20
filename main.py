from sympyfy import Sympyfy


def main() -> None:
    spotify = Sympyfy()
    spotify.load_credentials()

    test = spotify.get_artist("xyz")
    # test = spotify.get_artist("1GhPHrq36VKCY3ucVaZCfo")


if __name__ == "__main__":
    main()
