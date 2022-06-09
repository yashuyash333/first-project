x="Race"
y="Care"
x=x.lower()
y=y.lower()
if (len(x)) == (len(y)):
	sorted_x=sorted(x)
	sorted_y=sorted(y)
	if (sorted_x) == (sorted_y):
		print( x + " and " + x + " are anagram " )
	else:
		print(x+ " and " +y+" are not anagram ")
else:
	print(x+ " and " +y+" are not anagram ")

