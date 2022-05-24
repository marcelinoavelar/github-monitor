from src.application.use_cases.get_schedules_dto import GetSchedulesOutput
from src.domain.factories.repository_factory import RepositoryFactory


class GetSchedules:
    repository_factory: RepositoryFactory

    def __init__(self, repository_factory):
        self.repository_factory = repository_factory.schedule_repository

    def execute(self, ) -> GetSchedulesOutput:
        schedules = self.repository_factory.all()
        return GetSchedulesOutput(schedules)
