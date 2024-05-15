#Antone Simmons
#5/8/24
#P4HW2
#Overtime/Gross




employee_count = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0


while True:
    
    employee_name = input("Enter employee's name or \"Done\" to terminate: ")
    
    if employee_name == "Done":
        break

    hours_worked = float(input("How many hours did {} work? ".format(employee_name)))
    pay_rate = float(input("What is {}'s pay rate? ".format(employee_name)))

    overtime_hours = max(0, hours_worked - 40)
    overtime_pay = overtime_hours * pay_rate * 1.5
    regular_hour_pay = (hours_worked - overtime_hours) * pay_rate
    gross_pay = regular_hour_pay + overtime_pay

    employee_count += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_hour_pay
    total_gross_pay += gross_pay

    print("Employee name: {}".format(employee_name))
    print("Hours Worked \tPay Rate \tOverTime \tOverTime Pay \tRegHour Pay \tGross Pay")
    print("---------------------------------------------------------------------------------------------------------")
    print("{:.1f} \t\t{:.2f} \t\t{:.1f} \t\t{:.2f} \t\t${:.2f}\t\t${:.2f}".format(hours_worked, pay_rate, overtime_hours, overtime_pay, regular_hour_pay, gross_pay))
    print()

print("Total number of employees entered:", employee_count)
print("Total amount paid for overtime: ${:.2f}".format(total_overtime_pay))
print("Total amount paid for regular hours: ${:.2f}".format(total_regular_pay))
print("Total amount paid in gross: ${:.2f}".format(total_gross_pay))
