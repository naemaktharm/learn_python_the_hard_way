from sys import argv

script, filename = argv

text = open(filename)

print "The contents of the files are displayed below: \n"

print text.read()
