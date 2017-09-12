import finder_utils

from asset_file import AssetFile


class AssetFinder:

    GLOB_PATTERN = 'app/assets/**/*.rb'

    def __init__(self, context):
        self.context = context
        self.root_path = context['__root_path']

    def find_files(self):
        files = finder_utils.glob_project(self.root_path, self.GLOB_PATTERN)
        return [AbilityFile(filename) for filename in files]
