import json
import os

import requests

from data.schemas.authorize_schema import AuthorizeResponseSchema


class AuthorizeRequest:
    _headers = {"Content-Type": "application/json;charset=utf-8"}
    _url = f"{os.getenv('API_URL')}auth/login"

    def __init__(self) -> None:
        self.request_kwargs = {}

    def add(self, part) -> None:
        self.request_kwargs.update(part)

    def authorize_response(self) -> AuthorizeResponseSchema:
        response = requests.post(url=self._url, headers=self._headers, data=json.dumps(self.request_kwargs), timeout=10)
        return AuthorizeResponseSchema(
            user=response.json().get("user"),
            token=response.json().get("token"),
            expire=response.json().get("expire"),
            status_code=response.status_code,
        )
