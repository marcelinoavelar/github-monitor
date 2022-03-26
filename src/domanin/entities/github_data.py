import dataclasses
from dataclasses import dataclass, field

from src.domanin.entities.contributor import Contributor
from src.domanin.entities.issue import Issue


@dataclass
class GithubData:
    user: str
    repository: str
    issues: list[Issue] = field(default_factory=list)
    contributors: list[Contributor] = field(default_factory=list)

    def __post_init__(self):
        if len(self.user) < 1:
            raise ValueError("Invalid user")
        if len(self.repository) < 1:
            raise ValueError("Invalid repository")

    def to_json(self):
        return dataclasses.asdict(self)
