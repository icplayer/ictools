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
    contentFolder = createContentFolder(rootFolder)
    createPackageDocument(contentFolder, lesson)
    copyRuntime(contentFolder)
    createCSSFiles(contentFolder, lesson)
    createMediaFiles(contentFolder, lesson)
    createHtmlFiles(contentFolder, lesson)


def createMimeTypeFile(rootFolder, content):
    _writeTemplate(rootFolder + "/mimetype", 'mimetype', {})


def createMetaInfFolder(rootFolder):
    metaFolder = rootFolder + '/META-INF'
    os.mkdir(metaFolder)
    _writeTemplate(metaFolder + "/container.xml", 'container.xml', {})


def copyRuntime(contentFolder):
    runtimeFolder = contentFolder + '/runtime'
    os.mkdir(runtimeFolder)


def _writeTemplate(destFilename, templateName, params):
    ''' Parse template parameters and write contents to given folder 
        with the same name like template
    '''
    templateFile = open(TEMPLATES_DIR + templateName, 'r')
    content = templateFile.read()
    templateFile.close()
    for key,value in params.iteritems():
        content = content.replace('{{' + key + '}}', value)
    outFile = open(destFilename, 'w')
    outFile.write(content)
    outFile.close()


def createContentFolder(rootFolder):
    contentFolder = rootFolder + '/content'
    os.mkdir(contentFolder)
    return contentFolder
    
    
def createPackageDocument(contentFolder, lesson):
    items = _createManifestItems(lesson)
    spine = _createSpineItems(lesson)
    _writeTemplate(contentFolder + "/book.opf", 
                   'book.opf', 
                   {'title':lesson.name, 'items':items, 'itemrefs': spine, 'modified_date': ''})    


def _createManifestItems(lesson):
    items = ''
    for i in range(len(lesson.pages)):
        pageId = "page%d" % (i+1)
        items += "<item id='%s' href='xhtml/%s.html' media-type='application/xhtml+xml'/>\n" % (pageId, pageId)
    return items


def _createSpineItems(lesson):
    items = ''
    for i in range(len(lesson.pages)):
        pageId = "page%d" % (i+1)
        items += "<itemref idref='%s'/>\n" % pageId
    return items


def createCSSFiles(contentFolder, lesson):
    cssFolder = contentFolder + '/css'
    os.mkdir(cssFolder)


def createMediaFiles(contentFolder, lesson):
    mediaFolder = contentFolder + '/media'
    os.mkdir(mediaFolder)


def createHtmlFiles(contentFolder, lesson):
    htmlFolder = contentFolder + '/xhtml'
    os.mkdir(htmlFolder)
    for i in range(len(lesson.pages)):
        pageId = "page%d" % (i+1)
        destFile = "%s/%s.html" % (htmlFolder, pageId)
        _writeTemplate(destFile, 'page.html', {})

    
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