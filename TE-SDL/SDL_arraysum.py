#Calculate sum of all array elements present in a array
array = input("\nEnter array elements: ").split()

sum = 0
for i in array:
    sum += int(i)
print("Sum of array elements: ",sum)
print("\n")
