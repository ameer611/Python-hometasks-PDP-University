import random
sonlar = []

n = 8

for i in range(n):
    sonlar.append(random.randint(1, 100))

print(sonlar)
print(sonlar[::-1])