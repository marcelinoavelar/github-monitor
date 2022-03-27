import sys
import pytest

sys.path.append('')
from src.domanin.entities.issue import Issue


class TestIssueEntity:

    def test_should_create_issue(self):
        issue = Issue('The Issue', 'pythonist', ['bug', 'apocalypse'])
        assert issue.title == 'The Issue'
        assert len(issue.labels) == 2

    def test_not_should_create_issue_with_less_title(self):
        with pytest.raises(ValueError, match='Invalid title'):
            issue = Issue('', 'pythonist', ['bug', 'end-wold'])

    def test_not_should_create_issue_with_less_author(self):
        with pytest.raises(ValueError, match='Invalid author'):
            issue = Issue('The Issue', '', ['bug', 'end-wold'])

    def test_should_create_issue_with_less_labels(self):
        issue = Issue('The Issue', 'pythonist')
        assert len(issue.labels) == 0
