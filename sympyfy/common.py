"""

common classes used by other objects

"""

from dataclasses import dataclass


@dataclass
class Image:
    url: str
    height: int
    width: int
