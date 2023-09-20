import os

import requests
from data.schemas.change_role_schema import ChangeRoleResponseSchema


class ChangeRoleRequest:
    role_url = os.getenv("API_URL") + "users/578641fbc44c56220b15e48c/role/"

    def __init__(self, token):
        self._headers = {"Authorization": f"Bearer {token}"}

    def change_role(self, role_id) -> ChangeRoleResponseSchema:
        response = requests.put(url=self.role_url + role_id, headers=self._headers, timeout=10)
        return ChangeRoleResponseSchema(
            role_name=response.json().get("role").get("name"),
            status_code=response.status_code,
        )
