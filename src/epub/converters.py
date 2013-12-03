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
    def bodyText(self):
        logging.debug('No converter for module: %s' % self.module.moduleType)
        return ''

    @staticmethod
    def create(module):
        name = module.moduleType.lower() + 'converter'
        for cls in ModuleConverter.__subclasses__():
            if cls.__name__.lower() == name:
                return cls(module)
        return ModuleConverter(module)
    
    def _replacePropertyValues(self, template, properties):
        text = template
        for key,value in properties.iteritems():
            text = text.replace('{{' + key + '}}', value)
        return text
      
      
class TextConverter(ModuleConverter):

    @property
    def bodyText(self):
        text = '''
        <div module="Text">
            <model>
                <property name="id" value="{{id}}"/>
                <property name="isVisible" value="{{isVisible}}"/>
                <property name="text">{{text}}</property>
            </model>
        </div>
        '''
        properties = self.module.properties
        return self._replacePropertyValues(text, properties)

