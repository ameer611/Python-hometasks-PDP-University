a = 2
b = 11
c = 5
d = 7

if a%2==0 and b%2==1 and c%2==1 and d%2==1 or a%2==1 and b%2==0 and c%2==0 and d%2==0:
    print(1)
elif a%2==1 and b%2==0 and c%2==1 and d%2==1 or a%2==0 and b%2==1 and c%2==0 and d%2==0:
    print(2)
elif a%2==1 and b%2==1 and c%2==0 and d%2==1 or a%2==0 and b%2==0 and c%2==1 and d%2==0:
    print(3)
elif a%2==1 and b%2==1 and c%2==1 and d%2==0 or a%2==0 and b%2==0 and c%2==0 and d%2==1:
    print(4)
else:
    print(0)