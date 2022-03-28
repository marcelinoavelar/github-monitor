from fastapi import FastAPI

from src.application.use_cases.process_hook import ProcessHook
from src.application.use_cases.process_hook_dto import ProcessHookInput
from src.application.use_cases.schedule_hook import ScheduleHook
from src.application.use_cases.schedule_hook_dto import ScheduleHookInput
from src.infra.factories.rest_repository_factory import RestRepositoryFactory
from src.infra.factories.json_repository_factory import JsonRepositoryFactory

app = FastAPI()


@app.get('/')
def root():
    return {'message': 'github-monitor'}


@app.post('/hook')
def hook_create(_input: ProcessHookInput):
    try:
        repository_factory = RestRepositoryFactory()
        _input = ProcessHookInput(_input.user, _input.repository, _input.url_hook)
        process_hook = ProcessHook(repository_factory)
        output = process_hook.execute(_input)
        return output
    except ValueError as error:
        return {'message:': f'{error}'}


@app.post('/schedule')
def schedule_create(_input: ScheduleHookInput):
    try:
        repository_factory = JsonRepositoryFactory()
        schedule_hook = ScheduleHook(repository_factory)
        output = schedule_hook.execute(_input)
        return output
    except ValueError as error:
        return {'message:': f'{error}'}
