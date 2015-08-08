# while-loops: run loop so long as condition true
    # use sparingly (for-loop typically better)
    # review statements to ensure they eventually end up false
    # print test variable @ beginning/end to see what's up

# --- EXERCISE ---

# i = 0
# numbers = []

# while i < 6:
#    print "At the top i is %d" % i
#    numbers.append(i)

#    i += 1
#    print "Numbers now:", numbers
#    print "At the bottom i is %d" % i

# print "The numbers: "

# for num in numbers:
#    print num

# --- REWRITE AS FUNCTION ---

def append_while(x, y):
    i = 0 # define i
    numbers_def = []
    while i < x: # sets upper bound
        # print i # check top
        numbers_def.append(i)
        i += y # sets increment in function
        # print i # check bottom
    print numbers_def

append_while(4, 1)
append_while(69, 3)

# --- REWRITE AS FOR-LOOP, RANGE ---
# incrementor not necessary, can set in range()

def append_for(x, y):
    numbers_for = []
    for num in range (0, x, y): # x sets upper bound, y sets increment
        numbers_for.append(num)
    print numbers_for

append_for(60, 9)
append_for(1985, 5)
