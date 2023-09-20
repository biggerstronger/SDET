"""
App authorize schema
"""
from dataclasses import dataclass


@dataclass
class AuthorizeRequestSchema:
    login: str = "administrator"
    password: str = "123456"


@dataclass
class AuthorizeResponseSchema:
    token: str
    expire: str
    user: str
    status_code: int
