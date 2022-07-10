"""
This unitest file tests the various translation
functions in the translator module
"""

import unittest
from machinetranslation import english_to_french, french_to_english

class TestTranslation(unittest.TestCase):
    """
    This class test the translation module functions
    """
    def test_english_to_french(self):
        """
        This test function test the translation of englisj to french
        """
        #self.assertIsNone(english_to_french(None), 'The word is not not null')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Bonjourr')

    def test_french_to_english(self):
        """
        This test function test the translation of french to english
        """
        #self.assertIsNone(french_to_english(None), 'Word is not')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Hey')

unittest.main()
