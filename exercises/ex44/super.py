#--SUPER--#
# Parent is-a object
class Parent(object):

    def altered(self): # Parent has-a function named altered
        print "PARENT altered()" # which prints string @ left

# Parent has-a Child
class Child(Parent):

    def altered(self): # Child also has-a function named altered
        print "CHILD BEFORE PARENT altered()" # which prints string @ left
        super(Child, self).altered() # calls super function with args child and self, then calls altered function on super's returned value (research what args super() takes)
        print "CHILD AFTER PARENT altered()" # and finally prints string @ left

dad = Parent()
son = Child()

dad.altered()
son.altered()
