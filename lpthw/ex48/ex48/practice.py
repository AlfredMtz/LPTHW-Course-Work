lexicon = {
        'north':'direction',
        'south':'direction',
        'east':'direction',
        'west':'direction',
        'down':'direction',
        'up':'direction',
        'left':'direction',
        'right':'direction',
        'back':'direction',
        'go':'verb',
        'stop':'verb',
        'kill':'verb',
        'eat':'verb',
        'the':'stop',
        'in':'stop',
        'of':'stop',
        'at':'stop',
        'it':'stop',
        'door':'noun',
        'bear':'noun',
        'princess':'noun',
        'cabinet':'noun',
        }

def scan(sentence):
    pass
    result = []
    """ sentence got its value from scan('input').
        Then it splits it up in parts and will be values 
        for word in the loop.
        For each loop word compare its value(part) 
        to the content in lexicon."""
    sentence = sentence.split()
    for word in sentence:
        wordtype = lexicon.get(word, 'error')
        pair = (wordtype, word)

        """If there is a match it will append the wordtype + word to result. """
        if word in lexicon: #1
            result.append(pair)

            """ Then it look if it is a number(str). 
            If so it convert it with function convert_int to a integer. 
            Then pair adds 'number + the integer to a."""
        elif word not in lexicon: #2
            number = convert_int(word)
            if number:
                pair = ('number', number)

                """If neither of the two previous condition is met, 
                it sets pair to wordtype with its default value (error)"""
            elif word not in lexicon and not number: #3
                pair = (wordtype, word)
            
            # This append from conditions #2 and #3
            result.append(pair)

    #print(result) # For humans
    return result # For Python

# This function is used in condition #2
def convert_int(n):
    try:
        return int(n)
    except:
        print(ValueError)


scan('123 north south east')
