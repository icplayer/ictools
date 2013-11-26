# -*- coding: utf-8 -*-
'''
Created on 26-11-2013

@author: Krzysztof Langner
'''
import shutil
import os


TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'templates/')


def createBookFolders(rootFolder):
    if os.path.exists(rootFolder):
        raise Exception("Director %s already exists" % rootFolder)
    os.mkdir(rootFolder)
    createMimeTypeFile(rootFolder, 'application/epub+zip')
    createMetaInfFolder(rootFolder)


def createMimeTypeFile(rootFolder, content):
    fhandle = open(rootFolder + '/mimetype', 'w')
    fhandle.write(content)
    fhandle.close()


def createMetaInfFolder(rootFolder):
    metaFolder = rootFolder + '/META-INF'
    os.mkdir(metaFolder)
    shutil.copy(TEMPLATES_DIR + 'container.xml', metaFolder)


def cleanBookFolders(rootFolder):
    if os.path.exists(rootFolder):
        shutil.rmtree(rootFolder)


if __name__ == '__main__':
    bookFolder = os.path.join(os.path.dirname(__file__), '../../dist/test')
    cleanBookFolders(bookFolder)
    createBookFolders(bookFolder)
    print("Book created")