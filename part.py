from math import *

# Define the lengths of the sides
a = 3 # length of side AB
b = 4 # length of side BC
c = hypot(a, b) # length of side AC

# Calculate the angle between sides AB and BC
angle = atan2(b, a)

print("Right-angled triangle with sides:", a, b, c)
print("Angle between sides AB and BC:", angle)