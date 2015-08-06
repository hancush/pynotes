def cyberbully(social_network):
    print "Dang, %s?" % social_network,
    if int(social_network) > 500:
        print "You have more than me. :("
    else:
        print "lol loser"

twitter = raw_input("How many Twitter followers do you have? ")        
cyberbully(twitter)

facebook = raw_input("How many Facebook friends do you have? ")
cyberbully(facebook)

cyberbully(raw_input("What's ur karma score? "))