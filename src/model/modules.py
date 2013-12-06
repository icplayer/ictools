# -*- coding: utf-8 -*-
'''
Created on 05-08-2013

@author: Krzysztof Langner
'''

    
class Module(object):
    ''' Base class for page module. 
    '''
    
    def __init__(self, node):
        self.node = node
        
    @property
    def moduleType(self):
        return ''
        
    @property
    def properties(self):
        data = {}
        data['id'] = self.node.attributes['id'].value
        data['isVisible'] = self.node.attributes['isVisible'].value
        data['width'] = self.node.attributes['width'].value
        data['height'] = self.node.attributes['height'].value
        data['class'] = self._getAttribute('class', '')
        return data
    
    def _getAttribute(self, name, defaultValue):
        if self.node.hasAttribute(name):
            return self.node.attributes[name].value
        return defaultValue

    @staticmethod
    def create(node):
        name = node.tagName.lower()
        for cls in Module.__subclasses__():
            if cls.__name__.lower() == name:
                return cls(node)
        return Module(node)
      
      
class TextModule(Module):

    @property
    def moduleType(self):
        return 'Text'
        
    @property
    def properties(self):
        data = Module.properties.fget(self)
        textNode = self.node.getElementsByTagName('text')[0].childNodes[0]
        data['text'] = textNode.nodeValue
        return data


class ChoiceModule(Module):

    @property
    def moduleType(self):
        return 'Choice'
        
    @property
    def properties(self):
        data = Module.properties.fget(self)
        choiceNode = self.node.getElementsByTagName('choice')[0]
        data['isMulti'] = choiceNode.attributes['isMulti'].value
        optionNodes = self.node.getElementsByTagName('option')
        options = []
        for node in optionNodes:
            options.append({'value':int(node.attributes['value'].value), 
                            'text':node.getElementsByTagName('text')[0].childNodes[0].nodeValue})
        data['options'] = options
        return data


class ImageModule(Module):

    @property
    def moduleType(self):
        return 'Image'
        
    @property
    def properties(self):
        data = Module.properties.fget(self)
        choiceNode = self.node.getElementsByTagName('image')[0]
        data['src'] = choiceNode.attributes['src'].value
        return data


class ShapeModule(Module):

    @property
    def moduleType(self):
        return 'Shape'


class ButtonModule(Module):

    @property
    def moduleType(self):
        return 'Button'
        
    @property
    def properties(self):
        data = Module.properties.fget(self)
        buttonNode = self.node.getElementsByTagName('button')[0]
        data['buttonType'] = buttonNode.attributes['type'].value
        return data


class AddonModule(Module):

    @property
    def moduleType(self):
        return 'Addon'
