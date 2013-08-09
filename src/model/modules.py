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
        
    def getType(self):
        return ''

    @staticmethod
    def create(node):
        name = node.tagName.lower()
        for cls in Module.__subclasses__():
            if cls.__name__.lower() == name:
                return cls(node)
        return Module(node)
      
      
class TextModule(Module):

    def getType(self):
        return 'Text'


class ImageModule(Module):

    def getType(self):
        return 'Image'


class ShapeModule(Module):

    def getType(self):
        return 'Shape'


class ButtonModule(Module):

    def getType(self):
        return 'Button'


class AddonModule(Module):

    def getType(self):
        return 'Addon'
