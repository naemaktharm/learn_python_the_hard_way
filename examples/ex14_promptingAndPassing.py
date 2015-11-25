# import argv module from system
from sys import argv

# unpacking arguments and assigning to the variables
script, user_name = argv
prompt = '> '

# print the statements and get information from the users
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "What kind of headphones do you own?"
headphones = raw_input(prompt)

print "What company headphones do you own?"
headphones_company = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer and own a %s %s headphones. Nice.
""" % (likes, lives, computer, headphones, headphones_company)