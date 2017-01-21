class Template:

    def __init__(self, base_str, wordtypes):
        ''' the base string, and a list of word types to ask the user for '''
        self.template_string = base_str
        self.wordtypes = wordtypes


    def fill_in_template(self, userwords):
        ''' use tuple of userwords to populate template base string'''

        # verify there are enough words
        if len(self.wordtypes) != len(userwords):
            raise TemplateException('Length of words provided is different to words needed. %d words expected, %d provided.' % (len(self.wordtypes), len(userwords)) )

        completed_str = self.template_string.format(*userwords)
        return completed_str



class TemplateException(Exception):
    pass
