# 'doing things to lists'
#
# what happens when you call a list, python :
#   finds mentioned variable
#   considers possible functions for variable type
#   selects match from available functions for type
#   calls function with variable declared in paratheses
# list.append("argument") --> append(mystuff, "argument")
# use lists to :
#   maintain order
#   access contents randomly
#   access contents linearly
#
# class : logically related group of data, functions (methods) -- from: http://bit.ly/1TZVhNb
#   class != object, tho often used interchangably
#   self is generic variable used in writing classes to be filled with data on each instance
#       methods containing self = "instance methods"
#   __init__ method should set all necessary attributes to call all functions in class :
#       "it should be impossible for an object to get into an invalid state just by calling its methods"
#   class Class(object): # object implies "no inheritance"
#       static = !value
#       def __init__(self, arg1, arg2): # blueprint for each instance, should define all attributes
#           self.arg1 = !value
#           self.arg2 = !value
#       def function(self, arg1):
#           somecode
#           somecode
#   call class like function, i.e. Class(arg1, arg2, arg3)
#       inst = Class(arg1, arg2)
#           for __init__, varName passed in, hence self parameter in def'n, i.e. Class(inst, arg1, arg2)
#       "use class blueprint to create object, 'class instance'"
#   can then call functions defined for class on instance
#       inst.function(arg1)
#   as well as instance methods, static methods (vars or fxns) can be set for attributes true for all instances
#       static methods can be called via Class.method or Inst.method
#       precede any static method fxns with @staticmethod decorator
#   finally class methods can be set preceded by @classmethod decorator
#       passed Class rather than instance
#   inheritance : process by which "child" derives dates/behavior of "parent"
#       Liskov Substitution Principle : child class acceptable wherever parent class expected
#   "abstract base class" : class comprising universal formulas to be passed to tangible classes/instances
#       to prevent creation of ABC instance : 'from abc import ABCMeta, abstractmethod', then set '__metaclass__ = ABCmeta' within abc
#       create @abstractmethod--def fxn(): pass--at end of parent to be inherited and defined by child--def fxn(self): return '!value'
#       to pass to child class : class Child(Parent):

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding:", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])
