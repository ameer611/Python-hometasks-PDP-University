def calc(a, b, c):
    result = 0
    if c==1:
        result = a-b
    elif c==2:
        result = a*b
    elif c==3:
        result = a/b
    else:
        result=a+b
    return result