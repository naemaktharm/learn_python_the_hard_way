# print two statements
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

# assigning five lines poem to the variable - poem
poem = """
\tThe lovely world
with logic so firmly planted 
cannot discern \n the needs of lovely
nor comprehendpassion from intuituion
and requires an explanation
\n\t\twhere there is none.
"""

# printing the poem
print "----------------"
print poem
print "----------------"

# doing little math and assigning a value to the variable - five
five = 10 - 2 + 3 - 6

# printing the variable value - five
print "This should be five: %s" % five

# function is created and it called by passing one values, three values are returned from the function
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

# assigning a value to the variable - start_point	
start_point = 10000

# secret_formula - function is called by passing start_point and assigned the return values to beans, jars and crates
beans, jars, crates = secret_formula(start_point)

# print the values in start_point, beans, jars and crates
print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

# start_point is processed and assigned back to start_point
start_point = start_point / 10

# secret_formula is agained called with the new start_point value
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)