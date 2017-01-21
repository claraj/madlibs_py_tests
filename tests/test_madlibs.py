import unittest
from unittest import mock
from unittest.mock import patch
from unittest.mock import MagicMock

import re

from game import template, madlibs

''' run from directory above this one with

python -m unittest

which performs test discovery and runs all the tests in this package

or,

python -m unittest tests.test_madlibs

'''

class TestMadLibsGame(unittest.TestCase):

    #Testing that input is asking the right questions. Could combine with method below.
    def test_ask_user_for_words_check_for_correct_questions_printed(self):

        test_word_types = ['noun', 'adjective', 'verb', 'noun']
        test_user_supplied_answers = ('cake', 'blue', 'walking', 'snow')

        madlibs.input = MagicMock(side_effect=test_user_supplied_answers)   # Return these values from each successive call to input

        wordsret = madlibs.getwords(test_word_types)
        wordsexp = tuple(test_user_supplied_answers)

        self.assertIsInstance(wordsret, tuple, 'expected tuple for wordsret, but got type = ' + str(type(wordsret)))
        self.assertIsInstance(wordsexp, tuple, 'expected tuple for wordsexp, but got type = ' + str(type(wordsexp)))
        self.assertEqual(wordsexp, wordsret)

        call_args = madlibs.input.call_args_list

        for call, test_word_type in zip(call_args, test_word_types):
            out_string = call[0][0]
            if test_word_type not in out_string:
                self.fail('Question ' + out_string + ' did not include the word ' + test_word_type)


    def test_ask_user_for_words_check_for_correct_return(self):

        # verify returns list of user inputs

        test_word_types = ['noun', 'adjective', 'verb', 'noun']

        test_user_supplied_answers = ('cake', 'blue', 'walking', 'snow')

        madlibs.input = MagicMock(side_effect=test_user_supplied_answers)   # Return these values from each successive call to input

        wordsret = madlibs.getwords(test_word_types)
        wordsexp = tuple(test_user_supplied_answers)

        self.assertIsInstance(wordsret, tuple, 'expected tuple for wordsret, but got type = ' + str(type(wordsret)))
        self.assertIsInstance(wordsexp, tuple, 'expected tuple for wordsexp, but got type = ' + str(type(wordsexp)))
        self.assertEqual(wordsexp, wordsret)


        #TODO what about patching approach to this?
