#--OVERRIDE EXPLICITLY--#
# Parent class is-a object
class Parent(object):

    def override(self): # Parent has-a function called override
        print "PARENT override()" # which prints the string @ left

# Parent has-a Child class (Child inherits attributes from Parent)
class Child(Parent):

    def override(self): # Child also has-a function called override, which overrides function of same name in Parent
        print "CHILD override()" # to print the string @ left

dad = Parent() # set dad equal to instance of Parent
son = Child() # set son equal to instance of Child

dad.override() # call override function on Parent object
son.override() # call override function on Child object
