'''
Created on 05-08-2013

@author: klangner
'''
from model.content import Lesson, Page
import os.path
import unittest

DATA_ROOT = os.path.join(os.path.dirname(__file__), 'data/')


class LessonTest(unittest.TestCase):

    def testName(self):
        filename = DATA_ROOT + 'lesson1.ic.xml'
        lesson = Lesson(filename)
        self.assertEqual("Lesson 1", lesson.getName())

    def testPageCount(self):
        filename = DATA_ROOT + 'lesson1.ic.xml'
        lesson = Lesson(filename)
        pages = lesson.getPages()
        self.assertEqual(10, len(pages))

    def testPageName(self):
        filename = DATA_ROOT + 'lesson1.ic.xml'
        lesson = Lesson(filename)
        page = lesson.getPages()[0]
        self.assertEqual('Introduction', page.getName())


class PageTest(unittest.TestCase):

    def testModuleCount(self):
        filename = DATA_ROOT + 'page1.xml'
        page = Page(filename)
        self.assertEqual(3, len(page.getModules()))
        
    def testModuleType(self):
        filename = DATA_ROOT + 'page1.xml'
        page = Page(filename)
        module = page.getModules()[0]
        self.assertEqual('Text', module.getType())
        
    def testMoreModuleTypes(self):
        filename = DATA_ROOT + 'page2.xml'
        page = Page(filename)
        modules = page.getModules()
        self.assertEqual('Shape', modules[1].getType())
        self.assertEqual('Button', modules[2].getType())
        self.assertEqual('Addon', modules[3].getType())


if __name__ == "__main__":
    unittest.main()