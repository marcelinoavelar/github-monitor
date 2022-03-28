import uuid

from src.application.use_cases.schedule_hook_dto import ScheduleHookInput, ScheduleHookOutput
from src.domanin.entities.schedule import Schedule
from src.domanin.factories.repository_factory import RepositoryFactory


class ScheduleHook:
    repository_factory: RepositoryFactory

    def __init__(self, repository_factory):
        self.repository_factory = repository_factory.schedule_repository

    def execute(self, _input: ScheduleHookInput) -> ScheduleHookOutput:
        schedule_id = str(uuid.uuid4())
        schedule = Schedule(_input.user, _input.repository, _input.url_hook, schedule_id)
        self.repository_factory.save(schedule)
        return ScheduleHookOutput('Schedule create with success', schedule_id)
