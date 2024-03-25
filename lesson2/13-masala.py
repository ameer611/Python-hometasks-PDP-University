a = int(input("Uch xonali son kiriting: "))

right = a%10
left = a//100
middle = (a//10)%10

result = middle*100+right*10+left
print(result)