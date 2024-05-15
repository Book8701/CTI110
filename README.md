#Antone Simmons

#5/6/24

#structures

#calculting overtime



employee_name = input("Enter employee's name :")
weekly_hours = float(input("Enter hours of worked:"))
pay_rate = float(input("Enter employee's pay rate :"))

print("---------------------")
print("Employee's name:\t", employee_name)
print()

if (weekly_hours < 40):

   overtime = 0

elif(weekly_hours > 40):

    overtime =  weekly_hours - 40

overtime_pay = overtime * 1.5 * pay_rate

hourly_pay = min(weekly_hours, 40) * pay_rate

gross = hourly_pay + overtime_pay
  

print(f'{"Hours Worked":<13}  {"Pay Rate":<8}  {"Overtime":<10}  {"Overtime Pay":<13}  {"Reghour Pay":<11}  {"Gross Pay":<10}')
print("------------------------------------------------------------------------")
print(f"{weekly_hours:<13.1f}  {pay_rate:<8.2f}  {overtime:<10.1f}  ${overtime_pay:<12.2f}  ${hourly_pay:<11.2f}  ${gross:<9.2f}")

