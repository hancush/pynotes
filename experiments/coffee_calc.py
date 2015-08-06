print "How much do I spend on coffee?"

print "Calculate 1 coffee @ $3.50, 5 days a week, 50 weeks a year."
coffee = 5 * 3.5 * 50
print "$", coffee

if coffee >= 500:
    print "Damn!"
else:
    print "Oh, that's not bad." 
    
print "What about you? (respond in number format)"

qty = int(raw_input("How many times do you buy coffee a day? "))
cost = int(raw_input("How much does that cost? "))
days = int(raw_input("How many days a week? "))
weeks = int(raw_input("How many weeks a year? "))

print "Calculate %d coffee at $%d, %d days a week, %d weeks a year." % (
    qty, cost, days, weeks)
user_coffee = cost * days * weeks
print "$", user_coffee

if user_coffee >= coffee:
    print "Damn! That's even more than me!"
else:
    print "Oh, that's not bad." 