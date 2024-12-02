import pytest
from expects import expect, equal
from fastapi.testclient import TestClient
from fastapi.responses import JSONResponse

from src.delivery.api.health_check import router


@pytest.mark.acceptance
class TestHealthCheck:
    def setup_method(self) -> None:
        self.client = TestClient(router)

    def test_should_check_application_health(self):
        expected_code_status = 200
        expected_body = {"status": "Healthy"}

        response = self.when_a_request_is_made_to("/health-check")

        self.then_response_should_satisfy(expected_code_status, expected_body, response)

    def when_a_request_is_made_to(self, endpoint: str) -> JSONResponse:
        return self.client.get(endpoint)  # type: ignore

    def then_response_should_satisfy(
        self, expected_status_code: int, expected_body: dict, response: JSONResponse
    ) -> None:
        expect(response.status_code).to(equal(expected_status_code))
        expect(response.json()).to(equal(expected_body))
