import math

def circleS(r):
    if r>0:
        S = r**2*math.pi
    else:
        S = 'radius notugri'
    return S

print(circleS(10))
print(circleS(100))
print(circleS(1))