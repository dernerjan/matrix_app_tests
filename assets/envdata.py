import abc

from general_objects.argv_parser_object import ArgvParserObject


class EnvData(abc.ABC):
    print_logs = False

class DevData(EnvData):
    github_url = None
    jira_url = None