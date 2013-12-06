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

    def testStyle(self):
        filename = DATA_ROOT + 'lesson1.ic.xml'
        lesson = Lesson(filename)
        self.assertEqual(".myclass{}", lesson.style)

    def testPageCount(self):
        filename = DATA_ROOT + 'lesson1.ic.xml'
        lesson = Lesson(filename)
        self.assertEqual(6, len(lesson.pages))

    def testPageName(self):
        filename = DATA_ROOT + 'lesson1.ic.xml'
        lesson = Lesson(filename)
        page = lesson.pages[0]
        self.assertEqual('Introduction', page.name)


class PageTest(unittest.TestCase):

    def testModuleCount(self):
        filename = DATA_ROOT + 'page1.xml'
        page = Page(filename)
        self.assertEqual(4, len(page.modules))
        
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
        self.assertEqual('text_activity', properties['class'])
        self.assertEqual('Functional Division', properties['text'])


class ButtonModuleTest(unittest.TestCase):

    def testButtonType(self):
        filename = DATA_ROOT + 'buttons.xml'
        page = Page(filename)
        resetButton = page.modules[0].properties
        checkAnswersButton = page.modules[1].properties
        self.assertEqual('reset', resetButton['buttonType'])
        self.assertEqual('checkAnswers', checkAnswersButton['buttonType'])


class ChoiceModuleTest(unittest.TestCase):

    def testProperties(self):
        filename = DATA_ROOT + 'choice.xml'
        page = Page(filename)
        properties = page.modules[0].properties
        self.assertEqual('Choice1', properties['id'])
        self.assertEqual('true', properties['isVisible'])
        self.assertEqual('true', properties['isMulti'])

    def testOptions(self):
        filename = DATA_ROOT + 'choice.xml'
        page = Page(filename)
        properties = page.modules[0].properties
        self.assertEqual(3, len(properties['options']))

    def testCorrectOption(self):
        filename = DATA_ROOT + 'choice.xml'
        page = Page(filename)
        properties = page.modules[0].properties
        option = properties['options'][1]
        self.assertEqual(1, option['value'])
        self.assertEqual('This is a correct answer', option['text'])


class ImageModuleTest(unittest.TestCase):

    def testProperties(self):
        filename = DATA_ROOT + 'page1.xml'
        page = Page(filename)
        properties = page.modules[3].properties
        self.assertEqual('Image1', properties['id'])
        self.assertEqual('true', properties['isVisible'])
        self.assertEqual('395', properties['width'])
        self.assertEqual('280', properties['height'])
        self.assertEqual('../resources/1817685.jpg', properties['src'])


if __name__ == "__main__":
    unittest.main()