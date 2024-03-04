from rich.console import Console

from sympyfy import Sympyfy

console = Console()


def main() -> None:
    spotify = Sympyfy()
    spotify.load_credentials()

    # test = spotify.get_artist("xyz")
    # test = spotify.get_artist("1GhPHrq36VKCY3ucVaZCfo")
    # test = spotify.get_several_artists(["5N5tQ9Dx1h8Od7aRmGj7Fi", "1GhPHrq36VKCY3ucVaZCfo"])
    # test = spotify.get_several_artists(["zzz", "xyz"])
    # test = spotify.get_artist_related_artists("5N5tQ9Dx1h8Od7aRmGj7Fi")
    # test = spotify.get_track("6Ft7UiAv5SCfK7ZkqVmOCQ")
    # test = spotify.get_track("6Ft7UiAv5SCfK7ZkqVmOCQ", "FR")
    # test = spotify.get_album("2ANVost0y2y52ema1E9xAZ")
    # test = spotify.get_several_albums(["2ANVost0y2y52ema1E9xAZ", "3ExyKxlUkqD41I8tQumMDF", "2seoHZbHe4S2fOHRA5Lba9"])
    # test = spotify.get_several_albums(["2ANVost0y2y52ema1E9xAZ", "3ExyKxlUkqD41I8tQumMDF", "2seoHZbHe4S2fOHRA5Lba9"], "FR")
    # test = spotify.get_several_albums(["2ANVost0y2y52ema1E9xAZ", "xyz"])
    # test = spotify.get_artist_top_tracks("066X20Nz7iquqkkCW6Jxy6")
    # test = spotify.get_artist_top_tracks("066X20Nz7iquqkkCW6Jxy6", "FR")
    # test = spotify.get_several_tracks(["3EEd6ldsPat620GVYMEhOP", "2fKdsBazcOLLIzDiZUQCih"])
    # test = spotify.get_track_audio_features("6Ft7UiAv5SCfK7ZkqVmOCQ")
    # test = spotify.get_several_track_audio_features(["3EEd6ldsPat620GVYMEhOP", "2fKdsBazcOLLIzDiZUQCih"])
    # test = spotify.get_artist_albums("7bu3H8JO7d0UbMoVzbo70s")
    # test = spotify.get_several_track_audio_features(["xyz"])
    # test = spotify.get_album_tracks("2ANVost0y2y52ema1E9xAZ")
    # test = spotify.get_new_releases()
    # test = spotify.get_browse_category("dinner")
    # test = spotify.get_several_browse_categories()
    # test = spotify.get_genres()
    # test = spotify.get_user_profile("xxx")
    # test = spotify.get_show("6Ol9sx1lONDxBSffLW9qcZ")
    # test = spotify.get_several_shows(["6Ol9sx1lONDxBSffLW9qcZ", "4GC4FMJmYDDrqJI5t8I1Yy"])
    # test = spotify.get_show_episodes("6Ol9sx1lONDxBSffLW9qcZ", limit=2)
    # test = spotify.get_artist_top_tracks("5N5tQ9Dx1h8Od7aRmGj7Fi", "US")
    # test = spotify.get_episode("62Qq3LRFB2P3P3xSgVFA2U")
    # test = spotify.get_users_follow_playlist("3cEYpjA9oz9GiPac4AsH4n", ["jmperezperez", "thelinmichael", "wizzler"])
    # test = spotify.get_playlist("2LbyMChvxpn1emaIiDKKnT")
    test = spotify.get_playlist_cover_image("2LbyMChvxpn1emaIiDKKnT")

    console.print(test)


if __name__ == "__main__":
    main()
