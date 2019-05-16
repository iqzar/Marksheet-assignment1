# how to calculate mean from the list by using for loop and random,randint!
arr=[]
import random 
for i in range(100):
    arr.append(random.randint(1,100))
    a=arr[0]
    print(arr)
# calculation for mean
sum= 0
for j in range(len(arr)):
    sum=sum+arr[j]
print("Sum of observation is:", sum)
no_of_obervation = len(arr)
print("no of obervation is", no_of_obervation)
mean =sum/no_of_obervation
print("Mean is:", mean)
# calculation for min. and max. 
min_value = arr[0]
max_value = arr[0]
for a in range(len(arr)):
     if min_value> arr[a]: 
      min_value = arr[a]
      minimum_ind_position = a
     elif max_value< arr[a]:
        max_value = arr[a]
        maximum_ind_position = a
print("Maximum value is =", max_value) 
print("Minimum value is =", min_value)
   


