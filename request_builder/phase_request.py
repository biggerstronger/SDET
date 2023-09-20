import json
import os

import requests

from data.schemas.phases_schemas import PhaseResponseSchema


class PhaseRequest:
    _url = f"{os.getenv('API_URL')}estimates/" + "{estimate_id}/phases/"

    def __init__(self, token) -> None:
        self._headers = {"Content-Type": "application/json;charset=utf-8", "Authorization": f"Bearer {token}"}
        self.request_kwargs = {}

    def add(self, part) -> None:
        self.request_kwargs.update(part)

    def add_phase_response(self, estimate_id) -> PhaseResponseSchema:
        response = requests.post(url=self._url.format(estimate_id=estimate_id), headers=self._headers,
                                 data=json.dumps(self.request_kwargs), timeout=10)
        return PhaseResponseSchema(
            _original=response.json()[-1].get("_original"),
            name=response.json()[-1].get("name"),
            created=response.json()[-1].get("created"),
            status_code=response.status_code,
        )

    def delete_phase_response(self, estimate_id, phase_id) -> requests.Response:
        requests.delete(
            url=self._url.format(estimate_id=estimate_id) + phase_id,
            headers=self._headers,
            timeout=10,
        )
        return requests.get(
            url=self._url.format(estimate_id=estimate_id) + phase_id,
            headers=self._headers,
            timeout=10,
        )
