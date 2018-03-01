import finder_utils

from domain_file import DomainFile


class DomainFinder:

    GLOB_PATTERN = 'app/domains/**/*.rb'

    def __init__(self, context):
        self.context = context
        self.root_path = context['__root_path']

    def find_files(self):
        files = finder_utils.glob_project(self.root_path, self.GLOB_PATTERN)
        return [DomainFile(filename) for filename in files]
