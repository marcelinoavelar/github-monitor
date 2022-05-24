from abc import ABC

from src.domain.entities.contributor import Contributor
from src.domain.entities.github_data import GithubData
from src.domain.entities.issue import Issue
from src.domain.repositories.github_data_repository import GithubDataRepository


class GithubDataInMemoryRepository(GithubDataRepository, ABC):

    def find(self, user: str, repository: str) -> GithubData:
        contributors_1 = [
            Contributor('guido', 'Guido van Russen', 10),
        ]
        issues_1 = [
            Issue('The Issue-1', 'guido', ['feature']),
            Issue('The Issue-2', 'guido', ['bug', 'apocalypse']),
            Issue('The Issue-2', 'guido', ['doc', 'test']),
        ]
        github_data_1 = GithubData('guido', 'python', issues_1, contributors_1)

        contributors_2 = [
            Contributor('linus', 'Linus Torvald', 10),
            Contributor('dennis_ritchie', 'Dennis Ritchie', 5),
        ]
        issues_2 = [
            Issue('The Issue-1', 'linus', ['feature']),
            Issue('The Issue-2', 'linus', ['bug', 'apocalypse']),
            Issue('The Issue-2', 'dennis_ritchie', ['doc', 'test']),
        ]
        github_data_2 = GithubData('linus', 'linux', issues_2, contributors_2)


        repos = {
            'guidopython': github_data_1,
            'linuslinux': github_data_2,
        }
        return repos.get(f'{user}{repository}')
