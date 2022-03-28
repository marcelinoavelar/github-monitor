from abc import ABC, abstractmethod

from src.domanin.repositories.github_data_repository import GithubDataRepository
from src.domanin.repositories.schedule_repository import ScheduleRepository


class RepositoryFactory(ABC):

    @property
    @abstractmethod
    def github_data_repository(self) -> GithubDataRepository:
        raise NotImplementedError

    @property
    @abstractmethod
    def schedule_repository(self) -> ScheduleRepository:
        raise NotImplementedError
