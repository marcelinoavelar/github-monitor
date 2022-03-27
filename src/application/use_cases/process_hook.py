import json

import requests

from src.application.use_cases.process_hook_dto import ProcessHookInput
from src.domanin.factories.repository_factory import RepositoryFactory


class ProcessHook:
    repository_factory: RepositoryFactory

    def __init__(self, repository_factory):
        self.repository_factory = repository_factory.github_data_repository

    def execute(self, _input: ProcessHookInput):
        github_data = self.repository_factory.find(_input.user, _input.repository)
        if not github_data:
            return {'message': 'Not found'}
        payload = json.dumps(github_data.to_json())
        request = requests.post(_input.url_hook, data=payload)
        return request.status_code
