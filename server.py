from fastapi import FastAPI

from src.application.use_cases.get_schedules import GetSchedules
from src.application.use_cases.process_hook import ProcessHook
from src.application.use_cases.process_hook_dto import ProcessHookInput
from src.application.use_cases.schedule_hook import ScheduleHook
from src.application.use_cases.schedule_hook_dto import ScheduleHookInput
from src.infra.factories.json_repository_factory import JsonRepositoryFactory
from src.infra.factories.rest_repository_factory import RestRepositoryFactory

app = FastAPI()


@app.get('/')
def root():
    return {'message': 'github-monitor'}


@app.post('/hooks')
def hooks_create(_input: ProcessHookInput):
    try:
        repository_factory = RestRepositoryFactory()
        _input = ProcessHookInput(_input.user, _input.repository, _input.url_hook)
        process_hook = ProcessHook(repository_factory)
        output = process_hook.execute(_input)
        return output
    except ValueError as error:
        return {'message:': f'{error}'}


@app.get('/schedules')
def schedules_index():
    try:
        repository_factory = JsonRepositoryFactory()
        get_schedules = GetSchedules(repository_factory)
        output = get_schedules.execute()
        return output
    except ValueError as error:
        return {'message:': f'{error}'}


@app.post('/schedules')
def schedules_create(_input: ScheduleHookInput):
    try:
        repository_factory = JsonRepositoryFactory()
        schedule_hook = ScheduleHook(repository_factory)
        output = schedule_hook.execute(_input)
        return output
    except ValueError as error:
        return {'message:': f'{error}'}
