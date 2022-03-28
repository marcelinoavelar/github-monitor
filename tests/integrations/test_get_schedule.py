import sys

sys.path.append('')

import pytest

from src.application.use_cases.get_schedule import GetSchedule
from src.application.use_cases.get_schedule_dto import GetScheduleInput
from src.application.use_cases.schedule_hook import ScheduleHook
from src.application.use_cases.schedule_hook_dto import ScheduleHookInput
from src.infra.factories.json_repository_factory import JsonRepositoryFactory

repository_factory = JsonRepositoryFactory()


class TestGetScheduleHook:

    def test_should_given_schedule_by_schedule_id(self):
        input_schedule = ScheduleHookInput('linus', 'linux', 'https://webhook.webhook/123456789')
        schedule_hook_user_case = ScheduleHook(repository_factory)
        output_schedule = schedule_hook_user_case.execute(input_schedule)

        input_get_schedule = GetScheduleInput(output_schedule.schedule_id)
        print(input_get_schedule.schedule_id)

        get_schedule_use_case = GetSchedule(repository_factory)
        output_get_schedule = get_schedule_use_case.execute(input_get_schedule)
        assert output_get_schedule.schedule_id == output_schedule.schedule_id

    # def test_should_not_given_not_found_schedule(self):
    #     with pytest.raises(ValueError, match='Not found schedule'):
    #         _input = GetScheduleInput('xpto')
    #         get_schedule = GetSchedule(repository_factory)
    #         get_schedule.execute(_input)
