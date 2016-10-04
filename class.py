print "WELCOME TO ATM"
print "**************"
x=int(input("Enter 1 to deposit or 2 to withdraw : "))
if x==1:
	cash=int(input("Enter cash to be deposited : "))
elif x==2:
	cash1=int(input("Enter cash to be withdrawn : "))
else:
		print "Invalid input"
class Bank:
	def __init__(self,balance=0):
		self.balance=balance

	def deposit(self,cash):
		self.balance += cash
	
	def withdraw(self,cash1):
		self.balance -= cash1
	
	def checkbalance(self):
		return self.balance
if x==1:
	acc1=Bank()
	acc1.deposit(cash)
	print "Your balance was Zero and is now "  + str(acc1.checkbalance())
elif x==2:
	acc2=Bank()
	acc2.withdraw(cash1)
	print "Your balance was zero and is now  " + str(acc2.checkbalance())
else:
	pass
