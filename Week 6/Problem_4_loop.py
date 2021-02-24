#Problem 4 loop
#Nelson Koomson
#2/18/21

#This function uses for loop to loop through the numbers 1 to 50
for number in range(1,51):
    #This prints numbers divisible by 3.
    if number %3 == 0:
        print(number, "Divisible by three!")

    #This prints numbers divisible by 5.
    if number %5 == 0:
        print(number, "Divisible by five!")

    #This prints numbers that are both divisible by 3 and 5.
    if number %3 == 0 and number %5 == 0:
        print(number, "Divisible by both!")

    #This prints all other numbers.
    else:
        print(number)