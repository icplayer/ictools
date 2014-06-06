# -*- coding: utf-8 -*-
'''
Created on 26-11-2013

@author: Krzysztof Langner
'''
from epub.converters import ModuleConverter
from model.content import Lesson
import os
import shutil


TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'templates/')


def createBookFolders(rootFolder, lessonFolder, lesson):
    if os.path.exists(rootFolder):
        raise Exception("Director %s already exists" % rootFolder)
    os.makedirs(rootFolder)
    createMimeTypeFile(rootFolder, 'application/epub+zip')
    createMetaInfFolder(rootFolder)
    contentFolder = createContentFolder(rootFolder)
    _copyRuntime(contentFolder)
    createCSSFiles(contentFolder, lesson)
    _copyMediaFiles(contentFolder, lessonFolder)
    createPackageDocument(contentFolder, lesson)
    createHtmlFiles(contentFolder, lesson)
    createTocFile(contentFolder, lesson)


def createMimeTypeFile(rootFolder, content):
    _writeTemplate(rootFolder + "/mimetype", 'mimetype', {})


def createMetaInfFolder(rootFolder):
    metaFolder = rootFolder + '/META-INF'
    os.mkdir(metaFolder)
    _writeTemplate(metaFolder + "/container.xml", 'container.xml', {})


def _copyRuntime(contentFolder):
    shutil.copytree(TEMPLATES_DIR + 'icruntime', contentFolder + '/script')


def _writeTemplate(destFilename, templateName, params):
    ''' Parse template parameters and write contents to given folder 
        with the same name as template
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
    os.mkdir(contentFolder + '/css')
    os.mkdir(contentFolder + '/media')
    os.mkdir(contentFolder + '/xhtml')
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
    destFile = contentFolder + '/css/lesson.css'
    _writeTemplate(destFile, 'lesson.css', {'content':lesson.style})


def _copyMediaFiles(contentFolder, lessonFolder):
    shutil.copytree(lessonFolder + '/resources', contentFolder + '/resources')


def createHtmlFiles(contentFolder, lesson):
    htmlFolder = contentFolder + '/xhtml'
    for i in range(len(lesson.pages)):
        pageId = "page%d" % (i+1)
        destFile = "%s/%s.html" % (htmlFolder, pageId)
        page = lesson.pages[i]
        pageContent = convertPage(page)
        _writeTemplate(destFile, 'page.html', pageContent)
        
        
def convertPage(page):
    content = ''
    for module in page.modules:
        converter = ModuleConverter.create(module)
        content += converter.bodyText
    return {'content': content}        


def createTocFile(contentFolder, lesson):
    destFile = contentFolder + '/xhtml/navigation.html'
    toc = ''
    for i in range(len(lesson.pages)):
        pageId = "page%d" % (i+1)
        page = lesson.pages[i]
        toc += "<li><a href='" + pageId + ".html'>" + page.name + "</a></li>\n"
    _writeTemplate(destFile, 'navigation.html', {'toc':toc})

    
def cleanBookFolders(rootFolder):
    if os.path.exists(rootFolder):
        shutil.rmtree(rootFolder)


def makeDistribution(buildFolder, zipFilePath):
    shutil.make_archive(zipFilePath, "zip", buildFolder)
    shutil.move(zipFilePath + ".zip", zipFilePath)


if __name__ == '__main__':
    buildFolder = os.path.join(os.path.dirname(__file__), '../../build/epub/lesson1')
    distFilePath = os.path.join(os.path.dirname(__file__), '../../dist/lesson1.epub')
    lessonFolder = os.path.join(os.path.dirname(__file__), '../../mauthor/lesson1')
    lesson = Lesson(lessonFolder + '/pages/main.xml')
    cleanBookFolders(buildFolder)
    createBookFolders(buildFolder, lessonFolder, lesson)
    makeDistribution(buildFolder, distFilePath)
    print("Book created")