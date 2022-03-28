import sys

sys.path.append('')

from src.application.use_cases.get_schedules import GetSchedules
from src.infra.factories.json_repository_factory import JsonRepositoryFactory

repository_factory = JsonRepositoryFactory()


class TestGetSchedulesHook:

    def test_should_given_schedules_list(self):
        get_schedules = GetSchedules(repository_factory)
        output = get_schedules.execute()
        assert type(output.schedules) == list
