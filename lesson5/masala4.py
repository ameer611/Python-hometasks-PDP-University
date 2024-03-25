a = -5
b = -5
c = -4

if a>0 and b>0 and c>0:
    print("uchta")
elif (a<0 and b>0 and c>0) or (a>0 and b<0 and c>0) or (a>0 and b>0 and c<0):
    print('ikkita')
elif (a>0 and b<0 and c<0) or (a<0 and b>0 and c<0) or (a<0 and b<0 and c>0):
    print('bitta')
else:
    print('yoq')
