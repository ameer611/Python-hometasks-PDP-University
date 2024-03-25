a = int(input("Uch xonali son kiriting: "))

right = a%10
left = a//100
middle = (a//10)%10

chop_etish = (right*10)+middle
print(chop_etish)