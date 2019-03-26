#import lexicon


# Parser Error Exception class
class ParserError(Exception):
    pass
# Sentence object
class Sentence(object):

    def __init__(self, subject, verb, obj):
        # remember we take ('noun', 'princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]

#1. returns what type of word a the list have
def peek(word_list):
    if word_list:
        word = word_list[0]
        # Example: noun, verb, etc..
        return word[0]
    else:
        return None
        
#2. What kind of sentence are we dealing with? it is a direction
# a noun, a verb? What is it?
def match(word_list, expecting):
    # for each tuple in list
    if word_list:
        # save the tuple in position [0] to 'word'
        word = word_list.pop(0)
        # if the type of word is equals to expected
        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

#3. Skip words that aren't usefull to the sentence
def skip(word_list, word_type):

    while peek(word_list) == word_type:
        match(word_list, word_type)
        # The while loop is not returning anything, match()
        # returns a value, but the while-loop keeps running
        # until finally breaks and returns None. So the return
        # values of match are not being save or return anywhere.
        # The only thing that returns is the None value when
        # the loop breaks. This is how its call skiping this
        # words and finally returning None

def parse_verb(word_list):
    # breake the loop and run next block of code once
    # a word in not a 'stop' word
    skip(word_list, 'stop')

    # if the next word in the list is verb
    if peek(word_list) == 'verb':
        # return (type, word)
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")


def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")

def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a verb next.")
    
def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)
'''
word_list = lexicon.scan('in the north')
parse_verb(word_list)
'''