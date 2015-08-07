# assign values to variables
people = 30
cars = 40
trucks = 15

# decides what to print based on values
if cars > people: # more cars than people (true)
    print "We should take the cars." 
elif cars < people: # else + if (works like or), fewer cars than people (false)
    print "We should not take the cars." 
else: # if neither condition is met (that is to say, both of the above are false)
    print "We can't decide." 
# note: python runs first block that is true then stops parsing sequence
    
if trucks > cars: # more trucks than cars (false)
    print "That's too many trucks."
elif trucks < cars: # more cars than trucks (true)
    print "Maybe we could take the trucks."
else: # false
    print "We still can't decide."
    
if people > trucks: # more people than trucks (true) 
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."