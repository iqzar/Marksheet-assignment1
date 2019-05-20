# Python program to convert height (in feet and inches) to centimetres:
height_feet =int(input("Enter height in feet: "))
height_inches =int(input("Enter height in inches: "))
hf =height_feet*30.48 
hi =height_inches*2.54
print("Height in centimeter= ",round(hf+hi))