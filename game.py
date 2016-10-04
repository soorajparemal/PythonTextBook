print "Let The Games Begin"
print "```````````````````"
x=raw_input("Enter 'A' to attack the enemy or 'D' to defend from attack : ")
if x =='A' or x=='a':
	energy=int(input("Enter the strength of attack (Any number) :"))
elif x =='D' or x=='d':
	energy2=int(input("Enter the scale of defensive shield (Any number) : "))
else:
	print "Invalid input"
class game:
	def __init__(self,power=0):
		self.power=power

	def attack(self,energy):
		self.power += energy

	def defend(self,energy2):
		self.power -= energy2

	def energyleft(self):
		return self.power
if x=='A'or x=='a':
	gamer=game()
	gamer.attack(energy)
	print "The energy is "+ str(gamer.energyleft())
elif x=='D'or x=='d':
	gamer1=game()
	gamer1.defend(energy2)
	print "The energy left is "+ str(gamer1.energyleft()) 
else: 
	pass
