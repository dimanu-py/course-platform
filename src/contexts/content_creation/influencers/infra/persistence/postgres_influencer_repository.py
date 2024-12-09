from typing import override

from src.contexts.content_creation.influencers.domain.influencer import Influencer
from src.contexts.content_creation.influencers.domain.influencer_id import InfluencerId
from src.contexts.content_creation.influencers.domain.influencer_repository import (
    InfluencerRepository,
)
from src.contexts.content_creation.influencers.infra.persistence.sqlalchemy.influencer_model import (
    InfluencerModel,
)
from src.contexts.content_creation.shared.infra.sqlalchemy.session_maker import (
    SessionMaker,
)
from src.contexts.content_creation.shared.infra.sqlalchemy.sqlalchemy_repository import (
    SqlAlchemyRepository,
)


class PostgresInfluencerRepository(
    SqlAlchemyRepository[InfluencerModel], InfluencerRepository
):
    _session_maker: SessionMaker

    def __init__(self, session_maker: SessionMaker) -> None:
        super().__init__(session_maker=session_maker, model_class=InfluencerModel)

    @override
    def save(self, influencer: Influencer) -> None:
        self.persist(influencer)

    @override
    def search(self, influencer_id: InfluencerId) -> Influencer | None:
        return self.search_by_id(influencer_id)
