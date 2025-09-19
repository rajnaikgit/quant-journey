
semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25
total_cost = 1000000

down_payment = portion_down_payment * total_cost

low = 0
high = 10000

portion_saved = (low + high) / 2.0

epsilon = 100

steps = 0

annual_salary = float(input("Enter the starting salary: "))

def calculate_current_savings(annual_salary, portion_saved):
    current_savings = 0
    month_count = 0
    starting_salary = annual_salary
    while month_count < 36:
        monthly_salary = starting_salary / 12
        monthly_savings = (portion_saved / 10000) * monthly_salary
        current_savings = current_savings + ((current_savings*r)/12) + monthly_savings
        month_count = month_count + 1
        if (month_count % 6) == 0:
            starting_salary = starting_salary + (starting_salary * semi_annual_raise)
    return current_savings

if (calculate_current_savings(annual_salary, 10000) < (down_payment - epsilon)):
    print("It is not possible to pay the down payment in three years.")
    exit()

else:
    while (abs(calculate_current_savings(annual_salary, portion_saved) - down_payment) >= epsilon):
        if abs(calculate_current_savings(annual_salary, portion_saved) < down_payment):
            low = portion_saved
        else:
            high = portion_saved
        portion_saved = (low + high) / 2.0
        steps += 1

print("Best savings rate:", float(portion_saved / 10000))
print("Steps in bisection search:", steps)

