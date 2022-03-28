from abc import ABC

from src.domanin.factories.repository_factory import RepositoryFactory
from src.domanin.repositories.schedule_repository import ScheduleRepository
from src.infra.repositories.json.github_data_json_repository import GithubDataJsonRepository
from src.infra.repositories.json.schedule_json_repository import ScheduleJsonRepository


class JsonRepositoryFactory(RepositoryFactory, ABC):

    @property
    def github_data_repository(self) -> GithubDataJsonRepository:
        return GithubDataJsonRepository()

    @property
    def schedule_repository(self) -> ScheduleJsonRepository:
        return ScheduleJsonRepository()
