import finder_utils

from service_file import ServiceFile


class ServiceFinder:

    GLOB_PATTERN = 'app/services/**/*.rb'

    def __init__(self, context):
        self.context = context
        self.root_path = context['__root_path']

    def find_files(self):
        files = finder_utils.glob_project(self.root_path, self.GLOB_PATTERN)
        return [ServiceFile(filename) for filename in files]
