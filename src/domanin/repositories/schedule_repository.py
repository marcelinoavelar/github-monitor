from abc import ABC, abstractmethod

from src.domanin.entities.schedule import Schedule


class ScheduleRepository(ABC):

    @abstractmethod
    def find(self, schedule_id: str) -> Schedule:
        raise NotImplementedError

    @abstractmethod
    def save(self, schedule: Schedule):
        raise NotImplementedError

    @abstractmethod
    def all(self) -> list[Schedule]:
        raise NotImplementedError
