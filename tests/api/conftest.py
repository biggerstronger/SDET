"""
Conftest for API tests
"""

import os

import pytest
import requests

from api_helper.estimates_requests import EstimatesRequests
from request_builder.request_builder import PhaseBuilder
from request_builder.request_builder import AuthorizeBuilder


@pytest.fixture()
def get_bearer_token() -> str:
    return AuthorizeBuilder().login().password().prepared_request.authorize_response().token


@pytest.fixture()
def get_moderator_role_id(get_bearer_token) -> str | None:
    headers = {"Authorization": f"Bearer {get_bearer_token}"}
    content = requests.get(
        url=os.getenv("API_URL") + "roles",
        headers=headers,
        timeout=10,
    ).json().get("content")
    for role in content:
        if role.get("name") == "moderator":
            return role.get("_id")
        continue
    return None


@pytest.fixture()
def get_estimator_role_id(get_bearer_token) -> str | None:
    headers = {"Authorization": f"Bearer {get_bearer_token}"}
    content = requests.get(
        url=os.getenv("API_URL") + "roles",
        headers=headers,
        timeout=10,
    ).json().get("content")
    for role in content:
        if role.get("name") == "estimator":
            return role.get("_id")
        continue
    return None


@pytest.fixture()
def create_new_estimate(get_bearer_token) -> str:
    return EstimatesRequests(get_bearer_token).create_estimate()._id


@pytest.fixture()
def add_phase_to_estimate(get_bearer_token, create_new_estimate) -> str:
    return PhaseBuilder(get_bearer_token).add_phase().prepared_request.add_phase_response(create_new_estimate)._original
