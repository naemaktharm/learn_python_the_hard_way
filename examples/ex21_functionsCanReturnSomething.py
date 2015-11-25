# function for adding two numbers
def add (a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

# functions for subtracting two numbers	
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

# function for multiplying two numbers	
def multiply(a, b):
	print "MULTIPLY %d * %d" % (a, b)
	return a * b

# function for dividing two numbers	
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	
# print a statement
print "Let's do some math with just functions!"

# invoke the add function and assign it to variable "age"
age = add(30, 5)

# invoke the subtract function and assign it to variable "height"
height = subtract(78, 4)

# invoke the multiply function and assign it to variable "weight"
weight = multiply(90, 2)

# invoke the divide function and assign it to variable "iq"
iq = divide(100, 2)

# print the values in age, height, weight & iq
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

# result of one function is passed as an argument to another function 
#	and assigning to variable "what"
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# print the value in the variable "what"
print "That becomes: ", what, "can you do it by hand?"

# function for converting km/h to miles/hr
def kmPerHr_to_milesPerHr(kmPerHr):
	milesPerHr = kmPerHr / 1.609344 
	return milesPerHr
	
# function for converting miles/hr to km/hr
def milesPerHr_to_kmPerHr(milesPerHr):
	kmPerHr = milesPerHr * 1.609344 
	return kmPerHr
	
speed_in_kmPerHr = float(raw_input("Enter your vehicle speed in km/hr :"))
print "Speed in miles/hr: " , kmPerHr_to_milesPerHr(speed_in_kmPerHr)

speed_in_milesPerHr = float(raw_input("Enter your vehicle speed in miles/hr :"))
print "Speed in km/hr: " , milesPerHr_to_kmPerHr(speed_in_milesPerHr)