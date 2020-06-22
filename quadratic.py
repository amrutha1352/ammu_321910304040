a=float(input("enter the  a value")
b=float(input("enter the b value "))
c=float(input("enter the c value"))
if(a==0):
	print("it is not a quadratic equation")
else:
	d=((b*b)-(4*a*c))
	if(d==0):
		print("the roots are real and equal")
		x=(-b/(2*a))
		y=x
		print(x,"and",y,"are the rooys of the quadratic equation")
	elif(d>0):
			print("the roots are real and distinct")
			e=pow(d,0.5)
			x=((-b+e)/(2*a))
			y=((-b-e)/(2*a))
			print(x,"and",y,"are the rots of the quadratic equation")
	else:
		 print("the roots are imaginary")
		 e=pow(d,0.5)
		 x=(-b/(2*a))
		 y=(e/(2*a))
		 print(x,"+i",y,"and",x,"-i",y,"are the roots of a quadratic equatiin")
		 