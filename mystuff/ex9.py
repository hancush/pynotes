# Here's some new strange stuff, remember type it out exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
# /n creates new line, doesn't work in %r (which "prints it the way you wrote it (or close to it)")
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

print "The months are %r" % months

# 3x double quotes let you type strings with multiple lines, one of several "escape sequences"
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""