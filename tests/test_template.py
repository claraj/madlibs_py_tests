import unittest

from game import template



''' run from directory above this one with

python -m unittest

which performs test discovery and runs all the tests in this package

or,

python -m unittest tests.test_template

'''


class TestMadLibs(unittest.TestCase):

    def test_fill_in_template_with_correct_number_of_words(self):

        test_base = 'There once was a {} who went to {} for a {} party.'
        test_word_types = ['whatever', 'whatever', 'whatever']  # so long as there's 3 things
        test_user_words = ('fish', 'Chicago', 'trampoline')
        tmpl = template.Template(test_base, test_word_types)
        expected_completed = 'There once was a fish who went to Chicago for a trampoline party.'

        self.assertEqual(tmpl.fill_in_template(test_user_words), expected_completed)


    def test_fill_in_template_with_wrong_number_of_words(self):

        test_base = 'There once was a {} who went to {} for a {} party.'
        test_word_types = ['whatever', 'whatever', 'whatever']  # so long as there's 3 things
        test_user_words_too_few = ('fish', 'Chicago')  # not enough words
        test_user_words_too_many = ('fish', 'Chicago', 'trampoline', 'cheese', 'wombat')  # too many words
        tmpl = template.Template(test_base, test_word_types)

        self.assertRaises(template.TemplateException, tmpl.fill_in_template, test_user_words_too_few)
        self.assertRaises(template.TemplateException, tmpl.fill_in_template, test_user_words_too_many)
