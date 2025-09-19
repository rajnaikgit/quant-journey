
portion_down_payment = 0.25
current_savings = 0
r = 0.04

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

down_payment = portion_down_payment * total_cost
monthly_salary = annual_salary / 12
monthly_savings = portion_saved * monthly_salary
month_count = 0

while current_savings <= down_payment:
    current_savings = current_savings + ((current_savings*r)/12) + monthly_savings
    month_count = month_count + 1

print("Number of months:", month_count)



