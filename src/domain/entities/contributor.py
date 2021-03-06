from dataclasses import dataclass, field


@dataclass
class Contributor:
    username: str
    name: str = field(default_factory=str)
    qtd_commits: int = field(default_factory=int)

    def __post_init__(self):
        if len(self.username) < 1:
            raise ValueError('Invalid username')
