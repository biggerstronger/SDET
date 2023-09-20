import dataclasses
import json
import os

import requests

from data.schemas.authorize_schema import AuthorizeRequestSchema, AuthorizeResponseSchema


class AuthorizeRequest:
    url = os.getenv("API_URL") + "auth/login"
    headers = {"Content-Type": "application/json;charset=utf-8"}

    def authorize(self, authorize_data: AuthorizeRequestSchema) -> AuthorizeResponseSchema:
        body = json.dumps(
            dataclasses.asdict(authorize_data),
        )
        response = requests.post(url=self.url, headers=self.headers, data=body, timeout=10)
        return AuthorizeResponseSchema(
            user=response.json().get("user"),
            token=response.json().get("token"),
            expire=response.json().get("expire"),
            status_code=response.status_code,
        )
