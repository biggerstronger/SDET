import pytest

from data.schemas.phases_schemas import PhaseRequestSchema
from request_builder.request_builder import PhaseBuilder


class TestA4:

    @pytest.mark.api
    def test_api_add_phase(self, get_bearer_token, create_new_estimate):
        add_phase_response = PhaseBuilder(get_bearer_token).add_phase().prepared_request.add_phase_response(
            create_new_estimate)
        assert (
                add_phase_response.status_code == 200
                and add_phase_response._original == PhaseRequestSchema().templateIds[0]
        )

    @pytest.mark.api
    def test_api_add_custom_phase(self, get_bearer_token, create_new_estimate):
        add_phase_response = PhaseBuilder(get_bearer_token).add_phase(customNames=["test"],
                                                                      templateIds=[]).prepared_request.add_phase_response(
            create_new_estimate)
        assert (
                add_phase_response.status_code == 200
                and add_phase_response.name == "test"
        )

    @pytest.mark.api
    def test_api_delete_phase(self, get_bearer_token, create_new_estimate, add_phase_to_estimate):
        delete_phase_response = PhaseBuilder(get_bearer_token).add_phase().prepared_request.delete_phase_response(
            create_new_estimate, add_phase_to_estimate)
        assert delete_phase_response.status_code == 404
