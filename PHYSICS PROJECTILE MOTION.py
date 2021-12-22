import math
v = float(input("Enter the veloocity(m/s) - "))
g = float(input("Enter the value of gravity(m/s^2) - "))
H = float(input("Cannon Height(m) - "))
angle = int(input("Angle in degree: "))
sina = math.sin(math.radians(angle))
cosa = math.cos(math.radians(angle))
sin2a = math.cos(math.radians(2*angle))

max_height = (v*v*sina*sina)/(2*g)
max_height = H + max_height
print(f"MAXIMUM HEIGHT FROM GROUD: 2{max_height}m")

a = (g/2)
b = -v*sina
c = -H
dis = (b**2) - (4 * a*c)
time = (-b + math.sqrt(dis))/(2 * a)
print(f"TIME OF FLIGHT: {time.real}sec")

# RANGE
range = v*cosa*time.real
print(f"RANGE : {range}m")
