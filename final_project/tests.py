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
        #self.assertEqual(english_to_french(None), None)
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_french_to_english(self):
        """
        This test function test the translation of french to english
        """
        #self.assertEqual(french_to_english(None), None)
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()
