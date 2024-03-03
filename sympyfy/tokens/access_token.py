"""

Access_token: used for api call not needing oauth

"""

import json
from datetime import datetime, timedelta


class Access_token:
    def __init__(self, json_content: bytes) -> None:
        # Token: token content passed to the API
        # expiry: datetime when the token becomes invalid
        response_json = json.loads(json_content)
        self._token = response_json["access_token"]
        self._expiry: datetime = datetime.today() + timedelta(seconds=response_json["expires_in"])

    @property
    def token(self) -> str:
        return self._token

    @property
    def expiry(self) -> datetime:
        return self._expiry

    @property
    def headers(self) -> dict[str, str]:
        return {"Authorization": "Bearer " + self.token}

    def is_valid(self) -> bool:
        # token is invalid if current date > expiry
        return datetime.today() < self.expiry

    def __repr__(self) -> str:
        return f"(Token:'{self.token}', Expiry:'{self.expiry}')"
