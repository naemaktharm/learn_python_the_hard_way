# def - keyword represent the start of the function

# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# this function takes only one argument
def print_one(arg1):
	print "arg1: %r" % arg1
	
# this function takes no arguments
def print_none():
	print "I got nothin'."
	
# Calling the functions and passing the arguments
print_two("Naem", "Akthar")
print_two_again("Naem", "Akthar")
print_one("first!")
print_none()