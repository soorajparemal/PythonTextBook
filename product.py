#To get user input as a list and to find the product of numbers inside
num= input("Enter the numbers to be multiplied (no commas) : ")
numbers = list(map(int , num.split()))
def product(p):
	total = 1
	for i in p:
		total=total*i
	return total
print (product(numbers))
	
	
