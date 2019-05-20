#Python program to convert all units of time into seconds:
hour =int(input("Enter time in hours: "))
min =int(input("Enter time in min: "))
time_1 =hour*60*60
time_2 =min*60
time_sec =round(time_1+time_2)
print("Time in seconds :",time_sec)