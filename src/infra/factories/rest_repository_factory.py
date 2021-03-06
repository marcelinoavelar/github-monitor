from abc import ABC

from src.domain.factories.repository_factory import RepositoryFactory
from src.infra.repositories.rest.github_data_rest_repository import GithubDataRestRepository
from src.infra.repositories.rest.schedule_rest_repository import ScheduleJsonRepository


class RestRepositoryFactory(RepositoryFactory, ABC):

    @property
    def github_data_repository(self):
        return GithubDataRestRepository()

    @property
    def schedule_repository(self) -> ScheduleJsonRepository:
        return ScheduleJsonRepository()
