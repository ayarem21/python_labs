import math

radius = float(input("Enter the radius: "))
height = float(input("Enter the height: "))
conevol = 1 / 3 * math.pi * radius * 2 * height
cylvol = math.pi * radius**2 * height
spherevol = 3 / 4 * math.pi * radius**3

print("The volume of a cone: ", conevol)
print("The volume of a cylinder: ", cylvol)
print("The volume of a sphere: ", spherevol)