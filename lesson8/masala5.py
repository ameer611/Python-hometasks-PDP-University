def Range(a,b):
    if a>b or a==b:
        result = 0
    else:
        a = range(a, b+1)
        result = sum(a)
    return result

print(Range(3, 8))
print(Range(8, 5))