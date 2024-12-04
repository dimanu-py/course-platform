from src.contexts.content_creation.influencers.application.create_influencer_command import (
    CreateInfluencerCommand,
)
from src.contexts.content_creation.influencers.domain.influencer import Influencer
from src.contexts.content_creation.influencers.domain.influencer_repository import (
    InfluencerRepository,
)


class InfluencerCreator:
    def __init__(self, repository: InfluencerRepository) -> None:
        self._repository = repository

    def __call__(self, command: CreateInfluencerCommand) -> None:
        influencer = Influencer.create(
            id_=command.id_,
            name=command.name,
            username=command.username,
            email=command.email,
        )
        self._repository.save(influencer)
