from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class FindVideoCommentCounterQuery:
    video_id: str
