# speeding through this to get to for-loops in next lesson
# note to self: blocks inside blocks is called nesting

# first prompt
print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

# first answer
door = raw_input("> ")

# if answer is 1
if door == "1":
    print "There's a giant bear here each a cheesecake. What do you do?" # second_prompt.1
    print "1. Take the cake."
    print "2. Scream at the bear."
    
    bear = raw_input("> ") # second_answer.1
    
    # outcomes based on second_answer.1
    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

# if answer is 2        
elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina." # second_prompt.2
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."
    
    insanity = raw_input("> ") # second_answer.2
    
    # outcomes based on second_answer.2
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

# if answer is anything else
else:
    print "You stumble around and fall on a knife and die. Good job!"