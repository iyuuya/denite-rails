import finder_utils

from serializer_file import SerializerFile


class SerializerFinder:

    GLOB_PATTERN = 'app/serializers/**/*.rb'

    def __init__(self, context):
        self.context = context
        self.root_path = context['__root_path']

    def find_files(self):
        files = finder_utils.glob_project(self.root_path, self.GLOB_PATTERN)
        return [SerializerFile(filename) for filename in files]
