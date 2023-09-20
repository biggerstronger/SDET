from dataclasses import dataclass


@dataclass()
class CreateRequestSchema:
    locale: str = "ru"


@dataclass()
class CreateResponseSchema:
    _id: str
    status_code: int


@dataclass()
class CopyResponseSchema:
    _id: str
    name: str
