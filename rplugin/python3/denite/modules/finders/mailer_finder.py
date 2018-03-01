import finder_utils

from mailer_file import MailerFile


class MailerFinder:

    GLOB_PATTERN = 'app/mailers/**/*.rb'

    def __init__(self, context):
        self.context = context
        self.root_path = context['__root_path']

    def find_files(self):
        files = finder_utils.glob_project(self.root_path, self.GLOB_PATTERN)
        return [MailerFile(filename) for filename in files]
