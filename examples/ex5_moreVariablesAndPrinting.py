# Variables about "Zed"
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.0 # inches
weight = 180.0 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
weight_in_kgs = weight * 0.453592
height_in_cms = height * 2.54

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "You want height in cms?, Yes! - %d" % height_in_cms
print "He's %d pounds heavy." % weight
print "you want weight in kgs?, Yay - %d" % weight_in_kgs 
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add age - %d, height - %d, and weight - %d I get %d." % (age, height, weight, age + height + weight)