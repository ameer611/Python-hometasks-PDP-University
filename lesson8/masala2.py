def rootsCount(a, b, c):
    result = 0
    if a==0:
        result = 'Bu kvadrat tenglama emas'
    else:
        diskriminant = ((b ** 2) - (4 * a * c))
        if diskriminant>0:
            result = 2
        elif diskriminant<0:
            result = 0
        else:
            result = 1
    return result

p, q, c = 1, 4, 4
print(rootsCount(p, q, c))