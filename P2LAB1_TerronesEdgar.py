# Edgar C Terrones
# 09/23/25
# P1HW2
# Circle Calculations

import math 

print("What is the radius of the Circle?")
radius = float(input())
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius** 2

print("The diameter of the circle is", f"{diameter:.1f}")
print("The cirumference of the circle is", f"{circumference:.2f}")
print("The area of the circle is", f"{area:.3f}")
