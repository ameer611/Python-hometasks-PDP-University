a = -5
b = -5
c = -4

if a>0 and b>0 and c>0:
    print("uchta musbat")
elif (a<0 and b>0 and c>0) or (a>0 and b<0 and c>0) or (a>0 and b>0 and c<0):
    print('ikkita musbat, bitta manfiy')
elif (a>0 and b<0 and c<0) or (a<0 and b>0 and c<0) or (a<0 and b<0 and c>0):
    print('bitta musbat, ikkita manfiy')
else:
    print('uchta manfiy')