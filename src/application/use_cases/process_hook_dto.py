from dataclasses import dataclass


@dataclass
class ProcessHookInput:
    user: str
    repository: list
    url_hook: str
