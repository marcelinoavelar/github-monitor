import sys
import requests_mock

sys.path.append("")

from src.application.use_cases.process_hook import ProcessHook
from src.application.use_cases.process_hook_dto import ProcessHookInput
from src.infra.factories.in_memory_repository_factory import InMemoryRepositoryFactory

repository_factory = InMemoryRepositoryFactory()


class TestProcessHook:

    def test_should_process_hook(self):
        url_hook = 'https://webhook.site/27c276a1-d034-414d-b0e6-5c1bc70df117'
        _input = ProcessHookInput('linus', 'linux', url_hook)
        process_hook = ProcessHook(repository_factory)
        with requests_mock.Mocker() as mock:
            mock.post(url_hook, status_code=200)
            output = process_hook.execute(_input)
        assert output == 200
