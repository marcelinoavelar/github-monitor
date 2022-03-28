from abc import ABC

from src.domanin.entities.github_data import GithubData
from src.domanin.repositories.github_data_repository import GithubDataRepository


class GithubDataJsonRepository(GithubDataRepository, ABC):

    def find(self, user: str, repository: str) -> GithubData:
        return GithubData('not-implemented', 'not-implemented')
