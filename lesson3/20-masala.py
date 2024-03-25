a = 151

right = a%10
left = a//100
middle = a//10%10

boolean = right!=left and right!=middle and middle!=left

print(boolean)