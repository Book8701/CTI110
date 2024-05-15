
#Antone Simmons
#5/4/24
#P3LAB
#Debugging


amount_input = int(input())
if amount_input > 0:    
    dollar = amount_input // 100
    amount_input %= 100
    quarter = amount_input // 25
    amount_input %=25
    dime = amount_input //10
    amount_input %= 10
    nickel = amount_input // 5
    amount_input %= 5
    penny = amount_input
    
    if dollar == 1:
        print(dollar, "Dollar")
    elif dollar > 1: 
        print(dollar, "Dollars")
    if quarter == 1:
        print(quarter, "Quarter")
    elif quarter > 1: 
        print(quarter, "Quarters")
    if dime == 1:
        print(dime, "Dime")
    elif dime > 1: 
        print(dime, "Dimes")    
    if nickel == 1:
        print(nickel, "Nickel")
    elif nickel > 1: 
        print(nickel, "Nickels")    
    if penny == 1:
        print(penny, "Penny")
    elif penny > 1: 
        print(penny, "Pennies")
else:
    print("No change")
