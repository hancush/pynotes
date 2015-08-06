from sys import argv

script, thing1, thing2, thing3 = argv

print "This is a thing:", thing1 + "."
print "This is another thing:", thing2 + "."
print "This is a third thing:", thing3 + "."

expl = raw_input("What is %s? " % thing1)

print "Oh I thought it was %s but I see now it is %s." % (thing2, expl)

resp = raw_input("Isn't that silly? \n")

print "Well at least it isn't as silly as %s." % thing3
