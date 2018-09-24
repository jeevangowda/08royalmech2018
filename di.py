import random
while True:
    a=input("enter 'r' to rool")
    if(a=='r'): 
       r=random.randint(1,6)
    print(r)
else:
	print('wrong key!!')
	'break'
