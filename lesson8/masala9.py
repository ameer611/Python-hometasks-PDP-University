def IsSquare(x):
    if x>0:
        ildiz = x**0.5
        if ildiz%1==0:
            result =  True
        else:
            result =  'bu xech qanday sonning kvadrati emas'
    else:
        result =  'bu xech qanday sonning kvadrati emas'
    return result

a = range(1,11)
print(a)
for i in a:
    print(IsSquare(i))