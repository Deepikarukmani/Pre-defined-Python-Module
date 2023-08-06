def biggest(n1,n2):
    if n1>n2:
        print(n1,"is greater")
    else:
        print(n2, "is greater")

no1 = int(input("enter no:"))
no2 = int(input("enter no2:"))

python.biggest
#modules in python

import math

print(math.sqrt(100))
print(math.sqrt(25))
print(math.sqrt(10))

print(math.pi)

print(math.pow(10,3))

print(math.ceil(5.2))
print(math.ceil(5.8))

print(math.floor(4.7))
print(math.floor(4.2))

print(math.factorial(5))

print(math.trunc(5.1234))

print(math.gcd(3,5))



from math import pi

radius = int(input("enter radius "))

area = pi* radius * radius
print("Area of circle is",  round(area))



#eval()  -----> string input

expression =input("enter your expression") #5*2/10-3/4

print(expression)

expression = eval(expression)

print(expression)


#sys module: commamd line argument
no = [1,2,3,4,5]

from sys import argv

print(argv[0])


print(type(argv))