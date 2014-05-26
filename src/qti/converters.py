# -*- coding: utf-8 -*-
'''
Created on 02-12-2013

@author: Krzysztof Langner
'''


class ModuleConverter(object):
    ''' Base class for converters from icplayer to epub3 
    '''

    def __init__(self, module):
        self.module = module
    
    @property    
    def bodyText(self):
        return ""

    @property    
    def correctResponses(self):
        """ List of correct responses"""
        return []

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
      
      
class ChoiceConverter(ModuleConverter):

    @property    
    def correctResponses(self):
        correct = []
        for options in self.module.properties['options']:
            if options['value'] > 0:
                correct.append(options['id'])
        return correct

    @property
    def bodyText(self):
        text = '''
        <choiceInteraction responseIdentifier="RESPONSE" shuffle="false" maxChoices="{{maxChoice}}">
            {{items}}
        </choiceInteraction>
        '''
        properties = self.module.properties
        items = ''
        for options in properties['options']:
            items += "<simpleChoice identifier='%s'>%s</simpleChoice>\n" % (options['id'], options['text'])
        properties['items'] = items
        if properties["isMulti"].lower() == "true":
            properties['maxChoice'] = str(len(properties['options']))
        else:
            properties['maxChoice'] = "1" 
        del properties['options']
        return self._replacePropertyValues(text, properties)
      
      
class ImageConverter(ModuleConverter):

    @property
    def bodyText(self):
        text = '''
        <img class="{{class}}" src="{{src}}" width="{{width}}" height="{{height}}" />
        '''
        properties = self.module.properties
        return self._replacePropertyValues(text, properties)
      
      
class TextConverter(ModuleConverter):

    @property
    def bodyText(self):
        text = '''
        <div>
            {{text}}
        </div>
        '''
        properties = self.module.properties
        return self._replacePropertyValues(text, properties)

