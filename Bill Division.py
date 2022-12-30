def bonAppetit2(bill, k, b):
    # Write your code here
    anna_charged = b
    acutal_charged = (sum(bill) - bill[k])/2
    over_charge = anna_charged - acutal_charged
    if  over_charge == 0:
        print("Bon Appetit")
    else:
        print(int(over_charge))

def bonAppetit(bill, k, b):
    # Write your code here
    anna_charged = b
    acutal_charged = (sum(bill) - bill[k])/2
    over_charge = anna_charged - acutal_charged
    outcome = "Bon Appetit" if over_charge == 0 else int(over_charge)
    print(outcome)

bonAppetit([3,10,2,9], 1, 12)