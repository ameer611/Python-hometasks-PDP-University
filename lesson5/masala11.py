a = -5
b = 55

if a == b:
    a,b = 0, 0
else:
    if a>b:
        b = a
    else:
        a = b

print(a, " va ", b)