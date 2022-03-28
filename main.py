import argparse

from src.application.use_cases.process_hook import ProcessHook
from src.application.use_cases.process_hook_dto import ProcessHookInput
from src.application.use_cases.schedule_hook import ScheduleHook
from src.application.use_cases.schedule_hook_dto import ScheduleHookInput
from src.infra.factories.json_repository_factory import JsonRepositoryFactory
from src.infra.factories.rest_repository_factory import RestRepositoryFactory


def get_parser():
    parser = argparse.ArgumentParser()
    parser_group = parser.add_argument_group()
    parser_group.add_argument('-u', '--user', dest='user', type=str, required=True)
    parser_group.add_argument('-r', '--repo', dest='repository', type=str, required=True)
    parser_group.add_argument('-w', '--webhook', dest='url_hook', type=str, required=True)
    parser_group.add_argument('-s', '--schedule', dest='schedule', type=bool)
    return parser.parse_args()


def run_hook(args):
    repository_factory = RestRepositoryFactory()
    _input = ProcessHookInput(args.user, args.repository, args.url_hook)
    process = ProcessHook(repository_factory)
    output = process.execute(_input)
    print(output)


def schedule_hook(args):
    repository_factory = JsonRepositoryFactory()
    _input = ScheduleHookInput(args.user, args.repository, args.url_hook)
    schedule = ScheduleHook(repository_factory)
    output = schedule.execute(_input)
    print(output)


def main():
    args = get_parser()
    if args.schedule:
        schedule_hook(args)
    else:
        run_hook(args)


if __name__ == '__main__':
    main()
