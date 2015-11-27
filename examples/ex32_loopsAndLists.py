the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'pears', 'raspberry', 'mango']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number
	
# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit
	
# also we can go through the mix list too
# notice we have to use %r as we don't know what is in the list
for i in change:
	print "I got %r" % i

# we can also build list, first start with the empty one
elements = []
test_elements = []
test_elements = range(0,6)
print test_elements

# then use the range function in python to do 0 to 5 count
for i in range(0, 6):
	print "Adding %d to the list - elements" % i
	# append is a function that list understands
	elements.append(i)

# now we can print the values in the list which we added
for i in elements:
	print "Element was: %d" % i
	
# general nested list
test_2d = [[],[]]

for i in range(0,5):
	test_2d[0].append(i)
	test_2d[1].append(i)
		
for row in test_2d:
	for column in row:
		print "Element in test_2d list %r" % column

# learn about jagged list
values = [[10,20], [30,40,50,60]]

for value in values:
	print len(value), value
	
