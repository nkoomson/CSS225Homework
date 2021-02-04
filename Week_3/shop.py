#shop.py
#Nelson Koomson
#2/2/21


def check_money(total_cost, customer_money):
    #This uses the "if" statement to check if a customer can pay for the total cost of items bought
    total_cost = float(input("Your total cost is "))
    customer_money = float(input("How much do you have? "))
    if total_cost < customer_money:
        can_pay = True
        return can_pay
    if total_cost > customer_money:
        can_pay = False
        return can_pay


#This should print False
can_pay = check_money(107, 49)
print(can_pay)

#This should print True
can_pay = check_money(6, 88)
print(can_pay)
