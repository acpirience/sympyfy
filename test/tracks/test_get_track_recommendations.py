"""

test for sympyfy.get_track_recommendations

"""

from sympyfy import Sympyfy


def test_get_track_recommendations() -> None:
    test = Sympyfy()
    test.load_credentials()

    test_reco = test.get_track_recommendations(
        limit=2,
        seed_artists=["5Ho1vKl1Uz8bJlk4vbmvmf"],
        seed_genres=["techno", "electro"],
        seed_tracks=["7sovMMhuknCR0PHianjiEq"],
        tunable_track_attributes={"min_energy": 0.6, "max_energy": 1},
    )

    assert test_reco and len(test_reco.seeds) == 4
