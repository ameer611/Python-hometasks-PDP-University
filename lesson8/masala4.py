import math

def ringS(r1, r2):
    if r1>0 and r2>0:
        Skatta = max(r1, r2) ** 2 * math.pi
        Skichik = min(r1, r2) ** 2 * math.pi
        S = Skatta-Skichik
    else:
        S = 'radius notugri'
    return S

print(ringS(4, 2))
print(ringS(2, 1))
print(ringS(3, 2))