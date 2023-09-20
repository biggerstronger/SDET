import dataclasses
import json
import os

import requests

from data.schemas.estimates_schema import CreateRequestSchema, CreateResponseSchema, CopyResponseSchema


class EstimatesRequests:
    estimates_url = os.getenv("API_URL") + "estimates/"

    def __init__(self, token):
        self._headers = {"Content-Type": "application/json;charset=utf-8", "Authorization": f"Bearer {token}"}

    def create_estimate(self) -> CreateResponseSchema:
        body = json.dumps(
            dataclasses.asdict(CreateRequestSchema()),
        )
        response = requests.post(url=self.estimates_url, headers=self._headers, data=body, timeout=10)
        return CreateResponseSchema(
            _id=response.json().get("_id"),
            status_code=response.status_code,
        )

    def create_estimate_json(self) -> requests.Response:
        body = json.dumps(
            dataclasses.asdict(CreateRequestSchema()),
        )
        return requests.post(url=self.estimates_url, headers=self._headers, data=body, timeout=10).json()

    def delete_estimate(self, estimate_id: str) -> str:
        response = requests.delete(url=self.estimates_url + estimate_id, headers=self._headers, timeout=10)
        return response.text

    def copy_estimate(self, estimate_id: str) -> CopyResponseSchema:
        response = requests.post(url=self.estimates_url + estimate_id + "/copy", headers=self._headers, timeout=10)
        return CopyResponseSchema(name=response.json().get("name"), _id=response.json().get("_id"))
