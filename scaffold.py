import random

class Player(object):
	max_hp = 100
	current_hp = 100

	# Check if the player is still alive 
	# by ensuring that his current hp is greater than 0
	def is_alive(self):
		# Fill this in!

	# Return True or False depending on whether the Player's
	# attack was successful
	def successful_attack(self):
		# Fill this in!

	# Heal the Player, if his health is not full already
	def rest(self):
		# Fill this in!

	# The player has been damaged! Decrease the Player's
	# current health by the appropriate amount
	def damage(self, dmg):
		# Fill this in!

	def print_current_health(self):
		print("You currently have " + str(self.current_hp) + " health.")

	def info(self):
		print("You are " + self.name + " the " + self.player + "!")
		print("You attack with " + str(self.accuracy * 100) + "% accuracy.")
		print("Your successful attacks deal " + str(self.attack) + " damage.")
		print("Every time you heal yourself, you heal " + str(self.heal) + " health")
		
	def kill(self):
		self.max_hp = 0


class Archer(Player):
	# input the appropriate attributes for the Archer
	def __init__(self, name):
		# Fill this in!

class Swordsman(Player):
	# input the appropriate attributes for the Swordsman
	def __init__(self, name):
		# Fill this in!

class Healer(Player):
	# input the appropriate attributes for the Healer
	def __init__(self, name):
		# Fill this in!

class GiantSpider():
	# input the appropriate attributes for the Spider
	def __init__(self):
		# Fill this in!

	# Check if the spider is still alive 
	# by ensuring that its current hp is greater than 0
	def is_alive(self):
		# Fill this in!

	# The player has been damaged! Decrease the Spider's
	# current health by the appropriate amount
	def damage(self, dmg):
		# Fill this in!

	# Return True or False depending on whether the Plaeyer's
	# attack was successful
	def successful_attack(self):
		# Fill this in!

	def print_current_health(self):
		print("The enemy currently has " + str(self.hp) + " health.\n")

def fight(player, enemy):
	while(player.is_alive() and enemy.is_alive()):
		player.print_current_health()
		enemy.print_current_health()
		move = input("What is your move? ")
		print("")
		while(move != "a" and move != "h"):
			print("Press a to attack, press h to heal\n")
			move = input("What is your move? ")
			print("")
	
		if(move == "a"):
			# Fill in this code!
			# What happens if the user wanted to attck?
		
		elif(move == "h"):
			# Fill in this code!
			# What happens if the user wanted to heal?
			
		if(enemy.successful_attack()):
			# Fill in this code!
			# What happens if the spider made a successful attack?
			
		else:
			# Fill in this code!
			# What happens if the spider missed its attack?

	return player.is_alive

name= input("Hello! What's your name? ")
while(name == ""):
	name = input("We will need your name to proceed! What is your name? ")

player_class = input("Hi " + name + "! What class of character would you want to be? ")
player = None
while(player_class != "a" and player_class != "s" and player_class != "h"):
	print("")
	print("Press a to be an archer, press s to be a swordsman, press h to be a healer")
	player_class = input("What class of character would you want to be? ")

# Based on what the user has chosen, how should you 
# initialize his/her character?
if(player_class == "a"):
	# Fill this in!

elif(player_class == "s"):
	# Fill this in!

elif(player_class == "h"):
	# Fill this in!

print("")
player.info()

num_steps = 0
print("\nYou are in a tunnel, and you must get out! It will take 10 steps to get out, but as you walk along you may encounter some spiders that you will need to fight. \nIf at any point in the game you are unsure what the commands are, just hit enter and you'll receive some instructions. Good luck!\n")
while(player.is_alive and num_steps < 10):
	step = input("What do you want to do? ")
	print("")
	if(step == "s"):
		# Fill in this code! What happens if a player takes a step?
		# Hint: In this step, the user either encounters a spider OR
		# the player does not encounter anything
		# What is the chance that the player encounters a spider?

		num_steps += 1
		print("You have made a total of " + str(num_steps) + " steps!\n")
	elif(step == "q"):
		player.kill()
		print("Better luck next time!")
		break
	else:
		print("Press s to take a step, press q to quit")

if(player.is_alive()):
	print("You won!")
