#Antone Simmons
#4/30/2024
#P2Lab2
#cars

veh = {"Camaro" : 18.21, "Prius" : 52.36, "Model S" :110, "Silverdo" : 26}
veh_list=list(veh)
print('The keys in the dictionary are:')
print(*veh_list, sep=", ")
name=input("Enter a vehicle to see it's mpg:")
print(f'The',name, 'gets',(veh[name]), 'mpg.')
miles=float(input("How many miles will you the "+name+"?"))
import math
print((f' {miles/veh[name] : .2f}'),('gallon (s) of gas are needed to drive the "+name+" "+miles" '))
