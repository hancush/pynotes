# dictionaries

# map state to abbreviation
states = {
    "Oregon": "OR",
    "Florida": "FL",
    "California": "CA",
    "New York": "NY",
    "Michigan": "MI"
}

# map state abbreviation to city
cities = {
    "CA": "San Francisco",
    "MI": "Deroit",
    "FL": "Jacksonville"
}

# add key/values to cities
cities["NY"] = "New York"
cities["OR"] = "Portland"

# print cities
print "-" * 10
print "Michigan's abbreviation is: ", states["Michigan"]
print "Florida's abbreviation is: ", states["Florida"]

# print states
print "-" * 10
print "Michigan has: ", cities[states["Michigan"]]
print "Florida has: ", cities[states["Florida"]]

# print state abbrevations
print "-" * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s." % (state, abbrev)

# print cities in states
print "-" * 10
for abbrev, city in cities.items():
    print "%s has the city %s." % (abbrev, city)

# do both
print "-" * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s and has city %s." % (
        state, abbrev, cities[abbrev])

print "-" * 10
# safely attempt to get abbreviation for state not in list
state = states.get("Texas")
if not state:
    print "Sorry, not available!"

city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
