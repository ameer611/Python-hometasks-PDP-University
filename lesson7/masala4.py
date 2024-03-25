dictionary = dict(b=1, g=9, r=10, a=95, s=0, d=5, y=4)
dictionary1 = dict(j=7, h=15, e=75)
dictionary2 = dict(u=852, c=78, n=714, m=45)

dictionary.update(dictionary1)
dictionary.update(dictionary2)
print(dictionary)