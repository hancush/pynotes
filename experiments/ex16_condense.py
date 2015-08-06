from sys import argv

script, file = argv

open = open(file)

print "Let's read"
print open.read()

print "All done."
open.close()
