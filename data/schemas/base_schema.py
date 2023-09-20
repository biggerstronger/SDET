from dataclasses import dataclass


@dataclass
class BaseSchema:
    method: str
    url: str
    headers: dict = None
    body: dict = None
