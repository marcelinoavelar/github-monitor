import sys

import pytest
import requests_mock

sys.path.append('')

from src.application.use_cases.process_hook import ProcessHook
from src.application.use_cases.process_hook_dto import ProcessHookInput
from src.infra.factories.in_memory_repository_factory import InMemoryRepositoryFactory

repository_factory = InMemoryRepositoryFactory()


class TestProcessHook:

    def test_should_process_hook(self):
        url_hook = 'https://webhook.webhook/rando-web-hook'
        _input = ProcessHookInput('linus', 'linux', url_hook)
        process_hook = ProcessHook(repository_factory)
        with requests_mock.Mocker() as mock:
            mock.post(url_hook, status_code=200)
            output = process_hook.execute(_input)
        assert output.message == "Success hook process"

    def test_should_process_hook_with_not_foun_repo_return(self):
        url_hook = 'https://webhook.webhook/rando-web-hook'
        _input = ProcessHookInput('not-found', 'not-found', url_hook)
        process_hook = ProcessHook(repository_factory)
        with requests_mock.Mocker() as mock:
            mock.post(url_hook, status_code=200)
            with pytest.raises(ValueError, match='Not found repository'):
                output = process_hook.execute(_input)

    def test_not_should_process_hook_with_invalid_hook(self):
        url_hook = 'https://webhook.webhook/rando-web-hook'
        _input = ProcessHookInput('linus', 'linux', url_hook)
        process_hook = ProcessHook(repository_factory)
        with requests_mock.Mocker() as mock:
            mock.post(url_hook, status_code=404)
            with pytest.raises(ValueError, match='Fail request to hook'):
                output = process_hook.execute(_input)
