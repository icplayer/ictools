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


class AddonModule(Module):

    @property
    def moduleType(self):
        return 'Addon'
