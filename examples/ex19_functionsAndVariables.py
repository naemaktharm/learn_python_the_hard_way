# defined a function with input two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You habe %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

# invoke the function with two values passed by	
print "We can give the function numbers directly:"
cheese_and_crackers(20, 30)

# declare two variables with values assigned to it
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# invoke the function with two variables passed by
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# invoke the function with math values passed by
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# invoke the function with variables and values passed by
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def computer_information(person_name, system_name, price):
	print "The candidate name is: %s" % person_name
	print "He/She has the pc %s" % system_name
	print "The cost of the pc is %s \n" % price

print "enter the person name, pc details & price: "
person_name = raw_input(">")
system_name = raw_input(">")
price = raw_input(">")

print ""

computer_information(person_name, system_name, price)
computer_information("Shelly", "mac", "2000$")
computer_information("Naem", "Dell", "1000$")
computer_information("Robert", "Lenovo", "800$")
computer_information("David", "IBM", "750$")
computer_information("Dhelip", "Microsoft", "1900$")
computer_information("Ram", "Asus", "600$")
