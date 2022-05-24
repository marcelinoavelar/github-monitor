from abc import ABC, abstractmethod

from src.domain.repositories.github_data_repository import GithubDataRepository
from src.domain.repositories.schedule_repository import ScheduleRepository


class RepositoryFactory(ABC):

    @property
    @abstractmethod
    def github_data_repository(self) -> GithubDataRepository:
        raise NotImplementedError

    @property
    @abstractmethod
    def schedule_repository(self) -> ScheduleRepository:
        raise NotImplementedError
