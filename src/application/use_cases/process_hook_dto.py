from dataclasses import dataclass


@dataclass
class ProcessHookInput:
    user: str
    repository: list
    url_hook: str

    def __post_init__(self):
        if len(self.user) < 1:
            raise ValueError('Invalid username')
        if len(self.repository) < 1:
            raise ValueError('Invalid name')
        if len(self.url_hook) < 1:
            raise ValueError('Invalid url hook')


@dataclass
class ProcessHookOutput:
    message: str

    def __post_init__(self):
        if len(self.message) < 1:
            raise ValueError('Invalid username')
