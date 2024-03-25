a = 55
b = 55

if a == b:
    a,b = 0, 0
else:
    a = a+b
    b = a

print(a, " va ", b)