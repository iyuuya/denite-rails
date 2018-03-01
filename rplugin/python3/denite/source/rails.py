# -*- coding: utf-8 -*-

from denite import util
from .base import Base

import os
import site

# Add external modules
path_to_this_dir = os.path.abspath(os.path.dirname(__file__))
path_to_modules = os.path.join(path_to_this_dir, '../modules')
site.addsitedir(path_to_modules)
site.addsitedir(os.path.join(path_to_modules, 'inflection'))
site.addsitedir(os.path.join(path_to_modules, 'finders'))
site.addsitedir(os.path.join(path_to_modules, 'models'))

from dwim_finder import DwimFinder # noqa
from model_finder import ModelFinder # noqa
from controller_finder import ControllerFinder # noqa
from helper_finder import HelperFinder # noqa
from view_finder import ViewFinder # noqa
from test_finder import TestFinder # noqa
from spec_finder import SpecFinder # noqa
from ability_finder import AbilityFinder # noqa
from validator_finder import ValidatorFinder # noqa
from decorator_finder import DecoratorFinder # noqa
from mailer_finder import MailerFinder # noqa
from asset_finder import AssetFinder # noqa
from service_finder import ServiceFinder # noqa
from form_finder import FormFinder # noqa
from serializer_finder import SerializerFinder # noqa
from config_finder import ConfigFinder # noqa
from attribute_finder import AttributeFinder # noqa
from policy_finder import PolicyFinder
from loyalty_finder import LoyaltyFinder
from domain_finder import DomainFinder
from query_finder import QueryFinder
from factory_finder import FactoryFinder
from job_finder import JobFinder
from uploader_finder import UploaderFinder
from db_finder import DbFinder
from presenter_finder import PresenterFinder


class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'rails'
        self.kind = 'file'

    def on_init(self, context):
        try:
            context['__target'] = context['args'][0]
        except IndexError:
            raise NameError('target must be provided')

        cbname = self.vim.current.buffer.name
        context['__cbname'] = cbname
        context['__root_path'] = util.path2project(self.vim, cbname, context.get('root_markers', ''))

    def highlight(self):
        # TODO syntax does not work as expected
        self.vim.command('syntax region deniteSource_railsConstant start=+^+ end=+^.\{-}\s+')
        self.vim.command('highlight link deniteSource_railsConstant Statement')
        self.vim.command('syntax match deniteSource_railsSeparator /::/ containedin=deniteSource_railsConstant')
        self.vim.command('highlight link deniteSource_railsSeparator Identifier')
        self.vim.command('syntax region deniteSource_railsPath start=+(+ end=+)+')
        self.vim.command('highlight link deniteSource_railsPath Statement')
        self.vim.command('syntax match deniteSource_railsController /Controller:/')
        self.vim.command('highlight link deniteSource_railsController Function')
        self.vim.command('syntax match deniteSource_railsModel /Model:/')
        self.vim.command('highlight link deniteSource_railsModel String')
        self.vim.command('syntax match deniteSource_railsHelper /Helper:/')
        self.vim.command('highlight link deniteSource_railsHelper Type')
        self.vim.command('syntax match deniteSource_railsView /View:/')
        self.vim.command('highlight link deniteSource_railsView Statement')
        self.vim.command('syntax match deniteSource_railsTest /Test:/')
        self.vim.command('highlight link deniteSource_railsTest Number')
        self.vim.command('syntax match deniteSource_railsSpec /Spec:/')
        self.vim.command('highlight link deniteSource_railsSpec Number')

    def gather_candidates(self, context):
        file_list = self._find_files(context)
        if file_list is not None:
            return [self._convert(context, x) for x in file_list]
        else:
            return []

    def _find_files(self, context):
        target = context['__target']

        if target == 'dwim':
            finder_class = DwimFinder
        elif target == 'model':
            finder_class = ModelFinder
        elif target == 'controller':
            finder_class = ControllerFinder
        elif target == 'helper':
            finder_class = HelperFinder
        elif target == 'view':
            finder_class = ViewFinder
        elif target == 'test':
            finder_class = TestFinder
        elif target == 'spec':
            finder_class = SpecFinder
        elif target == 'ability':
            finder_class = AbilityFinder
        elif target == 'validator':
            finder_class = ValidatorFinder
        elif target == 'decorator':
            finder_class = DecoratorFinder
        elif target == 'mailer':
            finder_class = MailerFinder
        elif target == 'asset':
            finder_class = AssetFinder
        elif target == 'service':
            finder_class = ServiceFinder
        elif target == 'form':
            finder_class = FormFinder
        elif target == 'serializer':
            finder_class = SerializerFinder
        elif target == 'config':
            finder_class = ConfigFinder
        elif target == 'attribute':
            finder_class = AttributeFinder
        elif target == 'policy':
            finder_class = PolicyFinder
        elif target == 'loyalty':
            finder_class = LoyaltyFinder
        elif target == 'domain':
            finder_class = DomainFinder
        elif target == 'query':
            finder_class = QueryFinder
        elif target == 'factory':
            finder_class = FactoryFinder
        elif target == 'job':
            finder_class = JobFinder
        elif target == 'uploader':
            finder_class = UploaderFinder
        elif target == 'db':
            finder_class = DbFinder
        elif target == 'presenter':
            finder_class = PresenterFinder
        else:
            msg = '{0} is not valid denite-rails target'.format(target)
            raise NameError(msg)

        return finder_class(context).find_files()

    def _convert(self, context, file_object):
        result_dict = {
            'word': file_object.to_word(context['__root_path']),
            'action__path': file_object.filepath
        }

        return result_dict
