#Nelson Koomson
#1/22/2021

#Follow the instructions on the Lab Activity 2 sheet.
#This file should run without error and print the correct outputs


#Problem 1:
def say_hello():
    #This ask for the user's name and print it to them with a greetings
    name = input("What is your name? ")
    print("Hello", name)
    #Ask for the user's name
    #print their name with a nice message


#Problem 2:
def bmi():
    #This asks for the height and weight and prints the bmi for the person
    height = float(input("Your height is x "))
    weight = float(input("Your weight is y "))
    bmi = (weight/(height**2) * 703)
    return bmi
    #Ask for a user's height and weight
    #Be sure to put both into variables
    #Type out the equation on the assignment sheet
    #return the result of the equation
    

#Problem 3:
def total(price, amount):
    #This is the amount a person owes after buying multiple of the same item
    price = int(input("Price of an item is "))
    amount = int(input("Total number of same item bought is "))
    total = float(price * amount)
    return total
    #Multiply the price of an item by the amount purchased
    #Return the total owed
    
    
#Problem 4:
def add_up(num1, num2, num3):
    #This function takes three numbers and as parameters and returns the total
    total = num1+num2+num3
    return total
    #add the three parameters together and return the result


#***************************************
#Testing code
#
#DO NOT CHANGE ANY CODE BELOW THIS LINE
#***************************************

print("Problem 1:")
#Problem 1
#This should print the user's name along with a nice message.
say_hello()

print()

print("Problem 2:")
#Problem 2
#This line should display a user's bmi based on their height and weight
bmi = round(bmi(),2)
print("Your bmi is: ", bmi)

print()

print("Problem 3:")
#Problem 3
#This should print 67.2
print("Your total is: ", round(total(5.60, 12),2))
#This should print 59.96
print("Your other total is: ", total(14.99, 4))

print()

print("Problem 4:")
#Problem 4
#This should print 27
print("First add_up test: ", add_up(6, 9, 12))
#This should print 152
print("Second add_up test: ", add_up(45, 8, 99))

