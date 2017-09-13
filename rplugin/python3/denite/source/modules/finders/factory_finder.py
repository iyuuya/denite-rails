import finder_utils

from factory_file import FactoryFile


class FactoryFinder:

    GLOB_PATTERN = 'spec/factories/**/*.rb'

    def __init__(self, context):
        self.context = context
        self.root_path = context['__root_path']

    def find_files(self):
        files = finder_utils.glob_project(self.root_path, self.GLOB_PATTERN)
        return [FactoryFile(filename) for filename in files]
