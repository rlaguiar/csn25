import math

a = 15
r = math.sqrt(a)

b = 1
c = a-1
print(b)
print(c)
print(r, end="\n\n")

for i in range(10):
    b = (b+c)/2
    c = a/b
    print(i+1)
    print(b)
    print(c)
    print(r, end="\n\n")
    #if(b==c): break
    if (math.isclose(b, c)): break