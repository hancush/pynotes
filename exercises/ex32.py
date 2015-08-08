# list: container for information
# list = ['item1', 'item2', 'item3']

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# do this thing for each item in given list
for number in the_count: # for x in y:, x is arbitary name for item, y is list
    print "This is count %d" % number

# and again
for fruit in fruits:
    print "A fruit of type %s" % fruit

# mixed lists are fine, too
# use %r if mix of strings and values
for i in change:
    print "I got %r" % i

# to create empty list, use square brackets
# () is empty set
# {} is empty dictionary
elements = []

# use range to determine number of times loop runs
for i in range (0, 6): # numbers first through last, excluding last
    print "Adding %d to the list" % i # item name given in for-loop can be used as variable
    elements.append(i) # add each value in range to list
    print "Element was: %d" % i

# print what we added
# for i in elements:
#    print "Element was: %d" % i

# other list methods:
    # list.append(x) - add item, x, to end of list
    # list.extend(L) - append items in given list, L, to end of list
    # list.insert(i, x) - insert item, x, before item in postion, i
    # list.remove(x) - remove first item with value, x
    # list.pop(i) - remove/return item at given position, i (optional)
        # if not specified, remove/return last item
    # list.index(x) - return index (position) of first item with value, x
    # list.count(x) - return number of times value, x, appears in list
    # list.sort() - sort items in place, return none
        # sorted(list) - return sorted list (works with any iterable) w/o altering order of source
    # list.reverse() - reverse items in list in place
# see also: sets, dictionaries
