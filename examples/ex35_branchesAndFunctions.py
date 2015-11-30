from sys import exit

def gold_room():
	# print the statements and prompting the user to send commands
	print "This room is full of gold. How much do you take?"
	
	# prompting the user to send commands
	choice = raw_input('> ')
	
	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("Man. learn to type a number")
	
	if how_much < 50:
		print "Nice! You are not greedy. You win!!!"
		exit(0)
	else:
		dead("You greedy bastard!")

def bear_room():
	# print the statements and prompting the user to send commands
	print "There is a bear here."
	print "Bear has a bunch of honey."
	print "Fat Bear is in front of another room."
	print "How are you going to move the bear?"
	
	# initially setting the variable - bear_moved as False
	bear_moved = False
	
	# while function will be executed infinity times, till any other function is called 
	while True:
		
		# prompting the user to send the commands
		choice = raw_input('> ')
		
		# if user selects the choice as "take honey", print the message
		if choice == "take honey":
			print "The bear looks at you and slaps your face off."
			
		# if user selects the choice as taunt bear first time, print the message
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now"
			bear_moved = True
		
		# if user selects the choice as taunt bear second time, print the message
		elif choice == "taunt bear" and bear_moved:
			print "The bear gets pissed off and chews your leg off."
		
		# if user selects the choice - open door, gold_room() function will be invoked
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."

def cthulhu_room():
	print "Here you see that Great evil Cthulhu."
	print "He, it, watever stares at you and you go insane."
	print "Do you flee for life or eat ur head?"
	
	choice = raw_input('> ')
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!!!")
	else:
		cthulhu_room()
		
def dead(why):
	print why, "Good Job!"
	exit(0)
	
def start():
	# print the message to the user and prompting the user to send the commands
	print "Welcome"
	print "You are in a dark room"
	print "There is a door in ur left and right?"
	print "Which one do you take?"
	
	# prompting the user
	choice = raw_input('> ')
	
	# if user selects the choice - left -> bear_room() function is invoked
	if "left" in choice:
		bear_room()
		
	# if user selects the choice - right -> cthulhu_room() function is invoked
	elif "right" in choice:
		cthulhu_room()
	else:
		print "You stumble around the room until you starve"

# invoking the start function
start()	