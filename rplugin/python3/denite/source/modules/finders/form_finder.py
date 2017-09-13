import finder_utils

from form_file import FormFile


class FormFinder:

    GLOB_PATTERN = 'app/forms/**/*.rb'

    def __init__(self, context):
        self.context = context
        self.root_path = context['__root_path']

    def find_files(self):
        files = finder_utils.glob_project(self.root_path, self.GLOB_PATTERN)
        return [FormFile(filename) for filename in files]
