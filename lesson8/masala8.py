def even(a):
    result = True
    if a%2==0:
        result=result
    else:
        result=False
    return result

b = range(1,11)
count = 0
for i in b:
    if even(i):
        count+=1

print(count)