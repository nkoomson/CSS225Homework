#Nelson Koomson
#1/22/2021

#Problem 5
#This greets the customers when they start the self checkout
print("Hello Customer")

def amount_owe():
    #This asks for the number of an item a customer buys and calculates the amount owe for them.
    book = 4 * (float(input("How many books did you buy? ")))
    pen = 2 * (float(input("How many pens did you buy? ")))
    flashdrive = 8 * (float(input("How many flashdrive did you buy ")))
    amount_owe = (book + pen + flashdrive)
    return amount_owe





print("Problem 5:")
#Problem 5
amount_owe = float(amount_owe())
print("your amount_owe is ", amount_owe)





