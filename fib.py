n=int(input("Enter the limit : "))
def fib(n):
	a,b=0,1
	while a < n :
		yield(a)
		a,b=b,a+b
a=fib(n)
for x in a:
	print x
