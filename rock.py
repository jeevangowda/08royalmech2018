import random
a={1:'r',2:'p',3:'s'}
while True:
	p=input("your choice r/p/s:")
	c=a[random.randint(1,3)]
	print("your chose:",p,"computer chose:",c)
	if(a==c):
		print("tie")
		if(a=1,c=2):
			print()


