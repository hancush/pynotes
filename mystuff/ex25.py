# blueprint for later use inline
# from command line, enter python shell
# import ex25, then call functions ex25.function
# or, from ex25 import * (import all functions from ex25), call functions w/o ex25 

# creates function break words, parameter stuff
def break_words(stuff):
    """This function will break up words for us.""" # expl in help(file) 
    # split() is another string method, which will delimit each word in string 
    # with specified character, in this case single quotes
    words = stuff.split(' ')
    # set value to words in string, sentence, like so: ['word', 'word', 'word']
    # this is called a list
    return words
    
def sort_words(words):
    """Sorts the words."""
    # sorted() is yet another string method 
    # list.sort() is also a thing
    # returns nothing but sorts list permanently, i.e.
    # list = ['phil', 'is', 'so', 'cute']
    # list.sort()
    # list
    # ['cute', 'is', 'phil', 'so']
    return sorted(words)
    
def print_first_word(words):
    """Prints the first word after popping it off."""
    # pop() removes/returns word in specified position in list
    # it defaults to the last item
    # 0 is first and so on
    word = words.pop(0)
    # prints first word in unsorted list
    print word
    
def print_last_word(words):
    """Prints the last word after popping it off."""
    # negative notation to specify list item position means -nth item from list's end
    # and since 0 is first item and 0 can't be negative, last word is -1 and so on
    word = words.pop(-1)
    print word
    
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    # sets variable words equal to list of composite words in string sentence
    words = break_words(sentence)
    # runs said list through sort_words function to return sorted words
    return sort_words(words)
    
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    # sets variable words equal to list of composite words in string sentence
    words = break_words(sentence)
    # returns first word of sentence
    print_first_word(words)
    # returns last word of sentence
    print_last_word(words)
    # both of which are then removed from list
    
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last oen."""
    # sets variable words equal to sorted list of composite words
    # produced by function sort_sentence
    words = sort_sentence(sentence)
    # prints first word of sorted list
    print_first_word(words)
    # prints last word of sorted list
    print_last_word(words)
    # both of which are then removed from list