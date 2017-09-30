import finder_utils

from presenter_file import PresenterFile


class PresenterFinder:

    GLOB_PATTERN = 'app/presenters/**/*.rb'

    def __init__(self, context):
        self.context = context
        self.root_path = context['__root_path']

    def find_files(self):
        files = finder_utils.glob_project(self.root_path, self.GLOB_PATTERN)
        return [PresenterFile(filename) for filename in files]
