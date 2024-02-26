"""

test for common.add_market

"""

from sympyfy.common import sanitize


def test_sanitize_question_mark() -> None:
    test = sanitize("https://www.youtube.com/watch?v=ILwhI3qyl8I&t=3066s")

    assert test == "https://www.youtube.com/watch?v=ILwhI3qyl8I&t=3066s"


def test_sanitize_no_question_mark() -> None:
    test = sanitize("https://www.youtube.com/watch&v=ILwhI3qyl8I&t=3066s")

    assert test == "https://www.youtube.com/watch?v=ILwhI3qyl8I&t=3066s"


def test_sanitize_no_tail() -> None:
    test = sanitize("https://www.youtube.com")

    assert test == "https://www.youtube.com"
