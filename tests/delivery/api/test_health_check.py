from tests.delivery.api.acceptance_test_config import AcceptanceTestConfig


class TestHealthCheck(AcceptanceTestConfig):
    def test_should_check_application_health(self):
        expected_code_status = 200
        expected_body = {"status": "Healthy"}

        response = self.when_a_get_request_is_made_to("/health-check")

        self.then_response_should_satisfy(expected_code_status, expected_body, response)
