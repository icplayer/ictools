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
        logging.warn('%s - no converter' % self.module.moduleType)
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
      
      
class ButtonConverter(ModuleConverter):

    @property
    def bodyText(self):
        if self.module.properties['buttonType'] == 'checkAnswers':
            text = '''
            <div module="Check" class="ic_check {{class}}">
            <model>
                <property name="isVisible" value="true"/>
            </model>
            <button>Check</button>
        </div>
            '''
        else:
            text = '''
            <div module="Reset" class="ic_reset">
                <model>
                    <property name="isVisible" value="true"/>
                </model>
                <button>Reset</button>
            </div>
            '''
        return self._replacePropertyValues(text, self.module.properties)
      
      
class ChoiceConverter(ModuleConverter):

    @property
    def bodyText(self):
        text = '''
        <div module="Choice" class="ic_choice {{class}}">
            <model>
                <property name="id" value="{{id}}"/>
                <property name="isVisible" value="{{isVisible}}"/>
                <property name="isMulti" value="{{isMulti}}"/>
                <property name="options" type="list">
                    <items>
                    {{items}}
                    </items>
                </property>
            </model>
        </div>
        '''
        properties = self.module.properties
        items = ''
        for options in properties['options']:
            items += """<item>
                            <property name='score' value='%d'/>
                            <property name='text'>%s</property>
                        </item>\n""" % (options['value'], options['text'])
        properties['items'] = items
        del properties['options']
        return self._replacePropertyValues(text, properties)
      
      
class TextConverter(ModuleConverter):

    @property
    def bodyText(self):
        text = '''
        <div module="Text" class="{{class}}">
            <model>
                <property name="id" value="{{id}}"/>
                <property name="isVisible" value="{{isVisible}}"/>
                <property name="text">{{text}}</property>
            </model>
        </div>
        '''
        properties = self.module.properties
        return self._replacePropertyValues(text, properties)

