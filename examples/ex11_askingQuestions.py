# raw_input() -  function is in-built function used in python to get input data from user

# example about asking questions from User
print "How old are you:? ",
age = raw_input()
print "How tall are you? ",
height = raw_input()
print "how much do you weigh? ",
weight = raw_input()

# print the values obtained from the User
print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)