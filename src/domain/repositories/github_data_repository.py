from abc import ABC, abstractmethod

from src.domain.entities.github_data import GithubData


class GithubDataRepository(ABC):

    @abstractmethod
    def find(self, user: str, repository: str) -> GithubData:
        raise NotImplementedError
