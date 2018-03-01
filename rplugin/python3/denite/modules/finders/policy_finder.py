import finder_utils

from policy_file import PolicyFile


class PolicyFinder:

    GLOB_PATTERN = 'app/policies/**/*.rb'

    def __init__(self, context):
        self.context = context
        self.root_path = context['__root_path']

    def find_files(self):
        files = finder_utils.glob_project(self.root_path, self.GLOB_PATTERN)
        return [PolicyFile(filename) for filename in files]
