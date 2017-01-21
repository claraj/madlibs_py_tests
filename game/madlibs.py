''' The game


run from the directory above this code with

python -m game.madlibs

do it this way so tests will do the imports correctly when run with test discovery (?)


'''

from game import templateprovider

def play():
# get a template

    template = templateprovider.get_template()

    print('Please type in the following types of words:')

    userwords = getwords(template.wordtypes)

    print('Thank you! Here is your completed sentance....')

    completed = template.fill_in_template(userwords)

    print(completed)


def getwords(wordtypes):

    userwords = []

    for wordtype in wordtypes:
        userwords.append(input('Enter a ' + wordtype + ':'))

    return tuple(userwords)
    
