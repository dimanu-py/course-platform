import pytest

from tests.delivery.api.acceptance_test_config import AcceptanceTestConfig


class TestVideoCreateRoute(AcceptanceTestConfig):
    NO_BODY: dict = {}

    @pytest.mark.xfail
    def test_should_create_a_valid_product(self) -> None:
        request_body = {
            "title": "any_title",
            "description": "any_description",
        }

        response = self.when_a_put_request_is_made_to(
            "/videos/f847bd9c-cee0-4e14-996c-edaf13720c6c", request_body
        )

        self.then_response_should_satisfy(201, self.NO_BODY, response)
