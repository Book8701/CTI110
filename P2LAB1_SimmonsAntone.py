# Antone Simmons
# 4/24/24
#Variables and Expressions
# A brief description of the project

import math 
ratio = float(input('What is the radius of the circle?'))
diameter = ratio * 2
circumference = 2 * math.pi * ratio
area = math.pi * ratio ** 2

print('The diameter of the circle is', diameter)
print('The circumference of the circle is', end = '')
print (f'{circumference: .2f}')
print('The area of the circle is', end = '')
print (f'{area: .3f}') 
