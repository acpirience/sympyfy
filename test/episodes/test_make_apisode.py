"""

test for sympyfy.make_episode

"""
from sympyfy import Sympyfy


def test_make_episode() -> None:
    dict_content = {
        "audio_preview_url": "https://podz-content.spotifycdn.com/audio/clips/7zbTPaupCVUwal4VphJ4Cc/clip_1496360_1551350.mp3",
        "description": "You've built an awesome set of APIs and you have a wide array of devices and clients using them. Then you need to upgrade an end point or change them in a meaningful way. Now what? That's the conversation I dive into over the next hour with Stanislav Zmiev. We're talking about Versioning APIs.  Episode sponsors  Neo4j Sentry Error Monitoring, Code TALKPYTHON Talk Python Courses  Links from the show  Stanislav Zmiev: github.com Monite: monite.com Cadwyn: github.com Stripe API Versioning: stripe.com API Versioning NOtes: github.com FastAPI-Versioning: github.com Flask-Rebar: readthedocs.io Django Rest Framework Versioning: django-rest-framework.org pytest-fixture-classes: github.com Watch this episode on YouTube: youtube.com Episode transcripts: talkpython.fm  --- Stay in touch with us --- Subscribe to us on YouTube: youtube.com Follow Talk Python on Mastodon: talkpython Follow Michael on Mastodon: mkennedy",
        "duration_ms": 3766073,
        "explicit": False,
        "external_urls": {"spotify": "https://open.spotify.com/episode/5XG2gdUW0YJ6iLmK7F2nHM"},
        "href": "https://api.spotify.com/v1/episodes/5XG2gdUW0YJ6iLmK7F2nHM",
        "html_description": 'You&#39;ve built an awesome set of APIs and you have a wide array of devices and clients using them. Then you need to upgrade an end point or change them in a meaningful way. Now what? That&#39;s the conversation I dive into over the next hour with Stanislav Zmiev. We&#39;re talking about Versioning APIs.<br /><br/><br /><br/>Episode sponsors<br /><br/><br /><br/><a href="https://talkpython.fm/neo4j" rel="nofollow">Neo4j</a><br /><br/><a href="https://talkpython.fm/sentry" rel="nofollow">Sentry Error Monitoring, Code TALKPYTHON</a><br /><br/><a href="https://talkpython.fm/training" rel="nofollow">Talk Python Courses</a><br /><br/><br /><br/>Links from the show<br /><br/><br /><br/>Stanislav Zmiev: <a href="https://github.com/zmievsa" rel="nofollow">github.com</a><br /><br/>Monite: <a href="https://monite.com" rel="nofollow">monite.com</a><br /><br/>Cadwyn: <a href="https://github.com/zmievsa/cadwyn" rel="nofollow">github.com</a><br /><br/>Stripe API Versioning: <a href="https://stripe.com/blog/api-versioning" rel="nofollow">stripe.com</a><br /><br/>API Versioning NOtes: <a href="https://github.com/zmievsa/talks/blob/main/api_versioning.md" rel="nofollow">github.com</a><br /><br/>FastAPI-Versioning: <a href="https://github.com/DeanWay/fastapi-versioning" rel="nofollow">github.com</a><br /><br/>Flask-Rebar: <a href="https://flask-rebar.readthedocs.io/en/latest/quickstart/api_versioning.html" rel="nofollow">readthedocs.io</a><br /><br/>Django Rest Framework Versioning: <a href="https://www.django-rest-framework.org/api-guide/versioning/" rel="nofollow">django-rest-framework.org</a><br /><br/>pytest-fixture-classes: <a href="https://github.com/zmievsa/pytest-fixture-classes" rel="nofollow">github.com</a><br /><br/>Watch this episode on YouTube: <a href="https://www.youtube.com/watch?v&#61;_jmLqOSKIJU" rel="nofollow">youtube.com</a><br /><br/>Episode transcripts: <a href="https://talkpython.fm/episodes/transcript/450/versioning-web-apis-in-python" rel="nofollow">talkpython.fm</a><br /><br/><br /><br/>--- Stay in touch with us ---<br /><br/>Subscribe to us on YouTube: <a href="https://talkpython.fm/youtube" rel="nofollow">youtube.com</a><br /><br/>Follow Talk Python on Mastodon: <a href="https://fosstodon.org/web/&#64;talkpython" rel="nofollow">talkpython</a><br /><br/>Follow Michael on Mastodon: <a href="https://fosstodon.org/web/&#64;mkennedy" rel="nofollow">mkennedy</a><br />',
        "id": "5XG2gdUW0YJ6iLmK7F2nHM",
        "images": [
            {
                "height": 640,
                "url": "https://i.scdn.co/image/ab6765630000ba8ab5c9ca9fb91b19eb5dc7367d",
                "width": 640,
            },
            {
                "height": 300,
                "url": "https://i.scdn.co/image/ab67656300005f1fb5c9ca9fb91b19eb5dc7367d",
                "width": 300,
            },
            {
                "height": 64,
                "url": "https://i.scdn.co/image/ab6765630000f68db5c9ca9fb91b19eb5dc7367d",
                "width": 64,
            },
        ],
        "is_externally_hosted": False,
        "is_playable": True,
        "language": "en-US",
        "languages": ["en-US"],
        "name": "#450: Versioning Web APIs in Python",
        "release_date": "2024-02-22",
        "release_date_precision": "day",
        "type": "episode",
        "uri": "spotify:episode:5XG2gdUW0YJ6iLmK7F2nHM",
        "restrictions": {"reason": "test"},
    }

    test_episode = Sympyfy()._Sympyfy__make_episode(dict_content)  # type: ignore

    assert test_episode.name == "#450: Versioning Web APIs in Python"
    assert test_episode.duration_ms == 3766073
