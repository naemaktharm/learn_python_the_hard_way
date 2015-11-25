# open keyword used to open the file
# read keyword is used to read the data in the opened file


# from system import arguments
from sys import argv

# unpacking the arguments and assigning it to variables
script, filename = argv

# open the file and assign to variable txt
txt = open(filename)

# print the file name 
print "Here's your file %r:" % filename

# print the text in the file - filename
print txt.read()

# prints the message
print "Type the filename again:"

# second time the file is assigned to the variable 
file_again = raw_input("> ")

# open the file and assign to variable txt_again
txt_again = open(file_again)

# print the text in the file - file_again
print txt_again.read()