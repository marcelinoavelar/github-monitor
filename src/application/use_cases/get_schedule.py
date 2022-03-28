from src.application.use_cases.get_schedule_dto import GetScheduleInput, GetScheduleOutput
from src.domanin.factories.repository_factory import RepositoryFactory


class GetSchedule:
    repository_factory: RepositoryFactory

    def __init__(self, repository_factory):
        self.repository_factory = repository_factory.schedule_repository

    def execute(self, _input: GetScheduleInput) -> GetScheduleOutput:
        schedule = self.repository_factory.find(_input.schedule_id)
        return GetScheduleOutput(schedule.user, schedule.repository, schedule.url, schedule.schedule_id)
