def sign(x):
    result = 0
    if x>0:
        result = 1
    elif x<0:
        result = -1
    else:
        result = result
    return result

a = -15
b = 15
print(sign(a), ' ', sign(b))