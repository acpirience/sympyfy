"""

Access_token: used for api call not needing oauth

"""

from datetime import datetime, timedelta


class Access_token:
    def __init__(self, token: str, expires_in: int):
        # Token: token content passed to the API
        # expires_in: duration in seconds of the token validity
        # expiry: datetime when the token becomes invalid

        self.token = token
        self.expiry: datetime = datetime.today() + timedelta(seconds=expires_in)

    def is_valid(self) -> bool:
        # token is invalid if current date > expiry
        return datetime.today() < self.expiry

    def __repr__(self) -> str:
        return f"(Token:'{self.token}', Expiry:'{self.expiry}')"
