from dataclasses import dataclass


@dataclass
class GetScheduleInput:
    schedule_id: str

    def __post_init__(self):
        if len(self.schedule_id) < 1:
            raise ValueError('Invalid schedule_id')


@dataclass
class GetScheduleOutput:
    user: str
    repository: str
    url: str
    schedule_id: str

    def __post_init__(self):
        if len(self.user) < 1:
            raise ValueError('Invalid user')
        if len(self.repository) < 1:
            raise ValueError('Invalid repository')
        if len(self.url) < 1:
            raise ValueError('Invalid url')
        if len(self.schedule_id) < 1:
            raise ValueError('Invalid url')