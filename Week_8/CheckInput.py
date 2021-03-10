#CheckInput
#Nelson Koomson
#3/9/2021


#Problem 3
#This uses a while loop to check if that input is the letter A, B, or C.
letter = input("Pick a letter? A\n or B\n or C\n")
choice = letter.upper()
while choice != "A" and choice != "B" and choice != "C":
    choice = input("Try Again! Pick a letter")

#This will print well done if the letter A is selected.
print("Well done")