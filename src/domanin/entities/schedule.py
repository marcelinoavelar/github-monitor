from dataclasses import dataclass, field


@dataclass
class Schedule:
    user: str
    repository: str
    url: str
    schedule_id: str = field(default_factory=str)

    def __post_init__(self):
        if len(self.user) < 1:
            raise ValueError('Invalid user')
        if len(self.repository) < 1:
            raise ValueError('Invalid repository')
        if len(self.url) < 1:
            raise ValueError('Invalid url')
