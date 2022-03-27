from dataclasses import dataclass, field
import sys

import pytest

sys.path.append('')
from src.domanin.entities.github_data import GithubData
from src.domanin.entities.contributor import Contributor
from src.domanin.entities.issue import Issue


class TestGithubDataEntity:

    def test_should_create_github_data(self):
        contributor = Contributor('pythonista', 'Python Dev', 10)
        issue = Issue('The Issue', 'pythonist', ['bug', 'apocalypse'])
        github_data = GithubData('pythonist', 'python-lang', [issue], [contributor])
        assert github_data.user == 'pythonist'
        assert github_data.repository == 'python-lang'
        assert len(github_data.contributors) == 1
        assert len(github_data.issues) == 1

    def test_not_should_create_github_data_with_less_user(self):
        with pytest.raises(ValueError, match='Invalid user'):
            github_data = GithubData('', 'python-lang')

    def test_not_should_create_github_data_with_less_repository(self):
        with pytest.raises(ValueError, match='Invalid repository'):
            github_data = GithubData('pythonist', '')

    def test_should_create_github_data_with_less_contributor(self):
        github_data = GithubData('pythonist', 'python-lang')
        assert len(github_data.contributors) == 0

    def test_should_create_github_data_with_less_issue(self):
        github_data = GithubData('pythonist', 'python-lang')
        assert len(github_data.issues) == 0

    def test_should_generate_json(self):
        expected_json = GithubDataJsonFixture().value
        contributors = [
            Contributor('contributor-1', 'Python Dev - 1', 10),
            Contributor('contributor-2', 'Python Dev - 2', 5),
        ]
        issues = [
            Issue('The Issue-1', 'pythonist', ['feature']),
            Issue('The Issue-2', 'pythonist', ['bug', 'apocalypse']),
            Issue('The Issue-2', 'pythonist', ['doc', 'test']),
        ]
        github_data = GithubData('pythonist', 'python-lang', issues, contributors)
        assert github_data.to_json() == expected_json


@dataclass
class GithubDataJsonFixture:
    value: dict = field(default_factory=dict)

    def __post_init__(self):
        self.value = {
            'user': 'pythonist',
            'repository': 'python-lang',
            'issues': [
                {
                    'title': 'The Issue-1',
                    'author': 'pythonist',
                    'labels': [
                        'feature'
                    ]
                },
                {
                    'title': 'The Issue-2',
                    'author': 'pythonist',
                    'labels': [
                        'bug',
                        'apocalypse'
                    ]
                },
                {
                    'title': 'The Issue-2',
                    'author': 'pythonist',
                    'labels': [
                        'doc',
                        'test'
                    ]
                }
            ],
            'contributors': [
                {
                    'username': 'contributor-1',
                    'name': 'Python Dev - 1',
                    'qtd_commits': 10
                },
                {
                    'username': 'contributor-2',
                    'name': 'Python Dev - 2',
                    'qtd_commits': 5
                }
            ]
        }
