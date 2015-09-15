#--COMPOSITION--#
# Other is-a object
class Other(object):

    def override(self): # Other has-a function named override
        print "OTHER override()"

    def implicit(self): # and one named implicit
        print "OTHER implicit()"

    def altered(self): # and one named altered
        print "OTHER altered()"

# Child is-a object (inherits none)
class Child(object):

    def __init__(self): # Child has-a __init__
        self.other = Other() # which sets self.other equal to an instance of the class Other
        # Child has-a instance of Other

    def implicit(self): # Child has-a function named implicit
        self.other.implicit() # which calls the function implicit defined by Other

    def override(self): # Child also has-a function named override
        print "CHILD OVERRIDE()" # which returns string @ left (as opposed to calling function named override in Other)

    def altered(self): # Child has-a function named altered
        print "CHILD BEFORE OTHER altered()" # which prints string @ left
        self.other.altered() # then string from function of same name in Other
        print "CHILD AFTER OTHER altered()" # and finally string @ left

son = Child() # set son equal to an instance of Child

son.implicit()
son.override()
son.altered()
