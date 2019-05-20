#Python program to calculate the hypotenuse of a right angled triangle :
#Equation of right angled triangle is a^2+b^2=c^2 :
from math import sqrt
a =int(input("Enter value of a: "))
b =int(input("Enter value of b: "))
a2 =a**2
b2 =b**2
c =round (sqrt(a2+b2))
print("Hypotenuse of triangle is", c)