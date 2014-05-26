# -*- coding: utf-8 -*-
'''
Created on 26-11-2013

@author: Krzysztof Langner
'''
import os
import shutil

from model.content import Lesson
from qti.converters import ModuleConverter
from utils.template import writeToFile


TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'templates/')


def convert(lessonPath, dstFolder):
    lesson = Lesson(lessonPath)
    _prepareDstFolders(dstFolder)
    _createAssessment(lesson, dstFolder)
    for page in lesson.pages:
        _convertPage(page, dstFolder)


def _prepareDstFolders(dstFolder):
    ''' Prepare folders for building qti '''
    if os.path.exists(dstFolder):
        shutil.rmtree(dstFolder)
    os.mkdir(dstFolder)


def _createAssessment(lesson, dstFolder):
    params = { "title": lesson.name
             , "items": _createItemRefs(lesson)}
    writeToFile(TEMPLATES_DIR+"assessment.xml", dstFolder+"assessment.xml", params)
    
    
def _createItemRefs(lesson):
    items = ''
    for page in lesson.pages:
        pageId = page.name
        items += "<assessmentItemRef identifier='%s' href='%s.xml' fixed='false'/>\n" % (pageId, pageId)
    return items    


def _convertPage(page, dstFolder):
    pageId = page.name
    params = {"title": page.name, "id": page.id}
    params["correctResponses"] = _convertCorrectResponses(page)
    params["modules"] = _convertModules(page)
    writeToFile(TEMPLATES_DIR+"item.xml", dstFolder+pageId+".xml", params)
    
def _convertCorrectResponses(page):
    content = ""
    for module in page.modules:
        converter = ModuleConverter.create(module)
        for response in converter.correctResponses:
            content += "<value>" + response + "</value>\n"
    return content
    
def _convertModules(page):
    content = ""
    for module in page.modules:
        converter = ModuleConverter.create(module)
        content += converter.bodyText
    return content


if __name__ == '__main__':
    buildFolder = os.path.join(os.path.dirname(__file__), '../../build/qti/')
#     distFilePath = os.path.join(os.path.dirname(__file__), '../../dist/qti.zip')
    lessonPath = os.path.join(os.path.dirname(__file__), '../../sample/lesson1/pages/main.xml')
    convert(lessonPath, buildFolder)
#    _makeDistribution(buildFolder, distFilePath)
    print("QTI package created")