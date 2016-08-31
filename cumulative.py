nums=raw_input("Enter the digits seperated by comma : ")
b=list(nums.split(','))
entries=map(int,b)
print entries
sums = []
total=0
for e in entries:
	total += e
	sums.append(total)
print 'Values : ', entries
print 'Sums : ', sums



