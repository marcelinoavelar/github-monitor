import requests

from src.domain.entities.contributor import Contributor
from src.domain.entities.github_data import GithubData
from src.domain.entities.issue import Issue
from src.domain.repositories.github_data_repository import GithubDataRepository


class GithubDataRestRepository(GithubDataRepository):
    github_base_url = 'https://api.github.com/repos/'

    def find(self, user: str, repository: str) -> GithubData:
        base_url = f'{self.github_base_url}{user}/{repository}/'
        issues = get_issues(base_url)
        contributors = get_contributors(base_url)
        github_data = get_github_data(base_url)
        github_data.issues = issues
        github_data.contributors = contributors
        return github_data


def get_github_data(url: str):
    response_data = requests.get(f'{url[:-1]}')
    user = response_data.json()['owner']['login']
    name = response_data.json()['name']
    github_data = GithubData(user, name)
    return github_data


def get_issues(url: str):
    response_data = requests.get(f'{url}issues')
    json_data = response_data.json()
    issues = []
    for issue in json_data:
        title = issue['title']
        author = issue['user']['login']
        labels = []
        for label in issue['labels']:
            labels.append(label['description'])
        issues.append(Issue(title, author, labels))
    return issues


def get_contributors(url: str):
    response_data = requests.get(f'{url}contributors')
    json_data = response_data.json()
    contributors = []
    for contributor in json_data:
        login = contributor['login']
        qtd_commits = contributor['contributions']
        contributors.append(Contributor(login, get_name_of_contributor(login), qtd_commits))
    return contributors


def get_name_of_contributor(login: str):
    response_data = requests.get(f'https://api.github.com/users/{login}')
    json_data = response_data.json()
    try:
        return json_data['name']
    except ValueError(f'#{login}') as error:
        return error
