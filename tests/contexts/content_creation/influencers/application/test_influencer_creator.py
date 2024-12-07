from expects import expect, raise_error

from src.contexts.content_creation.influencers.application.influencer_creator import (
    InfluencerCreator,
)
from src.contexts.content_creation.influencers.domain.invalid_email_format_error import (
    InvalidEmailFormatError,
)
from tests.contexts.content_creation.influencers.domain.create_influencer_command_mother import (
    CreateInfluencerCommandMother,
)
from tests.contexts.content_creation.influencers.domain.influencer_mother import (
    InfluencerMother,
)
from tests.contexts.content_creation.influencers.influencer_module_unit_test_config import (
    InfluencerModuleUnitTestConfig,
)


class TestInfluencerCreator(InfluencerModuleUnitTestConfig):
    def setup_method(self) -> None:
        self.influencer_creator = InfluencerCreator(self.repository)

    def test_should_create_a_valid_influencer(self) -> None:
        command = CreateInfluencerCommandMother.valid()
        influencer_to_save = InfluencerMother.from_request(command)

        self.influencer_creator(command)

        self.should_have_saved(influencer_to_save)

    def test_should_fail_to_create_influencer_with_invalid_id(self) -> None:
        command = CreateInfluencerCommandMother.invalid_id()

        expect(lambda: self.influencer_creator(command)).to(raise_error(ValueError))

    def test_should_fail_to_create_influencer_with_invalid_email(self) -> None:
        command = CreateInfluencerCommandMother.invalid_email()

        expect(lambda: self.influencer_creator(command)).to(
            raise_error(InvalidEmailFormatError)
        )
