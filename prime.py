c=0
x=int(input("enter the number:"))
z=x
for i in range(2,x):
y=x%2
if(y==0):
	c=c+1
	if(c>0):
		print(z,"is not a prime")
	else:
		print(z,"is a prime")