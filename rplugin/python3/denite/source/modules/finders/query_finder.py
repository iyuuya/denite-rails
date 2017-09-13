import finder_utils

from query_file import QueryFile


class QueryFinder:

    GLOB_PATTERN = 'app/queries/**/*.rb'

    def __init__(self, context):
        self.context = context
        self.root_path = context['__root_path']

    def find_files(self):
        files = finder_utils.glob_project(self.root_path, self.GLOB_PATTERN)
        return [QueryFile(filename) for filename in files]
