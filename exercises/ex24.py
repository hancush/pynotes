print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that to do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "-----------"
print poem
print "-----------"

five = 10 - 2 + 3 - 6
print "This should be five %s" % five

# define function called secret_formula with parameter started
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates # return three values (tuple?)
    
start_point = 10000
# sets values returned by secret_formula() with parameter start_point defined above 
# to given variables, respectively
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
# inserts values from variables defined by tuple returned from function
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

# adjusts value of start_point
start_point /= 10 # op/equals shorthand holds for all mathematical ops apparently

print "We can also do that this way:"
# inserts values returned as tuple directly from function using adjusted start_point 
print "We'd have %d beans, %d jars, %d crates." % secret_formula(start_point)
