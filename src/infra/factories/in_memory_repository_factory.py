from abc import ABC

from src.domain.factories.repository_factory import RepositoryFactory
from src.domain.repositories.schedule_repository import ScheduleRepository
from src.infra.repositories.in_memory.github_data_in_memory_repository import GithubDataInMemoryRepository
from src.infra.repositories.in_memory.schedule_in_memory_repository import ScheduleInMemoryRepository


class InMemoryRepositoryFactory(RepositoryFactory, ABC):

    @property
    def github_data_repository(self) -> GithubDataInMemoryRepository:
        return GithubDataInMemoryRepository()

    @property
    def schedule_repository(self) -> ScheduleRepository:
        return ScheduleInMemoryRepository()
