from abc import ABC

from src.domanin.factories.repository_factory import RepositoryFactory
from src.infra.repositories.rest.github_data_rest_repository import GithubDataRestRepository


class RestRepositoryFactory(RepositoryFactory, ABC):

    @property
    def github_data_repository(self):
        return GithubDataRestRepository()
