from dataclasses import dataclass


@dataclass
class ScheduleHookInput:
    user: str
    repository: str
    url_hook: str

    def __post_init__(self):
        if len(self.user) < 1:
            raise ValueError('Invalid user')
        if len(self.repository) < 1:
            raise ValueError('Invalid repository')
        if len(self.url_hook) < 1:
            raise ValueError('Invalid url_hook')


@dataclass
class ScheduleHookOutput:
    message: str
    schedule_id: str

    def __post_init__(self):
        if len(self.message) < 1:
            raise ValueError('Invalid message')
