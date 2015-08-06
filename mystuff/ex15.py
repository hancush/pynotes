# imports package argv from library sys
from sys import argv

script, filename = argv
# get filename via argv

txt = open(filename)
# open() "returns file object" (file object : file :: dvd player : dvd)

print "Here's your file %r:" % filename
print txt.read()
# tells variable txt, which we set to open(filename) in line 6, 
# to do read command (aka function, method) 
# btw read prints contents of file in terminal
txt.close()

# print "Type the filename again:"
# file_again = raw_input("> ")

# txt_again = open(file_again)

# print txt_again.read()
# txt_again.close()

# set variable1 for filename, filename = raw_input("What file? ")
# set variable2 to open file object for filename, text = open(filename)
# command file object variable to read file, print text.read()