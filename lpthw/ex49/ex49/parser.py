import lexicon
import pdb

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

#1 What type of word is the first in the list
def peek(word_list):
    if word_list:
        word = word_list[0]
        # Example: noun, verb, etc..
        return word[0]
    else:
        return None
        
#2. I expect the first word in the list to be a 'noun' 'verb' 'etc..'
# if it is return the word tuple, if is not, then return None.
def match(word_list, expecting):
    # for each tuple in list
    if word_list:
        # pop(i) --> remores item at given position in list and returns it
        word = word_list.pop(0)
        # type of word == to expected
        if word[0] == expecting:
            #pdb.set_trace()
            return word
        else:
            return None
    else:
        return None

#3. Skip words that aren't usefull to the sentence
def skip(word_list, word_type):
    # is the first word in the list == word_type
    while peek(word_list) == word_type:
        # If it is, poped it out from the list and check if its == word_type.
        # if it is return the word(won't show thoguh) because there is not a
        # return statement inside of this loop or function, so just keep running
        # the while loop and updating the word_list until it breaks and you
        # finish with an updated list.
        match(word_list, word_type)
    
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


word_list = lexicon.scan("go to the south")
# While first word in the list is an error.
# Go ahead and get the word list and word type, and
# return the word tuple.
# else ??
# pk = peek(word_list)
# mt = match(word_list, 'error')
# skip(word_list, 'stop')
# print(word_list)
# print(pk)
# print(mt)
# skip(word_list, 'stop')
print(parse_sentence(word_list))
