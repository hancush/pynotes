name = 'Hannah E. Cushman'
age = 23 # not a lie
height_in = 56.00 # inches
height_cm = height_in / 0.39
weight_lb = 180.00 # lbs
weight_kg = weight_lb / 2.20
eyes = 'Blue'
teeth = 'Off White'
hair = 'Brown'

print "Let's talk about %s." % name
print "She's %d inches tall." % height_in
print "That's %f centimeters." % height_cm
print "She's %d pounds light." % weight_lb
print "Not American? Try %f kg." % round(weight_kg, 2)
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height_in, weight_lb, age + height_in + weight_lb)



my_name = 'Hannah'
today = 'Wednesday'

if today is 'Wednesday':
    qty = 'no'
else:
    qty = 'some'
    
print "Today %s has %s patience." % (my_name, qty)