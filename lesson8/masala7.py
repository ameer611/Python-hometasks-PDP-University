def qurter(x, y):
    result = 0
    if x>0 and y>0:
        result = 1
    elif x>0 and y<0:
        result = 2
    elif x<0 and y<0:
        result = 3
    elif x<0 and y>0:
        result = 4
    else:
        result = result
    return result
        