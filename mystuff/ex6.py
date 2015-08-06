# define x, substitute 10 for %d (indicates a whole integer)
x = "There are %d types of people." % 10
# define binary
binary = "binary"
# define do_not
do_not = "don't"
# define y, substitute respective values of indicated variables for %s (indicating string)
y = "Those who know what %s is and those who %s." % (binary, do_not) # string in string

print x
print y

# print statement, substitute x for %r (indicating raw string)
print "I said: %r." % x # string in string
# print statement, substitute y for %s (indicating string)
print "I also said: '%s'." % y #string in string

# define hilarious
hilarious = False
# define joke evaluation, with variable %r (indicating raw) for answer
joke_evaluation = "Isn't that joke so funny?! %r"

# print joke eval with answer hilarious
print joke_evaluation % hilarious # string in string

# define w
w = "This is the left side of..."
# define e
e = "a string with a right side."

# print values of both variables as single statement
print w + e