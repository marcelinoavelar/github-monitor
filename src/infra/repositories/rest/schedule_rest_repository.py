from abc import ABC

from src.domanin.entities.schedule import Schedule
from src.domanin.repositories.schedule_repository import ScheduleRepository


class ScheduleJsonRepository(ScheduleRepository, ABC):
    filename = 'db.json'

    def find(self, schedule_id: str) -> Schedule:
        return Schedule('x', 'x', 'x', 'x')

    def save(self, schedule: Schedule):
        print('x')

    def all(self):
        return []