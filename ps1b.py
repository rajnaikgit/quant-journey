
portion_down_payment = 0.25
current_savings = 0
r = 0.04

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))

down_payment = portion_down_payment * total_cost

month_count = 0

while current_savings <= down_payment:
    monthly_salary = annual_salary / 12
    monthly_savings = portion_saved * monthly_salary
    current_savings = current_savings + ((current_savings*r)/12) + monthly_savings
    month_count = month_count + 1
    if (month_count % 6) == 0:
        annual_salary = annual_salary + (annual_salary * semi_annual_raise)

print("Number of months:", month_count)
