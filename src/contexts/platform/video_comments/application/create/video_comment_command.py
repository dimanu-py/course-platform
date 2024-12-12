from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class VideoCommentCommand:
    id: str
    video_id: str
    author_id: str
    title: str
    content: str
