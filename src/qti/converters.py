# -*- coding: utf-8 -*-
'''
Created on 2014-05-26

@author: Krzysztof Langner
'''



class ModuleConverter(object):
    ''' Base class for converters from icplayer to epub3 
    '''

    def __init__(self, module):
        self.module = module
    
    def bodyText(self, resPath):
        return ""

    @property    
    def correctResponses(self):
        """ List of correct responses"""
        return []

    @property    
    def resources(self):
        """ List of resource urls which should be included in the package"""
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

    def bodyText(self, resPath):
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

    def bodyText(self, resPath):
        text = '''
        <img class="{{class}}" src="{{src}}" width="{{width}}" height="{{height}}" />
        '''
        properties = self.module.properties
        properties["src"] = resPath + "/" + properties["src"].split("/")[-1] 
        return self._replacePropertyValues(text, properties)

    @property    
    def resources(self):
        properties = self.module.properties
        return [properties["src"]]
      
      
class TextConverter(ModuleConverter):

    def bodyText(self, resPath):
        text = '''
        <div>
            {{text}}
        </div>
        '''
        properties = self.module.properties
        return self._replacePropertyValues(text, properties)

