'''
Created on 05-08-2013

@author: klangner
'''
from model.content import Lesson
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


class PageTest(unittest.TestCase):

    def testPageName(self):
        filename = DATA_ROOT + 'lesson1.ic.xml'
        lesson = Lesson(filename)
        page = lesson.getPages()[0]
        self.assertEqual('Introduction', page.getName())

    def testModuleCount(self):
        filename = DATA_ROOT + 'lesson1.ic.xml'
        lesson = Lesson(filename)
        page = lesson.getPages()[0]
        self.assertEqual(3, len(page.getModules()))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()