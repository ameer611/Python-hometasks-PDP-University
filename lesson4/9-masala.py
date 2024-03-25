# s va s0 satrlar berilgan. s satrdan s0 satr bilan ustma-ust tushuvchi oxirgi qism satr o‘chirilsin.
# Agar s satrda s0 satr topilmasa s satr o‘zgarishsiz chop etilsin

s= 'uny'
s0 = 'dunyo'
new = ''

index_ = s0.index(s)
for i in range(len(s0)):
    if i == index_:
        new += s0[i]

print(new)