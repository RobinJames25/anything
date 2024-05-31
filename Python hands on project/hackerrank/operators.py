def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    
    tip=(meal_cost*tip_percent)/100
    tax=(meal_cost*tax_percent)/100
    total=tip+tax+meal_cost
    
    print(round(total))
    
meal_cost=float(input("Enter your meal cost: "))
tip_percent=int(input("Enter your tip percentage: "))
tax_percent=int(input("Enter your tax percentage: "))

solve(meal_cost, tip_percent, tax_percent)

    