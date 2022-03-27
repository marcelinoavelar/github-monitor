from abc import ABC, abstractmethod

from src.domanin.repositories.github_data_repository import GithubDataRepository


class RepositoryFactory(ABC):

    @property
    @abstractmethod
    def github_data_repository(self) -> GithubDataRepository:
        raise NotImplementedError
