'''small grocery shop'''
print("welcome to the grocery shop")
print("happy shopping in our shop ")
print("as per our shop price for rice is '70' kg")
print("as per our shop price for sugar is '50'kg")
print("as per our shop price for biscuits is '10' pack")
print("as per our shop price for juice is '10' 1lt bottle")
print("enter you have taken the quntity of rice as in ' KG '")
n=int(input())
print("enter you have taken the quntity of sugar as in ' KG '")
m=int(input())
print("enter you have taken the quntity of biscuits as in ' PACKETS '")
o=int(input())
print("enter you have taken the quntity of rice as in ' BOTTLES '")
q=int(input())
print("you have taken the rice is :",n,"kg")
c=n*70
print(c)
print("you have taken the sugar is :",m,"kg")
v=m*50
print(v)
print("you have taken the biscuits is :",o,"packets")
b=o*10
print(b)
print("you have taken the  juice bottles is :",q,"bottles")
z=q*10
print(z)
total=c+v+b+z;
print("total is:",total)
per=total-70
print(per/100)
print("enter the customer  paid")
int(input())
change=total
