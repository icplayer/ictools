# -*- coding: utf-8 -*-
'''
Created on 26-11-2013

@author: Krzysztof Langner
'''
from model.content import Lesson
import os
import shutil


TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'templates/')


def createBookFolders(rootFolder, lesson):
    if os.path.exists(rootFolder):
        raise Exception("Director %s already exists" % rootFolder)
    os.mkdir(rootFolder)
    createMimeTypeFile(rootFolder, 'application/epub+zip')
    createMetaInfFolder(rootFolder)
    createContentFolder(rootFolder)
    createPackageDocument(rootFolder, lesson)


def createMimeTypeFile(rootFolder, content):
    _writeTemplate(rootFolder, 'mimetype', {})


def createMetaInfFolder(rootFolder):
    metaFolder = rootFolder + '/META-INF'
    os.mkdir(metaFolder)
    _writeTemplate(metaFolder, 'container.xml', {})


def _writeTemplate(destFolder, templateName, params):
    ''' Parse template parameters and write contents to given folder 
        with the same name like template
    '''
    templateFile = open(TEMPLATES_DIR + templateName, 'r')
    content = templateFile.read()
    templateFile.close()
    for key,value in params.iteritems():
        content = content.replace('{{' + key + '}}', value)
    outFile = open(destFolder + "/" + templateName, 'w')
    outFile.write(content)
    outFile.close()


def createContentFolder(rootFolder):
    contentFolder = rootFolder + '/content'
    os.mkdir(contentFolder)
    
    
def createPackageDocument(rootFolder, lesson):
    contentFolder = rootFolder + '/content'
    _writeTemplate(contentFolder, 'book.opf', {'title':lesson.name, 
                                               'items':'', 
                                               'itemrefs': '',
                                               'modified_date': ''})    


def cleanBookFolders(rootFolder):
    if os.path.exists(rootFolder):
        shutil.rmtree(rootFolder)


if __name__ == '__main__':
    buildFolder = os.path.join(os.path.dirname(__file__), '../../build/test')
    sampleFolder = os.path.join(os.path.dirname(__file__), '../../sample/lesson1')
    lesson = Lesson(sampleFolder + '/lesson1.ic.xml')
    cleanBookFolders(buildFolder)
    createBookFolders(buildFolder, lesson)
    print("Book created")