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
        self.assertEqual("Lesson 1", lesson.name)

    def testPageCount(self):
        filename = DATA_ROOT + 'lesson1.ic.xml'
        lesson = Lesson(filename)
        self.assertEqual(10, len(lesson.pages))

    def testPageName(self):
        filename = DATA_ROOT + 'lesson1.ic.xml'
        lesson = Lesson(filename)
        page = lesson.pages[0]
        self.assertEqual('Introduction', page.name)


class PageTest(unittest.TestCase):

    def testModuleCount(self):
        filename = DATA_ROOT + 'page1.xml'
        page = Page(filename)
        self.assertEqual(3, len(page.modules))
        
    def testModuleType(self):
        filename = DATA_ROOT + 'page1.xml'
        page = Page(filename)
        module = page.modules[0]
        self.assertEqual('Text', module.moduleType)
        
    def testMoreModuleTypes(self):
        filename = DATA_ROOT + 'page2.xml'
        page = Page(filename)
        modules = page.modules
        self.assertEqual('Shape', modules[1].moduleType)
        self.assertEqual('Button', modules[2].moduleType)
        self.assertEqual('Addon', modules[3].moduleType)


class TextModuleTest(unittest.TestCase):

    def testText(self):
        filename = DATA_ROOT + 'page1.xml'
        page = Page(filename)
        properties = page.modules[0].properties
        self.assertEqual('Text1', properties['id'])
        self.assertEqual('true', properties['isVisible'])
        self.assertEqual('Functional Division', properties['text'])


if __name__ == "__main__":
    unittest.main()