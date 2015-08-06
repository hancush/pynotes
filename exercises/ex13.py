from sys import argv
# from/import adds python feature to reduce program size, specify doc for other programmers
# argv = argument variable, "holds" arguments you specify while script is running
# feature actually = module (or sometimes library)

script, first, second, third = argv
# tells command line the four items input determine string values of named variables
# useful to run the same program with several different strings, basically a wild card you set when running the program
# $ python ex13.py var1 var2 var3

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third