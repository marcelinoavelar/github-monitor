import json
from abc import ABC
from os import path

from src.domanin.entities.schedule import Schedule
from src.domanin.repositories.schedule_repository import ScheduleRepository


class ScheduleJsonRepository(ScheduleRepository, ABC):
    filename = 'db.json'

    def find(self, schedule_id: str) -> Schedule:
        if path.isfile(self.filename) is False:
            raise Exception("File not found")
        with open(self.filename) as data:
            schedules = json.load(data)
        for schedule in schedules:
            if schedule['schedule_id'] == schedule_id:
                user = schedule['user']
                repository = schedule['repository']
                url = schedule['url']
                schedule_id = schedule['schedule_id']
                return Schedule(user, repository, url, schedule_id)
        raise ValueError('Nof found schedule')

    def save(self, schedule: Schedule):
        if path.isfile(self.filename) is False:
            file = open("db.json", "w")
            file.write("[]")
            file.close()
        with open(self.filename) as data:
            schedules = json.load(data)

        schedules.append({
            'user': schedule.user,
            'repository': schedule.repository,
            'url': schedule.url,
            'schedule_id': schedule.schedule_id
        })
        with open(self.filename, 'w') as json_file:
            json.dump(schedules, json_file,
                      indent=4,
                      separators=(',', ': '))

    def all(self):
        if path.isfile(self.filename) is False:
            raise Exception("File not found")
        with open(self.filename) as data:
            schedules_in_file = json.load(data)
        schedules_return = []
        for schedule in schedules_in_file:
            user = schedule['user']
            repository = schedule['repository']
            url = schedule['url']
            schedule_id = schedule['schedule_id']
            schedules_return.append(Schedule(user, repository, url, schedule_id))
        return schedules_return
