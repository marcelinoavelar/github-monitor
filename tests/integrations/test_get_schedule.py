import sys

import pytest

sys.path.append('')

from src.application.use_cases.get_schedule import GetSchedule
from src.application.use_cases.get_schedule_dto import GetScheduleInput
from src.infra.factories.in_memory_repository_factory import InMemoryRepositoryFactory

repository_factory = InMemoryRepositoryFactory()


class TestProcessHook:

    def test_should_given_schedule_by_schedule_id(self):
        _input = GetScheduleInput('abc')
        get_schedule = GetSchedule(repository_factory)
        output = get_schedule.execute(_input)
        assert output.user == 'a'

    def test_should_not_given_not_found_schedule(self):
        with pytest.raises(ValueError, match='Not found schedule'):
            _input = GetScheduleInput('xpto')
            get_schedule = GetSchedule(repository_factory)
            get_schedule.execute(_input)

