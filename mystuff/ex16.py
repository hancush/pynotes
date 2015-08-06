# variables set: script, filename, target, line1, line2, line3

# import argv from sys...
from sys import argv

# ...to tell command line this is key for your entry
script, filename = argv

# print the following, subbing in entered filename for %r
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do what that, hit RETURN."

# prompts user to do one of the above; ctrl-c aborts script via KeyboardInterrupt
raw_input("?")

# opens file in write mode (default open mode is 'r', or read)
# opening file in write mode automatically overwrites its existing contents
# open(filename, 'r')
#   1      2      3
# 1 is open command, 2 filename, 3 mode in which file to be opened
# modes: r - read, w - write (truncating file on open automatically),
# a - append,  r+,w+,a+ - open for updating, b - binary
# U or rU - universal newlines
# you can't read a file opened in w mode, etc
print "Opening the file..."
target = open(filename, 'w')

# deletes contents of file
# unnecessary after opening file in 'w'
# print "Truncating the file. Goodbye!"
# target.truncate()

print "Now I'm going to ask you for three lines."

# presents user for following prompts
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write("%s \n%s \n%s" % (
    line1, line2, line3))

print "And now we get outta write mode."
target.close()

target_read = open(filename)
    
print "Now let's see what we've got."
print target_read.read()

print "And finally, we close it."
target_read.close()
