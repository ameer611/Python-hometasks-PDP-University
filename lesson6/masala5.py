fibonachi = [1, 1]
n = 8

for i in range(1, n):
    fibonachi.append(fibonachi[i]+fibonachi[i-1])

print(fibonachi)
