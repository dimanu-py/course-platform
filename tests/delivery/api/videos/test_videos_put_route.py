import pytest
from expects import expect, equal
from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient

from src.delivery.api.videos.videos_put_route import router


@pytest.mark.acceptance
class TestVideosPutRoute:
    NO_BODY: dict = {}

    def setup_method(self) -> None:
        self.client = TestClient(router)

    def test_should_create_a_valid_product(self) -> None:
        request_body = {
            "title": "any_title",
            "description": "any_description",
        }

        response = self.when_a_request_is_made_to(
            "/videos/f847bd9c-cee0-4e14-996c-edaf13720c6c", request_body
        )

        self.then_response_should_satisfy(201, self.NO_BODY, response)

    def when_a_request_is_made_to(
        self, endpoint: str, request_body: dict
    ) -> JSONResponse:
        return self.client.put(endpoint, json=request_body)  # type: ignore

    def then_response_should_satisfy(
        self, expected_status_code: int, expected_body: dict, response: JSONResponse
    ):
        expect(response.status_code).to(equal(expected_status_code))
        expect(response.json()).to(equal(expected_body))
