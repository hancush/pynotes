# access elements of list
# zero indexed (item numbers starts @ 0), e.g. third animal at index 2

# given list:
animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

# create list of questions
questions = [
    'The animal at 1.',
    'The third (3rd) animal.',
    'The first (1st) animal.',
    'The animal at 3.',
    'The fifth (5th) animal.',
    'The animal at 2.',
    'The sixth (6th) animal.',
    'The animal at 4.'
]

def trans():
    for n in questions:
        if "at" in n: # if string contains 'at'
            n = int(filter(str.isdigit, n)) # n is the integer in the string
            print animals[n] # return animal at n
        elif "at" not in n: # if string != contain 'at'
            n = (int(filter(str.isdigit, n)) - 1) # n is the integer minus 1 (bc int in string is ordinal not the cardinal number)
            print animals[n] # return animal at n
        else:
            print "No position found" # for errors

trans()

# ---- ROUGH DRAFTS ----

# create cheatsheet, printing animals and positions
# def map():
#    for animal in animals:
#        print animal, animals.index(animal)

# map()

# manually computed positions from questions, return animals at said positions
# print animals[1]
# print animals[2]
# print animals[0]
# print animals[3]
# print animals[4]
# print animals[2]
# print animals[5]
# print animals[4]

# first run of trans() before it contained for-loop
# trans("at 1")
# trans("3rd")
# trans("1st")
# trans("at 3")
# trans("5th")
# trans("at 2")
# trans("6th")
# trans("at 4")
