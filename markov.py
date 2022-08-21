"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    with open(file_path) as file: 
        content = file.read()
    # your code goes here

    return content


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    list_of_words = text_string.split()
    # print(list_of_words)

    chains = {}
    
    for index in range(len(list_of_words)-2):       
        key = (list_of_words[index], list_of_words[index + 1]) #getting tuple bigram
        next_word = list_of_words[index +2] #next element to new tuple bigram
        # print(key)
        # print(next_word)

        value_list = chains.get(key, []) # value_list is the value from pair "key:value"
        value_list.append(next_word)
        chains[key] = value_list
    return chains



def make_text(chains):
    """Return text from chains."""

    words = []

    random_key = choice(list(chains.keys())) #choice is picking a random key. list is making it a list. keys function is getting all the keys
    words += random_key
    # print(words)

    while random_key in chains.keys():
        values_list = chains[random_key]
        random_value = choice(values_list)
        words.append(random_value)
        random_key = (random_key[1], random_value)            
   
    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)
#print(input_text)

# Get a Markov chain


chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

