from src.domanin.factories.repository_factory import RepositoryFactory
from src.infra.repositories.in_memory.github_data_in_memory_repository import GithubDataInMemoryRepository


class InMemoryRepositoryFactory(RepositoryFactory):

    @property
    def github_data_repository(self):
        return GithubDataInMemoryRepository()
