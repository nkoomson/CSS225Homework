#Problem 3 average
#Nelson Koomson
#2/18/21

#This function uses for loop to print the average of 10 numbers
total = 0
#for number in [2,3,5,7,8,10,14,16,17,22]:
for number in range(1,11):
    total += number
    average = total / 10
    print(average, "is average")