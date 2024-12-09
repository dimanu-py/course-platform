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


class PostgresInfluencerRepository(InfluencerRepository):
    _session_maker: SessionMaker

    def __init__(self, session_maker: SessionMaker) -> None:
        self._session_maker = session_maker

    @override
    def save(self, influencer: Influencer) -> None:
        with self._session_maker.get_session() as session:
            influencer_to_insert = InfluencerModel(**influencer.to_dict())
            session.add(influencer_to_insert)
            session.commit()

    @override
    def search(self, influencer_id: InfluencerId) -> Influencer | None:
        with self._session_maker.get_session() as session:
            influencer = (
                session.query(InfluencerModel)
                .filter(InfluencerModel.id == influencer_id.value)
                .first()
            )

            return (
                Influencer.create(
                    str(influencer.id),
                    influencer.name,  # type: ignore
                    influencer.username,  # type: ignore
                    influencer.email,  # type: ignore
                )
                if influencer
                else None
            )
