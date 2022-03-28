from fastapi import FastAPI

from src.application.use_cases.process_hook import ProcessHook
from src.application.use_cases.process_hook_dto import ProcessHookInput
from src.infra.factories.in_memory_repository_factory import InMemoryRepositoryFactory

app = FastAPI()


@app.get("/")
def root():
    return {'message': 'github-monitor'}


@app.post("/hook")
def hook_create(_input: ProcessHookInput):
    try:
        repository_factory = InMemoryRepositoryFactory()
        _input = ProcessHookInput(_input.user, _input.repository, _input.url_hook)
        process_hook = ProcessHook(repository_factory)
        output = process_hook.execute(_input)
        return output
    except ValueError as error:
        return {'message:': f'{error}'}
