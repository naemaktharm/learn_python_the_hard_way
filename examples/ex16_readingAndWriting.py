# write - keyword is used to write the data in the file 


# from system import arguments
from sys import argv

# unpacking the arguments and saving it to the variables
script, filename = argv

# print the statements
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# get acceptance from the user
raw_input("?")

# opening the file
print "Opening the file..."
target = open(filename, 'w')

# truncate the contents in the file
print "Truncating the file. Goodbye!"
target.truncate()

# print the statement
print "Now I'm going to ask you for three lines."

# get input from the user and store it to the variables
line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

# print the statement
print "I'm going to write these to the file."

# write the contents of the variables to the file 
target.write(line1 + "\n" + line2 + "\n" + line3)

# print the close message
print "And finally, we close it."
target.close()