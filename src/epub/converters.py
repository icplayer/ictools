# -*- coding: utf-8 -*-
'''
Created on 02-12-2013

@author: Krzysztof Langner
'''
import logging


class ModuleConverter(object):
    ''' Base class for converters from icplayer to epub3 
    '''

    def __init__(self, module):
        self.module = module
    
    @property    
    def html(self):
        logging.debug('No converter for module: %s' % self.module.moduleType)
        return ''

    @staticmethod
    def create(module):
        name = module.moduleType.lower() + 'converter'
        for cls in ModuleConverter.__subclasses__():
            if cls.__name__.lower() == name:
                return cls(module)
        return ModuleConverter(module)
      
      
class TextConverter(ModuleConverter):

    @property
    def html(self):
        return '<div>Text module</div>\n'

