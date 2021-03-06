from abc import ABC

from src.domain.entities.schedule import Schedule
from src.domain.repositories.schedule_repository import ScheduleRepository


class ScheduleInMemoryRepository(ScheduleRepository, ABC):
    schedules = [
        Schedule('a', 'b', 'c', 'abc'),
        Schedule('w', 'y', 'k', 'xyk')
    ]

    def find(self, schedule_id: str) -> Schedule:
        for schedule in self.schedules:
            if schedule.schedule_id == schedule_id:
                return schedule
            else:
                raise ValueError('Not found schedule')

    def save(self, schedule: Schedule):
        self.schedules.append(schedule)

    def all(self):
        return self.schedules