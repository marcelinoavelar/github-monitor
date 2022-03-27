import json

import requests

from src.application.use_cases.process_hook_dto import ProcessHookInput, ProcessHookOutput
from src.domanin.factories.repository_factory import RepositoryFactory


class ProcessHook:
    repository_factory: RepositoryFactory

    def __init__(self, repository_factory):
        self.repository_factory = repository_factory.github_data_repository

    def execute(self, _input: ProcessHookInput) -> ProcessHookOutput:
        github_data = self.repository_factory.find(_input.user, _input.repository)
        if not github_data:
            raise ValueError('Not found repository')
        payload = json.dumps(github_data.to_json())
        request = requests.post(_input.url_hook, data=payload)
        if not request:
            raise ValueError('Fail request to hook')
        return ProcessHookOutput('Success hook process')
