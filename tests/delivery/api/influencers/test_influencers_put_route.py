from tests.delivery.api.acceptance_test_config import AcceptanceTestConfig


class TestInfluencersPutRoute(AcceptanceTestConfig):
    NO_BODY: dict = {}

    def test_should_create_a_valid_influencer(self) -> None:
        request_body = {
            "name": "Diego",
            "username": "dimanu",
            "email": "dimanu@py.com",
        }

        response = self.when_a_put_request_is_made_to(
            "/influencers/05fbc052-7c8e-4d99-824b-ae469f2bc80e", request_body
        )

        self.then_response_should_satisfy(201, self.NO_BODY, response)
