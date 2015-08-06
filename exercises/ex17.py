# from sys import argv
# returns True if a file exists, else False
# from os.path import exists

#script, from_file, to_file = argv

# print "Copying from $%s to %s" % (from_file, to_file)

# we could for these two on one line, how?
# in_file = open(from_file)
# indata = in_file.read()

# print "The input file is %d bytes long" % len(indata)

# print "Does the output file exist? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, CRTL-C to abort."
# raw_input()

# out_file = open(to_file, 'w')
# out_file.write(indata)

# print "Alright, all done."

# out_file.close()
# in_file.close()

from sys import argv ; script, from_file, to_file = argv
in_file = open(from_file) ; out_file = open(to_file, 'w') ; out_file.write(in_file.read())
in_file.close() ; out_file.close()
