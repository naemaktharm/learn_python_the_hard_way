# importing argv modules from system - python
from sys import argv

# argument is unpacked and assigned to four variables
script, first, second, third = argv

# print the values in script variable
print "The script is called:", script

# Get the fourth variable value from user
fourth = raw_input("Enter the fourth argument:")

# print the values in four variables 
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth