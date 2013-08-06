# -*- coding: utf-8 -*-
'''
Created on 05-08-2013

@author: Krzysztof Langner
'''

    
class Module:
    ''' Base class for page module. 
    '''
    
    def __init__(self, node):
        self._node = node