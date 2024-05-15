#Antone Simmons
#04/30/24
#P2HW1
#budget with $

print('This program calculates and displays travel expenses')
print('Enter Budget:', end='')
x=int(input())
print('Enter travel destination:', end='')
y=(input())
print('How much do you think you will spend on gas?', end='')
z=int(input())
print('Approximately, how much will you need for accomodation/hotel?', end='')
xx=int(input())
print('Last, how much do you need for food?', end='')
xxy=int(input())
print('-----------Travel Expenses-----------')
print('Location:', y)
print('Initial Budget:', f'${x: .2f}')
print('Fuel:', f'${z: .2f}')
print('Accomodation:',f'${xx: .2f}')
print('Food:', f'${xxy: .2f}')
print('--------------------------------------')
print('Remaining Balance:', f'${x - z - xx - xxy: .2f}')
