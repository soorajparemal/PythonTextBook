print "MY PUPPY STORE"
print "______________"
print "--------------"
x=raw_input("Suggest a name for the puppy you like : ")
y=int(input("Enter the number of puppies you want : "))
class puppy:
	def __init__(self,num=0):
		self.num=num
	
	def name(self,x):
		return x.upper() + ' ! What a nice name ! '
	
	def number(self,y):
		self.num += y
		return self.num
	
pup1=puppy()
print pup1.name(x)
con=raw_input( 'You want ' + str(pup1.number(y)) + ' puppies right ? ')
if con =='yes' or con=='y' or con=='Yes':
	print "Thanks. Visit Again! "
elif con =='no' or con=='No' or con=='n':
	so=int(input("Please confirm the number : "))
	if so is int:
		print "Okey . thanks for shopping :"
	else:
		numbb=int(input("Enter the  number and try again after a while ! "))
		print "Okay visit again !"
else:
	print"Enter 'yes' or 'no' ! "
