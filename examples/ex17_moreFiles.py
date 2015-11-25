# close keyword is used to close the opened file for read or write

# imports arguments from system
from sys import argv

# import exists function from os.path
from os.path import exists

# unpacking the arguments and assigning it to the variables
script, from_file, to_file = argv

# print the information
print "Copying from %s to %s" % (from_file, to_file)

# open one file and read the data 
# we could do these two on one line, how?
in_file = open(from_file, 'r')
indata = in_file.read()

# print the length of the data in file 1
print "The input file is %d bytes long" % len(indata)

# checking whether the output file is exist or not?
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

# open the second file and write the data in second file
out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

# close the files
out_file.close()
in_file.close()