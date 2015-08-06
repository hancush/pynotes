cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# NameError is when you haven't defined the variable you've asked the program to define; in this case, asked for car_pool_capacity when our defined variable was carpool_capacity; spaces matter 

voters = 1000
candidates = 3
majority_votes = voters / candidates + 1

print "How many people need to vote for one candidate to win a majority of votes?"
print majority_votes

print "Hey %s there." % "you"

