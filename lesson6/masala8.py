import random
sonlar = []
juftSonlar = []

n = 8
k = 0

for i in range(n):
    son = random.randint(1, 100)
    sonlar.append(son)
    if son%2==0:
        juftSonlar.append(son)

print(sonlar)
print(juftSonlar)
print(len(juftSonlar))


