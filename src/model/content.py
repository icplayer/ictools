'''
Created on 05-08-2013

@author: klangner
'''
from model.modules import Module
from xml.dom import minidom
from xml.dom.minidom import Node
import os.path


class Lesson:
    ''' Lesson model is kept in XML DOM. 
        It can be safely saved back to the file 
    '''
    
    def __init__(self, filename):
        self._filename = filename
        self._xmldoc = minidom.parse(self._filename)
        self._root_node = self._xmldoc.getElementsByTagName('interactiveContent')[0]
        self._loadPages()
        
    def _loadPages(self):
        self._pages = []
        base_path = os.path.dirname(self._filename) + "/" 
        for page_node in  self._xmldoc.getElementsByTagName('page'):
            url = base_path + page_node.attributes['href'].value
            page = Page(url, page_node.attributes['name'].value)
            self._pages.append(page)
            
    @property
    def pages(self):
        return self._pages
    
    @property
    def name(self):
        return self._root_node.attributes['name'].value
    
    @property
    def style(self):
        styleNode = self._xmldoc.getElementsByTagName('style')[0].childNodes[0]
        return styleNode.nodeValue


class Page:
    ''' Page model is kept in XML DOM. 
        It can be safely saved back to the file 
    '''
    
    def __init__(self, filename, name=''):
        self.name = name
        self._filename = filename
        self._xmldoc = minidom.parse(self._filename)
        self._root_node = self._xmldoc.getElementsByTagName('page')[0]
        self._loadModules()
        
    def _loadModules(self):
        self._modules = []
        module_nodes = self._xmldoc.getElementsByTagName('modules')[0]
        for module_node in  module_nodes.childNodes:
            if module_node.nodeType == Node.ELEMENT_NODE:
                module = Module.create(module_node)
                self._modules.append(module)
            
    @property
    def modules(self):
        return self._modules
    
