from src.contexts.content_creation.influencers.application.create_influencer_command import (
    CreateInfluencerCommand,
)
from src.contexts.content_creation.influencers.domain.influencer import Influencer
from tests.contexts.content_creation.influencers.domain.influencer_email_mother import (
    InfluencerEmailMother,
)
from tests.contexts.content_creation.influencers.domain.influencer_id_mother import (
    InfluencerIdMother,
)
from tests.contexts.content_creation.influencers.domain.influencer_name_mother import (
    InfluencerNameMother,
)
from tests.contexts.content_creation.influencers.domain.influencer_username_mother import (
    InfluencerUsernameMother,
)


class InfluencerMother:
    @classmethod
    def from_request(cls, command: CreateInfluencerCommand) -> Influencer:
        return Influencer.create(
            command.id_, command.name, command.username, command.email
        )

    @classmethod
    def create(cls) -> Influencer:
        return Influencer(
            InfluencerIdMother.create(),
            InfluencerNameMother.create(),
            InfluencerUsernameMother.create(),
            InfluencerEmailMother.create(),
        )
