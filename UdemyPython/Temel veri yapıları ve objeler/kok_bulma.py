a= int(input("a:"))
b= int(input("b:"))
d= int(input("d:"))
delta=b**2- 4*a*d
print("Sayıların deltası= {}".format(delta))
x1=(-b-delta**0.5) /(2*a)
x2=(-b+delta**0.5) /(2*a)
print("Birinci kök ={}\nİkinci kök={}\n".format(x1,x2))