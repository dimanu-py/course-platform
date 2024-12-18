from dataclasses import dataclass, asdict


@dataclass
class VideoTotalCommentsResponse:
    total_comments: int

    def model_dump(self) -> dict:
        return asdict(self)
