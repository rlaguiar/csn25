import math

r = 5.11

area = 3.14 * r * r
print("2 casas dec: ", area)

area = 3.1415 * r * r
print("4 casas dec: ", area)

area = 3.14 * math.pow(r, 2)
print("2 casas e pow: ", area)

area = 3.1415 * math.pow(r, 2)
print("4 casas e pow: ", area)

area = math.pi*math.pow(r, 2)
print("tudo math:", area)

print(math.pi.__format__('.99f'))

