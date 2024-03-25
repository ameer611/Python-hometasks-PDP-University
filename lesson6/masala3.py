hadlar = []

n = 7
a = 2
d = 3
hadlar.append(a)

for i in range(n):
    hadlar.append(hadlar[-1]+d)

print(hadlar)