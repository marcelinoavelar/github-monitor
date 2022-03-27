from abc import ABC, abstractmethod

from src.domanin.entities.github_data import GithubData


class GithubDataRepository(ABC):

    @abstractmethod
    def find(self, user: str, repository: str) -> GithubData:
        raise NotImplementedError
