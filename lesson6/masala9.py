import random
sonlar = []
toqSonlar = []

n = 8
k = 0

for i in range(n):
    son = random.randint(1, 100)
    sonlar.append(son)
    if son%2==0:
        toqSonlar.append(son)

print(sonlar)
print(sorted(toqSonlar))
print(len(toqSonlar))