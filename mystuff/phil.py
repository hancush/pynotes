thing1 = raw_input("Name an object! \n")
thing2 = raw_input("How 'bout another? \n")
thing3 = raw_input("One more! \n")

expl = raw_input("Tell me more about %s. \n" % thing1)

print "Oh, %s? Is that so?" % expl,
raw_input("Well how's that different from %s? \n" % thing2)

print "Well I love %s, %s and %s, but I love you the most! Pizza?" % (
    thing1, thing2, thing3)