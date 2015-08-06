print "How old are you?",
age = raw_input() # prompts user for answer which it then converts to string for given variable
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input ()

print "So, you're %s old, %s tall and %s heavy." % (
    age, height, weight)
    
# using %r instead of %s prints user responses in '' single quotes
# for this reason %r returns \' escape sequence if response includes '' single quotes
    
  
name = raw_input("What's your name? ")
print "I love you, %s" % name

cat = raw_input("Your cats are named? ")
print "Wow I love %s, too." % cat

# ^ essentially two ways of doing the name thing, with the second way apparently more efficient
# not sure why one favored over the other