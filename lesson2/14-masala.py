a = int(input("Uch xonali son kiriting: "))

right = a%10
left = a//100
middle = (a//10)%10

result = right*100+left*10+middle
print(result)