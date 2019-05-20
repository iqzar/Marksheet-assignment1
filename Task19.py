#Python program to convert the distance (in feet) to inches, yards, and miles: 
# 1 feet = 12 inches, 3 feet = 1 yard, 5280 feet = 1 mile
distance=int(input("Enter distance in feet: "))
dis_inches=distance*12
dis_yard=distance*1/3
dis_mile=distance*1/5280
print("Distance in inches= ",dis_inches)
print("Distance in yards= ",dis_yard)
print("Distance in miles= ",dis_mile)