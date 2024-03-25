a = -2
b = -4
c = 5

if a<0 and b>0 and c>0 or a>0 and b<0 and c<0:
    print(1)
elif a > 0 and b < 0 and c > 0 or a < 0 and b > 0 and c < 0:
    print(2)
elif a > 0 and b > 0 and c < 0 or a < 0 and b < 0 and c > 0:
    print(3)
else:
    print(0)