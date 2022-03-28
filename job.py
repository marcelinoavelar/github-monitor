from src.application.use_cases.get_schedules import GetSchedules
from src.application.use_cases.process_hook import ProcessHook
from src.application.use_cases.process_hook_dto import ProcessHookInput
from src.infra.factories.json_repository_factory import JsonRepositoryFactory
from src.infra.factories.rest_repository_factory import RestRepositoryFactory


def get_schedules():
    try:
        repository_factory = JsonRepositoryFactory()
        get_schedules = GetSchedules(repository_factory)
        output = get_schedules.execute()
        return output
    except ValueError as error:
        print(f'{error}')


def run_hook(user: str, repository: str, url_hook: str):
    try:
        repository_factory = RestRepositoryFactory()
        _input = ProcessHookInput(user, repository, url_hook)
        process = ProcessHook(repository_factory)
        output = process.execute(_input)
        print(f'\n {output} \n')
    except ValueError as error:
        print(f'{error}')


def main():
    schedules = get_schedules().schedules
    for schedule in schedules:
        print(f'\n {schedule.schedule_id}')
        run_hook(schedule.user, schedule.repository, schedule.url)


if __name__ == '__main__':
    main()
