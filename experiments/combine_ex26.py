def break_sort(sentence):
    words = sentence.split(' ') 
    print "These are the words:" 
    print words
    print "These are the sorted words:" 
    print sorted(words)
    print "This is the first word:" 
    print words.pop(0)
    print "This is the first sorted word:" 
    print sorted(words).pop(0)
    print "This is the last word:" 
    print words.pop(-1)
    print "This is the last sorted word:"
    print sorted(words).pop(-1)
    
sentence = "Phil is too cute to function."

break_sort(sentence)