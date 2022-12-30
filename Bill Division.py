def bonAppetit(bill, k, b):
    # Write your code here
    anna_charged = b
    acutal_charged = (sum(bill) - bill[k])/2
    over_charge = anna_charged - acutal_charged
    if  over_charge == 0:
        print("Bon Appetit")
    else:
        print(int(over_charge))

bonAppetit([3,10,2,9], 1, 12)