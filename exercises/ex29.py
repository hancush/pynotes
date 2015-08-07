people = 20
cats = 30
dogs = 15

if people < cats:
    print "Too many cats! The world is doomed!"
    
if people > cats:
    print "Not many cats! The world is saved!"
    
if people < dogs:
    print "The world is drooled on!"
    
if people > dogs:
    print "The world is dry!"
    
dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."
    
if people <= dogs:
    print "People are less than or equal to dogs." 
    
if people == dogs:
    print "People are dogs."
    
# study questions:
# 1. if makes code beneath conditional to following statement
# 2. code indented to specify which parts of code are conditional (like function)
# 2a. lines ending with colon signify code blocks, which must be indented
# 3. if not indented, line not read as conditional