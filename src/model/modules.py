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
        return {}

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
        data = {}
        data['id'] = self.node.attributes['id'].value
        data['isVisible'] = self.node.attributes['isVisible'].value
        textNode = self.node.getElementsByTagName('text')[0].childNodes[0]
        data['text'] = textNode.nodeValue
        return data


class ImageModule(Module):

    @property
    def moduleType(self):
        return 'Image'


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
        data = {}
        data['id'] = self.node.attributes['id'].value
        data['isVisible'] = self.node.attributes['isVisible'].value
        buttonNode = self.node.getElementsByTagName('button')[0]
        data['buttonType'] = buttonNode.attributes['type'].value
        return data


class AddonModule(Module):

    @property
    def moduleType(self):
        return 'Addon'
