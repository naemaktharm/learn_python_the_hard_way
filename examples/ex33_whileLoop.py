# variable declaration
i = 0

# initialized a list
numbers = []

# while loop operation
# adding numbers to the list - numbers
while i < 6:
	print "At the top of the while loop, i is %d" % i
	numbers.append(i)
	
	# incremented the value of i
	i  += 1
	
	# print the list
	print "Numbers list now: ", numbers
	print "At the bottom of the while loop, i is %d" % i
	
# print the numbers in the list
print "The numbers in the list: "

for num in numbers:
	print num
	
def print_list(list, end_limit):
	i = 0
	# while loop operation
	# adding numbers to the list - numbers
	list_1 = list
	list_2 = new list
	print list_1
	print list_2

	while i < end_limit:

		list_1.append(i)
		
		# incremented the value of i
		i  += 1
	print list_1
	print list_2
	for i in range(0, end_limit):
		list_2.append(i)
		
	print list_2
	
list_example = []
print_list(list_example, 8)

