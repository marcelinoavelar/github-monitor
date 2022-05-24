from abc import ABC

from src.domain.entities.github_data import GithubData
from src.domain.repositories.github_data_repository import GithubDataRepository


class GithubDataJsonRepository(GithubDataRepository, ABC):

    def find(self, user: str, repository: str) -> GithubData:
        return GithubData('not-implemented', 'not-implemented')
