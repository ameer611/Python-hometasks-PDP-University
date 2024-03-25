a = int(input("Uch xonali son kiriting: "))

right = a%10
left = a//100
middle = (a//10)%10

reverse = right*100+middle*10+left
print(reverse)