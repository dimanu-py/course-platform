import pytest
from expects import expect, equal
from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient

from src.delivery.api.main import app


@pytest.mark.acceptance
class AcceptanceTestConfig:
    def setup_method(self) -> None:
        self.client = TestClient(app)

    def when_a_get_request_is_made_to(self, endpoint: str) -> JSONResponse:
        return self.client.get(endpoint)  # type: ignore

    def when_a_put_request_is_made_to(
        self, endpoint: str, request_body: dict
    ) -> JSONResponse:
        return self.client.put(endpoint, json=request_body)  # type: ignore

    def then_response_should_satisfy(
        self, expected_status_code: int, expected_body: dict, response: JSONResponse
    ) -> None:
        expect(response.status_code).to(equal(expected_status_code))
        expect(response.json()).to(equal(expected_body))
