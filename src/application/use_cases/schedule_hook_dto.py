from dataclasses import dataclass


@dataclass
class ScheduleHookInput:
    user: str
    repository: str
    url: str

    def __post_init__(self):
        if len(self.user) < 1:
            raise ValueError('Invalid user')
        if len(self.repository) < 1:
            raise ValueError('Invalid repository')
        if len(self.url) < 1:
            raise ValueError('Invalid url')


@dataclass
class ScheduleHookOutput:
    message: str

    def __post_init__(self):
        if len(self.message) < 1:
            raise ValueError('Invalid message')
