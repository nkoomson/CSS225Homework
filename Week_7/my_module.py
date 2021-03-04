#my_module
#Nelson Koomson
#2/28/2021

import math
import random


#Problem 1
#This uses a for loop and random module to print 10 random integers between 25 and 35
def randum():
    for i in range(10):
        print(random.randrange(25,35))

#Problem 2
#This uses the random module to return random element from a list
def random_module(x):
    print(random.choice(x))


#Problem 3
#This function generates and returns a random odd integer between 0 and 100
def odd_integer():
    print(random.randrange(1,100,2))


#Problem 4
#This uses the sqrt() and pow() functions to calculate the Pythagorean theorem
def math_module():
   a = int(input("a = "))
   b = int(input("b = "))
   #c = math.sqrt(math.pow(a,2) + math.pow(b,2))
   #c = round(math.sqrt(a**2 + b**2), 2)
   #print("The result is:", c)

   c = round(math.sqrt(math.pow(a,2) + math.pow(b,2)))
   print("The result is:", c)