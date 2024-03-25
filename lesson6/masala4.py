hadlar = []

n = 7
b = 2
q = 3
hadlar.append(b)

for i in range(n):
    hadlar.append(hadlar[-1]*q)

print(hadlar)