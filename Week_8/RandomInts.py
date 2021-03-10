#RandomInts.py
#Nelson Koomson
#3/9/2021

import random


#Problem 2
#This uses a while loop and random module to print 10 random integers between 25 and 35
number = 1
while number <= 10:
    print(random.randint(25, 35))
    #print("The number is", number)
    number += 1