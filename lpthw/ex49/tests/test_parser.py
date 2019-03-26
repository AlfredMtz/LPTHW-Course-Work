import pytest
from ex49 import lexicon
from ex49 import parser

def test_subject():
    sentc = parser.Sentence(('noun', 'player'),
                            ('verb', 'go'), ('direction', 'north'))
    assert sentc.subject == 'player'
    assert sentc.verb == 'go'
    assert sentc.object == 'north'

def test_peek():
    word_list = []
    assert parser.peek(word_list) == None

    word_list = [('noun', 'player'), ('verb', 'go'), ('direction', 'north')]
    assert parser.peek(word_list) == 'noun'

    word_list = lexicon.scan('123 south st')
    assert parser.peek(word_list) == 'number'

def test_match():
    # Empty list
    word_list = []
    assert parser.match(word_list, None) == None

    # The word_list changes once it is run once
    word_list = [('noun', 'player'), ('verb', 'go'), ('direction', 'north')]
    assert parser.match(word_list, 'noun') == ('noun', 'player')
    assert parser.match(word_list, 'direction') == None

    # help of the scan fucntion
    word_list = lexicon.scan('123 in the south')
    assert parser.match(word_list, 'number') == ('number', 123)
    
def test_skip():
     word_list = lexicon.scan('123 in the south')
     assert parser.skip(word_list, 'stop') == None
     assert parser.match(word_list[1:], 'stop') == ('stop', 'in')

     word_list = lexicon.scan('the princess go')
     assert parser.skip(word_list, 'stop') == None
     
def test_parse_verb():
    word_list = lexicon.scan('go to the norht')
    assert parser.parse_verb(word_list) == ('verb', 'go')
    word_list = lexicon.scan('in the go north')
    assert parser.parse_verb(word_list) == ('verb', 'go')
    # How do I assert that I raise an error if not verb.

def test_parse_object():
    word_list = lexicon.scan('in the door')
    assert parser.parse_object(word_list) == ('noun', 'door')
    word_list = lexicon.scan('in the north')
    assert parser.parse_object(word_list) == ('direction', 'north')
    # How do I assert that I raise an error if not verb.

def test_parse_subject():
    word_list = lexicon.scan('Go to the princess')
    assert parser.parse_subject(word_list) == ('noun', 'player')
    word_list = lexicon.scan('the princess')
    assert parser.parse_subject(word_list) == ('noun', 'princess')
    
    # It expects a verb or a noun after 'the' is skipped,
    # however a direction 'north' was given instead.
    word_list = lexicon.scan('the north princess')
    with pytest.raises(parser.ParserError):
        # run the code that trigger the exception
        parser.parse_subject(word_list)

def test_parse_sentence():
    word_list = lexicon.scan('the bear run south')
    sent = parser.parse_sentence(word_list)
    assert sent.subject == 'bear'
    assert sent.verb == 'run'
    assert sent.object == 'south'

    # It should raise a parse error because it expects an object
    # with a 'noun' or 'direction', but the verb 'eat' is given.
    word_list = lexicon.scan('the bear go to eat')
    with pytest.raises(parser.ParserError):
        parser.parse_sentence(word_list)
