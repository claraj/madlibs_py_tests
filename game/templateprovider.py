from game.template import Template

def get_template():

    #obtain a template.
    #Could read from a file, or generate a template somehow, but for testing, return a hard coded template
    return test_template()


def test_template():

    base_str = 'One day, {} met a large {} walking {} down the road. \
They became best friends and went on a trip to {} together, where \
they ate delicious {} and bought souvenir {} for their favorite {}.'

    # shouldn't be too hard to come up with a better template :)

    wordtypes = ['name', 'animal', 'adverb', 'place', 'food', 'plural noun', 'profession']

    template = Template(base_str, wordtypes)

    return template
