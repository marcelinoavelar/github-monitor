import argparse
import sys

from src.application.use_cases.process_hook import ProcessHook
from src.application.use_cases.process_hook_dto import ProcessHookInput
from src.infra.factories.rest_repository_factory import RestRepositoryFactory


# from src.infra.factories.in_memory_repository_factory import InMemoryRepositoryFactory


def main():
    parser = argparse.ArgumentParser()
    parser_group = parser.add_argument_group()
    parser_group.add_argument('-u', '--user', dest='user')
    parser_group.add_argument('-r', '--repo', dest='repository')
    parser_group.add_argument('-w', '--webhook', dest='url_hook')
    args = parser.parse_args()
    if not args.user:
        print('Informe o nome do dono do repositório desejado')
        sys.exit()
    if not args.repository:
        print('Informe o nome do repositorio desjado')
        sys.exit()
    if not args.url_hook:
        print('Informe URL do webhook')
        sys.exit()
    repository_factory = RestRepositoryFactory()
    _input = ProcessHookInput(args.user, args.repository, args.url_hook)
    process_hook = ProcessHook(repository_factory)
    output = process_hook.execute(_input)
    print(output)


if __name__ == '__main__':
    main()
