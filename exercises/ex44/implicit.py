#--IMPLICIT--#
# Parent class is-a object
class Parent(object):

    def implicit(self): # Parent has-a function named implicit
        print "PARENT implicit()" # which prints string @ left

# Parent has-a Child class
class Child(Parent):
    pass # Child has-a empty block; it inherits all attributes and functionality from Parent

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
