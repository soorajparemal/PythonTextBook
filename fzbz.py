a=int(input("Enter the limit : "))
def fzbz(a):
	for i in range(a) :
		if i%3==0 and i%5==0:
			print 'Fizzbuzz'
		elif i%3==0:
			print 'Fizz'
		elif i%5==0:
			print 'Buzz'
		else:
			print (i)
fun=fzbz(a)
print "-------------------------------------------------"
print "FizzBuzz using list comprehension"
print "_________________________________________________"

b=int(input('Enter the limit : '))
lst = [(x, 'Fizz', 'Buzz', 'FizzBuzz') \
     [(not x % 3) | (not x % 5) << 1] for x in range(b)]
for x in lst:print x
