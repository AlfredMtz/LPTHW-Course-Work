import pdb

'''
The scan() fucntion should take a string sentence,
break it down into words and return a list of tuples
which include the ('wordtype', 'word')
'''

lexicon_dict = {
    'north': 'direction',
    'south': 'direction',
    'east': 'direction',
    'west': 'direction',
    'down': 'direction',
    'up': 'direction',
    'left': 'direction',
    'right': 'direction',
    'back': 'direction',
    'go': 'verb',
    'stop': 'verb',
    'kill': 'verb',
    'eat': 'verb',
    'the': 'stop',
    'in': 'stop',
    'of': 'stop',
    'from': 'stop',
    'at': 'stop',
    'it': 'stop',
    'door': 'noun',
    'bear': 'noun',
    'princess': 'noun',
    'cabinet': 'noun'
}

def scan(words):
    # Change to lower case / Why? Because it makes it able for the user to pass lower or
    # capitalize letters
    words = words.lower()
    # Splits sentence into list of words, now that any words in capital letters have been
    # transform into lowercase letters.
    splitted_words = words.split()
    #pdb.set_trace()

    pairs_list = []

    # for each word in the list of words.
    for word in splitted_words:
        # if word is in the lexicon_diccionary keys
        if word in lexicon_dict.keys():
            pairs = ((lexicon_dict.get(word), word))
            pairs_list.append(pairs)
            pdb.set_trace()
        # else if the word is not in the diccionary keys
        elif word not in lexicon_dict.keys():
            # Try to make a number
            num = convert_number(word)
            # If not a number
            if num == None:
                pairs = ('error', word)
                pairs_list.append(pairs)
            # If a number
            else:
                pairs = (('number', num))
                pairs_list.append(pairs)
        # Otherwise is an error 
        else:
            pass

    #print(pairs_list)
    return pairs_list

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

print(scan('123 south east asldfjsdlf'))