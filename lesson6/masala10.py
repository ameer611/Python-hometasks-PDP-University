import random
sonlar = []
toqSonIndex = []
juftSonIndex = []

n = 8

for i in range(n):
    son = random.randint(1, 100 )
    sonlar.append(son)

for i in range(n):
    if sonlar[i]%2==0:
        juftSonIndex.append(i)
    else:
        toqSonIndex.append(i)

print(sonlar)
print(juftSonIndex)
print(toqSonIndex[::-1])