# The test based on unittest module
import unittest
import json
from .context import morphemes

path = "./data"

organizationally = {
                             "word": "organizationally",
                             "status": "FOUND_IN_DATABASE",
                             "morpheme_count": 5,
                             "tree": [
                                 {
                                     "children": [
                                         {
                                             "text": "organ",
                                             "type": "root"
                                         },
                                         {
                                             "text": "ize",
                                             "type": "bound"
                                         }
                                     ],
                                     "type": "free"
                                 },
                                 {
                                     "text": "ion",
                                     "type": "bound"
                                 },
                                 {
                                     "text": "al",
                                     "type": "bound"
                                 },
                                 {
                                     "text": "ly",
                                     "type": "bound"
                                 }
                             ]
                         }
poop = {
                             "status": "FOUND_IN_DATABASE",
                             "word": "poop",
                             "morpheme_count": 1,
                             "tree": [
                                 {
                                     "children": [
                                         {
                                             "text": "poop",
                                             "type": "root"
                                         }
                                     ],
                                     "type": "free"
                                 }
                             ]
                         }
automobile = {
                             "status": "FOUND_IN_DATABASE",
                             "word": "automobile",
                             "morpheme_count": 2,
                             "tree": [
                                 {
                                     "children": [
                                         {
                                             "text": "<auto<mobile",
                                             "type": "root"
                                         }
                                     ],
                                     "type": "free"
                                 }
                             ]
                         }
applesauce_not_found = {'morpheme_count': 1, 'status': 'NOT_FOUND', 'word': 'applesauce'}


class TestSingleWordMorphemeParse(unittest.TestCase):
    def runTest(self):
        print("")
        print("---Single word morpheme parse---")
        m = morphemes.Morphemes(path)
        output = m.parse("organizationally")
        self.assertEqual(output,
                         organizationally,
                         "Failed parse of 'organizationally")

        print("  ✓ PASSED")


class TestSingleWordMorphemeCount(unittest.TestCase):
    def runTest(self):
        print("")
        print("---Single word morpheme count---")
        m = morphemes.Morphemes(path)
        output = m.count("organizationally")
        self.assertEqual(output,
                         5,
                         "Failed count of 'organizationally")

        print("  ✓ PASSED")


class TestMultipleWordMorphemeParse(unittest.TestCase):
    def runTest(self):
        print("")
        print("---Multiple word morpheme parse---")
        m = morphemes.Morphemes(path)
        output = m.parse("organizationally")
        self.assertEqual(output,
                         organizationally,
                         "Failed parse of 'organizationally")
        output = m.parse("poop")
        self.assertEqual(output,
                         poop,
                         "Failed parse of 'poop")
        output = m.parse("automobile")
        self.assertEqual(output,
                         automobile,
                         "Failed parse of 'automobile")
        print("  ✓ PASSED")


class TestMultipleWordMorphemeCount(unittest.TestCase):
    def runTest(self):
        print("")
        print("---Multiple word morpheme count---")
        m = morphemes.Morphemes(path)
        output = m.count("organizationally")
        self.assertEqual(output,
                         5,
                         "Failed count of 'organizationally")
        output = m.count("poop")
        self.assertEqual(output,
                         1,
                         "Failed count of 'poop")
        output = m.count("automobile")
        self.assertEqual(output,
                         2,
                         "Failed count of 'automobile")
        print("  ✓ PASSED")


class TestNotFoundMorphemeOutput(unittest.TestCase):
    def runTest(self):
        print("---Not Found morpheme test---")
        m = morphemes.Morphemes(path)
        output = m.parse("applesauce")
        self.assertEqual(output,
                         applesauce_not_found,
                         "Failed not found test using the word 'applesauce")
        print("  ✓ PASSED")
