from dataclasses import dataclass, field


@dataclass
class Issue:
    title: str
    author: str
    labels: list[str] = field(default_factory=list)

    def __post_init__(self):
        if len(self.title) < 1:
            raise ValueError("Invalid title")
        if len(self.author) < 1:
            raise ValueError("Invalid author")
