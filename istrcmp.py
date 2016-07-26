#not case sensitive
a=raw_input("Enter your Username :")
b=raw_input("Re-enter your Username :")
x= a.upper()
y=b.upper()
def istrcmp(x,y):
	if x == y :
		return True
	else:
		return False
print istrcmp(x,y)
