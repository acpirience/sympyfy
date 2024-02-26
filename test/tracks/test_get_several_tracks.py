"""

test for sympyfy.get_several_tracks

"""

from sympyfy import Sympyfy


def test_get_known_tracks() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_track_list = test.get_several_tracks(["3EEd6ldsPat620GVYMEhOP", "2fKdsBazcOLLIzDiZUQCih"])

    assert test_track_list

    test_tracks_names = [x.name for x in test_track_list]

    assert "Goo Goo Muck" in test_tracks_names
    assert "Novocaine For The Soul" in test_tracks_names


def test_get_unknown_track() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_tracks_list = test.get_several_tracks(["3EEd6ldsPat620GVYMEhOP", "xyz"])

    assert test_tracks_list
    assert len(test_tracks_list) == 1

    test_tracks_names = [x.name for x in test_tracks_list]

    assert "Goo Goo Muck" in test_tracks_names
    assert "Novocaine For The Soul" not in test_tracks_names
