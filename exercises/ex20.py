# import argv
from sys import argv

# set arguments
script, input_file = argv

# define function print_all with parameter f
def print_all(f):
# return contents of f
    print f.read()

# define function rewind with parameter f    
def rewind(f):
# move back to beginning of file (0th byte)
    f.seek(0)
# f.tell() returns position in file (again, in bytes... each character is essentially a byte)
# standard format: f.seek(offset, from_what) 


# define function print_a_line with parameters line_count and f   
def print_a_line(line_count, f):
# return current line, contents of that line
    print line_count, f.readline()
    
# creates file object for input_file (original input) named current_file
current_file = open(input_file)

# returns phrase
print "First let's print the whole file:\n"

# returns entire contents of input_file via file object current_file
print_all(current_file)

# returns phrase
print "Now let's rewind, kind of like a tape."

# go back to top of file (i.e. typewriter) via f.seek(0), see above
rewind(current_file)

returns phrase
print "Let's print three lines:"

# set current_line
current_line = 1
# return manually set current_line (line count in function), first line of file f.readline()
print_a_line(current_line, current_file)

# adds one to current_line
# x = x + y --> x += y
current_line =+ 1
# return current_line and second line of file
print_a_line(current_line, current_file)

# again
current_line =+ 1
print_a_line(current_line, current_file)