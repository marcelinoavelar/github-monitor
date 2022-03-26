import sys
import pytest

sys.path.append("")
from src.domanin.entities.contributor import Contributor


class TestContributorEntity:

    def test_should_create_contributor(self):
        contributor = Contributor("pythonista", "Python Dev", 10)
        assert contributor.username == "pythonista"

    def test_not_should_create_contributor_with_less_username(self):
        with pytest.raises(ValueError, match="Invalid username"):
            contributor = Contributor("", "Python Dev", 10)

    def test_not_should_create_contributor_with_less_name(self):
        with pytest.raises(ValueError, match="Invalid name"):
            contributor = Contributor("pythonista", "", 10)

    def test_should_create_contributor_with_less_qtd_commits(self):
        contributor = Contributor("pythonista", "Python Dev")
        assert contributor.qtd_commits == 0
