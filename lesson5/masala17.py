a = 4.0
b = 4.5
c = 5.0

if a<b<c or c<b<a:
    a,b,c = a*2, b*2, c*2
else:
    a, b, c = a*(-1), b*(-1), c*(-1)

print(a, ' va ', b, ' va ', c)