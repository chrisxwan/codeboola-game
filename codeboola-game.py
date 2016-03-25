import random

class Player(object):
	max_hp = 100
	current_hp = 100
	
	def is_alive(self):
		return self.current_hp > 0
	
	def successful_attack(self):
		rand = random.random()
		return rand < self.accuracy
	
	def rest(self):
		if(self.current_hp < self.max_hp):
			self.current_hp += self.heal
			if(self.current_hp > self.max_hp):
				self.current_hp = self.max_hp
			print("You healed yourself!")
		else:
			print("You are already at full health!")

	def damage(self, dmg):
		self.current_hp -= dmg

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
	def __init__(self, name):
		self.player = "Archer"
		self.name=name
		self.accuracy=0.3
		self.heal=5
		self.attack=10

class Swordsman(Player):
	def __init__(self, name):
		self.player = "Swordsman"
		self.name=name
		self.accuracy=0.7
		self.heal=5
		self.attack=5

class Healer(Player):
	def __init__(self, name):
		self.player = "Healer"
		self.name=name
		self.accuracy=0.9
		self.heal=10
		self.attack=2

class GiantSpider():
	def __init__(self):
		self.hp = 10
		self.attack = 2
		self.accuracy = 0.6

	def is_alive(self):
		return self.hp > 0

	def damage(self, dmg):
		self.hp -= dmg

	def successful_attack(self):
		rand = random.random()
		return rand < self.accuracy

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
			if(player.successful_attack()):
				print("You dealt " + str(player.attack) + " damage to the enemy!")
				enemy.damage(player.attack)
			else:
				print("You missed!")
		elif(move == "h"):
			player.rest()
			
		if(enemy.successful_attack()):
			print("The enemy dealt " + str(enemy.attack) + " to you!\n")
			player.damage(enemy.attack)
		else:
			print("The enemy missed its attack.\n")

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
	
if(player_class == "a"):
	player = Archer(name)
elif(player_class == "s"):
	player = Swordsman(name)
elif(player_class == "h"):
	player = Healer(name)

print("")
player.info()

num_steps = 0
print("\nYou are in a tunnel, and you must get out! It will take 10 steps to get out, but as you walk along you may encounter some spiders that you will need to fight. \nIf at any point in the game you are unsure what the commands are, just hit enter and you'll receive some instructions. Good luck!\n")
while(player.is_alive and num_steps < 10):
	step = input("What do you want to do? ")
	print("")
	if(step == "s"):
		chance = random.random()
		if(chance < 0.5):
			print("You have encountered a spider!")
			enemy = GiantSpider()
			battle = fight(player, enemy)
			if(battle == False):
				print("You died ): ")
				break
			else:
				print("You have conquered the enemy!\n")
			
	
	
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
