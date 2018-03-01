import finder_utils

from attribute_file import AttributeFile


class AttributeFinder:

    GLOB_PATTERN = 'app/attributes/**/*.rb'

    def __init__(self, context):
        self.context = context
        self.root_path = context['__root_path']

    def find_files(self):
        files = finder_utils.glob_project(self.root_path, self.GLOB_PATTERN)
        return [AttributeFile(filename) for filename in files]
