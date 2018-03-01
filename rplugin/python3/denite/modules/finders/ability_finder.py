import finder_utils

from ability_file import AbilityFile


class AbilityFinder:

    GLOB_PATTERN = 'app/abilities/**/*.rb'

    def __init__(self, context):
        self.context = context
        self.root_path = context['__root_path']

    def find_files(self):
        files = finder_utils.glob_project(self.root_path, self.GLOB_PATTERN)
        return [AbilityFile(filename) for filename in files]
