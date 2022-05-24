import sys

import pytest

from src.domain.entities.schedule import Schedule

sys.path.append('')


class TesteScheduleEntity:

    def test_should_create_schedule(self):
        schedule = Schedule('linus', 'linux', 'https://webhook.webhook/123456789')
        assert schedule.user == 'linus'

    def test_not_should_create_schedule_less_user(self):
        with pytest.raises(ValueError, match='Invalid user'):
            schedule = Schedule('', 'linux', 'https://webhook.webhook/123456789')

    def test_not_should_create_schedule_less_repository(self):
        with pytest.raises(ValueError, match='Invalid repository'):
            schedule = Schedule('linus', '', 'https://webhook.webhook/123456789')

    def test_not_should_create_schedule_less_url(self):
        with pytest.raises(ValueError, match='Invalid url'):
            schedule = Schedule('linus', 'linux', '')
