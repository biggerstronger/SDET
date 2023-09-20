import pytest

from request_builder.request_builder import AuthorizeBuilder


class TestBuilder:

    @pytest.mark.builder
    def test_builder(self):
        authorize_response = AuthorizeBuilder().login().password().prepared_request.authorize_response()
        assert authorize_response.status_code == 200 and authorize_response.user
