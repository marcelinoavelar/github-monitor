import sys

import pytest

sys.path.append('')

from src.application.use_cases.schedule_hook import ScheduleHook
from src.application.use_cases.schedule_hook_dto import ScheduleHookInput
from src.infra.factories.in_memory_repository_factory import InMemoryRepositoryFactory

repository_factory = InMemoryRepositoryFactory()


class TestProcessHook:

    def test_should_schedule_hook(self):
        _input = ScheduleHookInput('linus', 'linux', 'https://webhook.webhook/123456789')
        schedule_hook = ScheduleHook(repository_factory)
        output = schedule_hook.execute(_input)
        assert output.message == 'Schedule create with success'

    def test_not_should_schedule_hook_less_user(self):
        with pytest.raises(ValueError, match='Invalid user'):
            _input = ScheduleHookInput('', 'linux', 'https://webhook.webhook/123456789')
            schedule_hook = ScheduleHook(repository_factory)
            schedule_hook.execute(_input)

    def test_not_should_schedule_hook_less_repository(self):
        with pytest.raises(ValueError, match='Invalid repository'):
            _input = ScheduleHookInput('linus', '', 'https://webhook.webhook/123456789')
            schedule_hook = ScheduleHook(repository_factory)
            schedule_hook.execute(_input)

    def test_not_should_schedule_hook_less_url(self):
        with pytest.raises(ValueError, match='Invalid url'):
            _input = ScheduleHookInput('linus', 'linux', '')
            schedule_hook = ScheduleHook(repository_factory)
            schedule_hook.execute(_input)
