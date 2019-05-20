#Python program that will return true if the two given integer values are equal or their sum or difference is 5.
f_num =int(input("Enter first number: "))
s_num =int(input("Enter second number:"))
if f_num == s_num or f_num+s_num == 5 or f_num-s_num == 5 :
    print("True")
else :
    print("Fasle")

