sonlar = []

n = 7
a = 8
b = 6
sonlar.append(a)
sonlar.append(b)

for i in range(n):
    sonlar.append(sum(sonlar))

print(sonlar)