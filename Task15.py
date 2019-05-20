#Python program to compute the future value:
pv =int(input("Enter principle value: "))
r =int(input("Enter rate of interet: "))
n =int(input("Enter no. of years: "))
#formula for future value FV=pv(1+r)^n :
fv = pv*((1+(0.01*r))**n)
print("Futue value of principle amount is ",fv)