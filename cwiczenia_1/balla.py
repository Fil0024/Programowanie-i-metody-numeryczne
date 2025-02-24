import math
import sys

R=int(sys.argv[1])

pole_pow=4*math.pi*R**2
obj=4/3*math.pi*R**3

print("Pole powierzchni: " + str(pole_pow))
print("Objętość: " + str(obj))