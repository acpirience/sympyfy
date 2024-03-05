"""

test for sympyfy.make_url

"""

from sympyfy import Sympyfy
from sympyfy.sympyfy import INCLUDE_GROUPS


def test_id() -> None:
    url = "http://test.com/{id}"
    params = {"id": "TEST"}
    test = Sympyfy()._Sympyfy__make_url(url, params)  # type: ignore

    assert test == "http://test.com/TEST"


def test_ids() -> None:
    url = "http://test.com/{ids}"
    params = {"ids": ["TEST1", "TEST2"]}
    test = Sympyfy()._Sympyfy__make_url(url, params)  # type: ignore

    assert test == "http://test.com/TEST1%2CTEST2"


def test_add_include_groups_full() -> None:
    url = "http://test.com"
    params = {"include_groups": INCLUDE_GROUPS}
    test = Sympyfy()._Sympyfy__make_url(url, params)  # type: ignore

    assert test == "http://test.com?include_groups=album%2Csingle%2Cappears_on%2Ccompilation"


def test_add_include_groups_one_missing() -> None:
    url = "http://test.com"
    params = {"include_groups": ["single", "appears_on", "compilation"]}
    test = Sympyfy()._Sympyfy__make_url(url, params)  # type: ignore

    assert test == "http://test.com?include_groups=single%2Cappears_on%2Ccompilation"


def test_add_include_groups_one_ko() -> None:
    url = "http://test.com"
    params = {"include_groups": ["xxx", "single", "appears_on", "compilation"]}
    test = Sympyfy()._Sympyfy__make_url(url, params)  # type: ignore

    assert test == "http://test.com?include_groups=single%2Cappears_on%2Ccompilation"


def test_add_include_groups_all_ko() -> None:
    url = "http://test.com"
    params = {"include_groups": ["xxx", "yyy", "zzz"]}
    test = Sympyfy()._Sympyfy__make_url(url, params)  # type: ignore

    assert test == "http://test.com?include_groups=album%2Csingle%2Cappears_on%2Ccompilation"


def test_add_market_empty() -> None:
    spotify = Sympyfy()
    spotify.load_credentials()

    url = "http://test.com"
    params = {"market": None}
    test = spotify._Sympyfy__make_url(url, params)  # type: ignore

    assert test == "http://test.com"


def test_add_market_incorrect_country() -> None:
    spotify = Sympyfy()
    spotify.load_credentials()

    url = "http://test.com"
    params = {"market": "AZERTY"}
    test = spotify._Sympyfy__make_url(url, params)  # type: ignore

    assert test == "http://test.com"


def test_add_market_correct_country() -> None:
    spotify = Sympyfy()
    spotify.load_credentials()

    url = "http://test.com"
    params = {"market": "FR"}
    test = spotify._Sympyfy__make_url(url, params)  # type: ignore

    assert test == "http://test.com?market=FR"


def test_add_pagination_ok() -> None:
    url = "http://test.com"
    params = {"limit": 20, "offset": 20}
    test = Sympyfy()._Sympyfy__make_url(url, params)  # type: ignore

    assert test == "http://test.com?limit=20&offset=20"


def test_add_pagination_limit_ko() -> None:
    url = "http://test.com"
    params = {"offset": 0, "limit": 0}
    test = Sympyfy()._Sympyfy__make_url(url, params)  # type: ignore

    assert test == "http://test.com?offset=0&limit=1"

    params = {"offset": 0, "limit": 200}
    test = Sympyfy()._Sympyfy__make_url(url, params)  # type: ignore
    assert test == "http://test.com?offset=0&limit=50"


def test_add_pagination_offset_ko() -> None:
    url = "http://test.com"
    params = {"offset": -20, "limit": 1}
    test = Sympyfy()._Sympyfy__make_url(url, params)  # type: ignore

    assert test == "http://test.com?offset=0&limit=1"


def test_add_url_parameter() -> None:
    url = ""
    params = {"test": "tested"}
    test = Sympyfy()._Sympyfy__make_url(url, params)  # type: ignore

    assert test == "?test=tested"


def test_test_add_url_parameter_no_value() -> None:
    url = ""
    params = {"test": None}
    test = Sympyfy()._Sympyfy__make_url(url, params)  # type: ignore

    assert test == ""


def test_sanitize_question_mark() -> None:
    url = "https://www.youtube.com/watch?v=ILwhI3qyl8I&t=3066s"
    params: dict[str, str] = {}
    test = Sympyfy()._Sympyfy__make_url(url, params)  # type: ignore

    assert test == "https://www.youtube.com/watch?v=ILwhI3qyl8I&t=3066s"


def test_sanitize_no_question_mark() -> None:
    url = "https://www.youtube.com/watch&v=ILwhI3qyl8I&t=3066s"
    params: dict[str, str] = {}
    test = Sympyfy()._Sympyfy__make_url(url, params)  # type: ignore

    assert test == "https://www.youtube.com/watch?v=ILwhI3qyl8I&t=3066s"


def test_tunable_track_attributes_invalid() -> None:
    url = ""
    tunable_track_attributes = {"xxx": 0}
    params = {"tunable_track_attributes": tunable_track_attributes}
    test = Sympyfy()._Sympyfy__make_url(url, params)  # type: ignore

    assert test == ""


def test_tunable_track_attributes_valid() -> None:
    url = ""
    tunable_track_attributes = {"target_instrumentalness": 0.1, "min_key": 1}
    params = {"tunable_track_attributes": tunable_track_attributes}
    test = Sympyfy()._Sympyfy__make_url(url, params)  # type: ignore

    assert test == "?target_instrumentalness=0.1&min_key=1"
